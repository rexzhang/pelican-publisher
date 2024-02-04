# Pelican Publisher

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

An automatic build/publish service for [Pelican](https://getpelican.com) website in docker

## Install

```shell
docker pull ray1ex/pelican-publisher
```

## Configuration

Create file `pelican-publisher.env`

```env
PELICAN_PUBLISHER_DOMAIN=pelican-publisher.rexzhang.com
PELICAN_SITES=[{"NAME":"rexzhang.com","ZIP_URL":"https://github.com/rexzhang/rexzhang.com/archive/master.zip","WEBHOOK_SECRET":"please-change-it-!"},{"NAME":"sample.com","ZIP_URL":"https://sample.com/master.zip","WEBHOOK_SECRET":"secret"}]
```

- `PELICAN_PUBLISHER_DOMAIN` is your publisher host's domain, empty will accept any domain
- `PELICAN_PUBLISHER_PREFIX` is your URL prefix path
- `PELICAN_SITES` in JSON format, empty is `[]`
- `SENTRY_DSN` is your sentry client key (DSN)

## Start Service

```shell
docker run -dit -p 127.0.0.1:8000:8000 --restart unless-stopped \
  -v=/var/www:/output -v=$(pwd)/data:/data \
  --env-file pelican-publisher.env \
  --name pelican-publisher ray1ex/pelican-publisher
```

- Your site will output to path `/var/www/SITE_NAME`
- Your database file db.sqlite3 will at `$(pwd)/data/db.sqlite3`

## Setup Webhook

- Github
  - Payload URL: like this
        `https://pelican-publisher.rexzhang.com/webhook/github/rexzhang.com`
  - Content type: application/json

## Example

| instance          | <https://pelican-publisher.rexzhang.com>   |
|-------------------|------------------------------------------|
| source            | <https://github.com/rexzhang/rexzhang.com> |
| target            | <https://rexzhang.com>                     |

## TODO

- processing task info

## Development

`http://127.0.0.1:8000/webhook/test` trigger task
`build_pelican_site_task`
