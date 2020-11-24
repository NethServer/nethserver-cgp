==============
nethserver-cgp
==============

Expose collectd metrics using Collectd Graph Panel (CGP): https://github.com/pommi/CGP

Database example: ::

 cgp=configuration
    alias=02bf3f8364beea0d5f23044bf14d31d93f63e98d

The ``alias`` is a random path generated once on first install and it will be used to compose CGP URL.

So in this case will be acessibile from ``https://<fqdn>:980/02bf3f8364beea0d5f23044bf14d31d93f63e98d``.

Where ``<fqdn>`` is the fully qualified domain name of the server or its IP address.

