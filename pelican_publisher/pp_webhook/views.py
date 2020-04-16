#!/usr/bin/env python
# coding=utf-8


import hmac
from hashlib import sha1
from datetime import datetime
from logging import getLogger

from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseServerError, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.utils.encoding import force_bytes
import requests
from ipaddress import ip_address, ip_network

from pp_core.runtimes.common import get_site_info_by_name
from pp_core.tasks import build_pelican_site_task

logger = getLogger(__name__)


def test(request):
    build_pelican_site_task.delay('rexzhang.com', datetime.now())
    return HttpResponse('success')


@csrf_exempt
@require_http_methods(["GET", "POST"])
def github_webhook(request, site_name):
    if request.method != 'POST':
        return HttpResponseRedirect('/')

    # https://simpleisbetterthancomplex.com/tutorial/2016/10/31/how-to-handle-github-webhooks-using-django.html
    # https://gist.github.com/vitorfs/145a8b8f0865cb65ee915e0c846fc303
    # Verify if request came from GitHub
    forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if forwarded_for is None:
        logger.warning('HTTP_X_FORWARDED_FOR is None')
        return HttpResponseForbidden('Permission denied.')

    client_ip_address = ip_address(forwarded_for)
    whitelist = requests.get('https://api.github.com/meta').json()['hooks']

    for valid_ip in whitelist:
        if client_ip_address in ip_network(valid_ip):
            break
    else:
        logger.warning('ip not in whitelist')
        return HttpResponseForbidden('Permission denied.')

    # Verify the request signature
    header_signature = request.META.get('HTTP_X_HUB_SIGNATURE')
    if header_signature is None:
        logger.warning('HTTP_X_HUB_SIGNATURE is None')
        return HttpResponseForbidden('Permission denied.')

    sha_name, signature = header_signature.split('=')
    if sha_name != 'sha1':
        return HttpResponseServerError('Operation not supported.', status=501)

    site_info = get_site_info_by_name(site_name)

    mac = hmac.new(force_bytes(site_info['SECRET']), msg=force_bytes(request.body), digestmod=sha1)
    if not hmac.compare_digest(force_bytes(mac.hexdigest()), force_bytes(signature)):
        logger.warning('webhook SECRET no match')
        return HttpResponseForbidden('Permission denied.')

    # If request reached this point we are in a good shape
    # Process the GitHub events
    event = request.META.get('HTTP_X_GITHUB_EVENT', 'ping')

    if event == 'ping':
        return HttpResponse('pong')
    elif event == 'push':
        # Deploy some code for example
        logger.debug(request.body)
        build_pelican_site_task.delay(site_name, datetime.now())
        logger.info('webhook request process finished')
        return HttpResponse('success')

    # In case we receive an event that's not ping or push or other support event
    logger.warning('can not support event: {}'.format(event))
    return HttpResponse('Can not support event: {}'.format(event), status=204)
