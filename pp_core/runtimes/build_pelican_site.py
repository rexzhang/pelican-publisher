import os.path
import subprocess
from logging import getLogger
from pathlib import Path, PurePath
from shutil import rmtree
from uuid import uuid4
from zipfile import ZipFile

import requests
from django.conf import settings

from pp_core.runtimes.common import get_site_info_by_name

logger = getLogger(__name__)


def _run_subprocess_run(cmd):
    r = subprocess.run(cmd, capture_output=True, encoding="utf-8", text=True)
    return_code = r.returncode
    output = r.stdout
    output += "\n"
    output += r.stderr

    logger.info(f"returncode: {return_code}")
    return return_code, output


def build_pelican_site(site_name):
    site_info = get_site_info_by_name(site_name)

    # get source
    site_stage_path, site_file_path = _download_and_extract_zip_from_github(site_info)
    if site_file_path is None:
        return

    # generate site
    content_path = PurePath(site_file_path).joinpath("content")
    pelicanconf_file = PurePath(site_file_path).joinpath("pelicanconf.py")
    publishconf_file = Path(site_file_path).joinpath("publishconf.py")
    if publishconf_file.exists():
        settings_file = publishconf_file
    else:
        settings_file = pelicanconf_file

    result = _generate_site_to_local_file(
        pelican_content_path=content_path,
        pelican_settings_file=settings_file,
        site_info=site_info,
    )

    # cleanup
    if not settings.DEBUG:
        rmtree(site_stage_path, ignore_errors=True)

    return result


def _download_and_extract_zip_from_github(site_info):
    """
    from https://pelican-blog/archive/master.zip
    to: /path/pelican-blog
    """
    unique_id = uuid4().hex
    zip_file_url = site_info["ZIP_URL"]

    zip_file_name = os.path.join(
        settings.PELICAN_PUBLISHER["WORKING_ROOT"],
        "{}-{}.zip".format(site_info["NAME"], unique_id),
    )
    site_stage_path = os.path.join(
        settings.PELICAN_PUBLISHER["WORKING_ROOT"],
        "{}-{}".format(site_info["NAME"], unique_id),
    )
    logger.debug(f"zip file name: {zip_file_name}")
    logger.debug(f"site stage path: {site_stage_path}")

    # download zip file
    r = requests.get(zip_file_url)
    if not r.ok:
        logger.error("download failed")
        return None, None

    open(zip_file_name, "wb").write(r.content)
    logger.info("download finished")

    # extract zip file
    ZipFile(zip_file_name).extractall(site_stage_path)

    # pelican site file check
    site_file_path = None
    for p in Path(site_stage_path).glob("*"):
        if p.is_dir():
            site_file_path = p.as_posix()
            break

    if site_file_path is None:
        logger.error("pelican site file extract failed, more subdir")
        return None, None

    logger.info(f"extracted pelican site file to: {site_file_path}")
    return site_stage_path, site_file_path


def _generate_site_to_local_file(
    pelican_content_path, pelican_settings_file, site_info
):
    output_path = os.path.join(
        settings.PELICAN_PUBLISHER["OUTPUT_ROOT"], site_info["NAME"]
    )
    return_code, output = _run_subprocess_run(
        [
            "pelican",
            "-s",
            pelican_settings_file,
            "-o",
            output_path,
            pelican_content_path,
        ]
    )

    logger.info(f"build to: {output_path} finished")
    return output


def test(arg1, arg2):
    logger.info("this is test logging message")
    return_code, output = _run_subprocess_run(["ls", "-la"])
    return output
