#################
Pelican Publisher
#################

    An automatic build/publish service for `Pelican <https://getpelican.com/>`__ website in docker


Install
-------

.. code-block::

    docker pull ray1ex/pelican-publisher

Configuration
-------------

Create file ``pelican-publisher.env``

.. code-block::

    PELICAN_PUBLISHER_DOMAIN=pelican-publisher.rexzhang.com
    PELICAN_SITES=[{"NAME":"rexzhang.com","ZIP_URL":"https://github.com/rexzhang/rexzhang.com/archive/master.zip","SECRET":"please-change-it-!"},{"NAME":"sample.com","ZIP_URL":"https://sample.com/master.zip","SECRET":"secret"}]

- ``PELICAN_PUBLISHER_DOMAIN`` is your publisher host's domain, empty will accept any domain
- ``PELICAN_SITES`` in JSON format, empty is ``[]``

Start Service
-------------

.. code-block::

    docker run -dit -p 127.0.0.1:8000:8000 -v=/var/www/pp-output:/pp-output -v=/var/www/pp-data:/pp-data --env-file pelican-publisher.env --name pelican-publisher ray1ex/pelican-publisher

- Your site will output to path ``/var/www/pp-output/SITE_NAME``
- Your database file db.sqlite3 will at ``/var/www/pp-data/db.sqlite3``

Setup Webhook
-------------

webhook url like this ``https://pelican-publisher.rexzhang.com/webhook/github/rexzhang.com``

Example
-------
=================   ========================================
instance            https://pelican-publisher.rexzhang.com
-----------------   ----------------------------------------
source              https://github.com/rexzhang/rexzhang.com
-----------------   ----------------------------------------
target              https://rexzhang.com
=================   ========================================


TODO
----
- processing task info


Issues
------
Redis

    WARNING: The TCP backlog setting of 511 cannot be enforced because /proc/sys/net/core/somaxconn is set to the lower value of 128.
    WARNING you have Transparent Huge Pages (THP) support enabled in your kernel. This will create latency and memory usage issues with Redis. To fix this issue run the command 'echo never > /sys/kernel/mm/transparent_hugepage/enabled' as root, and add it to your /etc/rc.local in order to retain the setting after a reboot. Redis must be restarted after THP is disabled.

celery

    RuntimeWarning: You're running the worker with superuser privileges: this is absolutely not recommended!
