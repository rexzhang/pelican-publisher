#################
Pelican Publisher
#################

    An automatic build/publish service for `pelican <https://blog.getpelican.com/>`__ website in docker


Install
-------

.. code-block::

    docker pull ray1ex/pelican-publisher

Configuration
-------------

Create file ``pelican-publisher.env``

.. code-block::

    PELICAN_PUBLISHER_DOMAIN=pelican-publisher.rexzhang.com
    PELICAN_SITE_NAME=rexzhang.com
    PELICAN_SITE_SOURCE_ZIP_URL=https://github.com/rexzhang/rexzhang.com/archive/master.zip
    PELICAN_SITE_SECRET=your-github-webhook-secret


Start Service
-------------

.. code-block::

    docker run -dit -p 127.0.0.1:8000:8000 -v=/var/www/pelican-publisher:/publisher-output --env-file pelican-publisher.env --name pelican-publisher ray1ex/pelican-publisher

Your site will output to path ``/var/www/pelican-publisher``

Example
-------
=================   ========================================
source git repos    https://github.com/rexzhang/rexzhang.com
-----------------   ----------------------------------------
target website      https://rexzhang.com
=================   ========================================


TODO
----
- processing task info
- multi-site


Issues
------
Redis

    you have Transparent Huge Pages (THP) support enabled in your kernel. This will create latency and memory usage issues with Redis. To fix this issue run the command 'echo never > /sys/kernel/mm/transparent_hugepage/enabled' as root, and add it to your /etc/rc.local in order to retain the setting after a reboot. Redis must be restarted after THP is disabled.

celery

    RuntimeWarning: You're running the worker with superuser privileges: this is absolutely not recommended!
