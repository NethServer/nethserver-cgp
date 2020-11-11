==============
nethserver-cgp
==============

Expose collectd metrics using Collectd Graph Panel (CGP): https://github.com/pommi/CGP

Database example: ::

 cgp=configuration
    PublicAccess=enabled
    alias=02bf3f8364beea0d5f23044bf14d31d93f63e98d

The ``alias`` is a random path generated once on first install and it will be used to compose CGP URL.

So in this case will be acessibile from:

- ``https://<fqdn>:980/02bf3f8364beea0d5f23044bf14d31d93f63e98d``
- ``https://<fqdn>/02bf3f8364beea0d5f23044bf14d31d93f63e98d``

Where ``<fqdn>`` is the fully qualified domain name of the server or its IP address.

Restrict access
===============

As default CGP is accessible from all IP addresses.
To restrict the access only from local and trusted networks use: ::

  config setprop cgp PublicAccess disabled
  signal-event nethserver-cgp-update
