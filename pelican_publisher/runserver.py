#!/usr/bin/env python


import argparse

import uvicorn


def cli_parser():
    """CLI args parse"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--host", "-H", type=str, default=None, help="The interface to bind to."
    )
    parser.add_argument(
        "--port", "-p", type=int, default=None, help="The port to bind to."
    )
    parser.add_argument(
        "--workers",
        "-w",
        type=int,
        default=None,
        help="Number of worker processes. "
        "Defaults to the $WEB_CONCURRENCY environment variable if available. "
        "Not valid with --reload.",
    )

    return parser.parse_args()


def main():
    cli_args = cli_parser()

    kwargs = {
        "app": "pelican_publisher.asgi:application",
        "lifespan": "off",  # won't fix:  https://code.djangoproject.com/ticket/31508
    }

    for key, arg in (
        ("host", cli_args.host),
        ("port", cli_args.port),
        ("workers", cli_args.workers),
    ):
        if arg:
            kwargs[key] = arg

    uvicorn.run(**kwargs)


if __name__ == "__main__":
    main()
