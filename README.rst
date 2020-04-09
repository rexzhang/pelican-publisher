Pelican Publisher
#################

    An automatic build/publish service for `pelican <https://blog.getpelican.com/>`__ website in docker


Setup
-----

Create file `pelican-publisher.env`

.. code-block::

    PELICAN_SITE_SECRET=your-github-webhook-secret

Create docker pod

.. code-block::

    docker pull ray1ex/pelican-publisher
    docker run -dit -p 127.0.0.1:8000:8000 -v=/var/www/pelican-output:/pelican-output --env-file pelican-publisher.env --name pelican-publisher ray1ex/pelican-publisher

Your site output path

    /var/www/pelican-output

Example
-------
=================   ========================================
source git repos    https://github.com/rexzhang/rexzhang.com
-----------------   ----------------------------------------
target website      https://rexzhang.com
=================   ========================================


TODO
----
- publish/build history
- publish/build task detail info
- current task info


Issues
------
Redis

    you have Transparent Huge Pages (THP) support enabled in your kernel. This will create latency and memory usage issues with Redis. To fix this issue run the command 'echo never > /sys/kernel/mm/transparent_hugepage/enabled' as root, and add it to your /etc/rc.local in order to retain the setting after a reboot. Redis must be restarted after THP is disabled.
