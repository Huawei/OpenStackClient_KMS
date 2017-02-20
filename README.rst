python-kmclient
=====================

This is a `OpenStack Client`_ plugin for HuaWei Volume Backup Management API
which provides **command-line scripts** (integrated with openstack) and
Python library for accessing the Cloud-Eye management API.


Installation
------------

1. Install python-openstackclient
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This project is a plugin of  `OpenStack Client`_. Therefor, you need
to have `OpenStack Client`_ installed before using the plugin. You can
install `OpenStack Client`_ by pip::

    pip install python-openstackclient

*To get more information about python-openstackclient, please check the
official site* `OpenStack Client`_

2. Install plugin
^^^^^^^^^^^^^^^^^^

Currently, We can install the plugin from source code

.. code:: console

    $ git clone https://github.com/Huawei/OpenStackClient_VBS python-kmclient
    $ cd python-kmclient
    # use python setup.py develop for test purpose
    $ python setup.py install
    $ pip install -r requirements.txt


Command Line Client Usage
-----------------------------------------

.. note::

    The command line client is self-documenting. Use the --help or -h flag to access the usage options.
    You can find more command line client examples `here <./commands.rst>`_


This plugin is integrated with `OpenStack Client`_ , so the command line client
follow all the usage **openstack** provided.


Show Help for command::

    $ openstack --help
    usage: openstack [--version] [-v | -q] [--log-file LOG_FILE] [-h] [--debug]
                 [--os-cloud <cloud-config-name>]
                 [--os-region-name <auth-region-name>]
                 [--os-cacert <ca-bundle-file>] [--os-cert <certificate-file>]
                 [--os-key <key-file>] [--verify | --insecure]
                 [--os-default-domain <auth-domain>]
                 [--os-interface <interface>] [--timing] [--os-beta-command]
                 [--os-profile hmac-key]
                 [--os-compute-api-version <compute-api-version>]
                 [--os-network-api-version <network-api-version>]
                 [--os-image-api-version <image-api-version>]
                 [--os-volume-api-version <volume-api-version>]
                 [--os-identity-api-version <identity-api-version>]
                 [--os-object-api-version <object-api-version>]
                 [--os-queues-api-version <queues-api-version>]
                 [--os-clustering-api-version <clustering-api-version>]
                 [--os-search-api-version <search-api-version>]
                 .......


Volume-Backup-Service Client contains commands list in table below, use -h
option to get more usage


1. Show Help for `Create Volume Backup`::

    $ openstack volume backup create ext -h
    usage: openstack volume backups create [-h] [--name <name>]
                                           [--description <description>]
                                           <volume>

    Create new volume backup (HuaWei custom)

    positional arguments:
      <volume>              Volume to backup (name or ID)

    optional arguments:
      -h, --help            show this help message and exit
      --name <name>         Name of the backup
      --description <description>
                            Description of the backup

#. Create Volume Backup::

    $ openstack volume backup ext create volume-telia-WS1 --name
    A1-QianBiao-Test --description=QianBiao-Test-purpose
        --os-vb-endpoint-override=https://vbs.eu-de.otc.t-systems.com
    Request Received, job id: 2c9eb2c559b8a2c2015a0e039f095821

#. Restore Volume Backup::

    # restore backup `A1-QianBiao-Test` for volume `volume-telia-WS1`
    $ openstack volume backup ext restore A1-QianBiao-Test volume-telia-WS1
    Request Received, job id: 2c9eb2c559b8a2c2015a0e039f095821

#. Show volume backup job::

    # show volume backup job
    $ openstack volume backup job show 2c9eb2c559b8a2c2015a0e039f095821 --os-vb-api-version=1
        --os-vb-endpoint-override=https://vbs.eu-de.otc.t-systems.com
    +------------+-----------------------------------------------------------------------------------------------------------------------+
    | Field      | Value                                                                                                                 |
    +------------+-----------------------------------------------------------------------------------------------------------------------+
    | Id         | 2c9eb2c559b8a2c2015a0e039f095821                                                                                      |
    | Type       | bksCreateBackup                                                                                                       |
    | Begin Time | 2017-02-05T11:23:22.760Z                                                                                              |
    | End Time   | 2017-02-05T11:27:19.557Z                                                                                              |
    | Entities   | backup_id='c6be4287-6707-4f5b-84ef-07013851b60d', bks_create_volume_name='autobk_volume_2017-02-05T11:23:36.346Z',    |
    |            | snapshot_id='34f14aeb-cede-4e1b-8d9f-14a2c43bae9f', volume_id='a5109cba-1b1f-4d40-b3a9-753bc808b66a'                  |
    | Status     | SUCCESS                                                                                                               |
    +------------+-----------------------------------------------------------------------------------------------------------------------


Python Library Usage
-------------------------------

The full api is documented in the `Volume Backup Official Document`_ site

Here's an example of listing antiddos status using Python library with keystone V3 authentication:

.. code:: python

    >>> from keystoneauth1 import session
    >>> from keystoneauth1 import client
    >>> from kmclient.v2 import client

    >>> # Use Keystone API v3 for authentication as example
    >>> auth = identity.v3.Password(auth_url=u'http://localhost:5000/v3',
    ...                             username=u'admin_user',
    ...                             user_domain_name=u'Default',
    ...                             password=u'password',
    ...                             project_name=u'demo',
    ...                             project_domain_name=u'Default')

    >>> # Next create a Keystone session using the auth plugin we just created
    >>> session = session.Session(auth=auth)

    >>> # Now we use the session to create a CloudEye client
    >>> client = client.Client(session=session)

    >>> # Then we can access all Volume Backup API
    >>> client.backup_mgr.create('volume-1', name='volume-1-backup')
    {"job_id" : "xxxxx"}




    >>> from keystoneauth1 import session
    >>> from keystoneauth1 import client
    >>> from kmclient.v2 import client

    >>> # Use Keystone API v3 for authentication as example
    >>> auth = identity.v3.Password(auth_url=u'http://localhost:5000/v3',
    ...                             username=u'admin_user',
    ...                             user_domain_name=u'Default',
    ...                             password=u'password',
    ...                             project_name=u'demo',
    ...                             project_domain_name=u'Default')

    >>> # Next create a Keystone session using the auth plugin we just created
    >>> session = session.Session(auth=auth)

    >>> # Now we use the session to create a CloudEye client
    >>> client = client.Client(session=session)

    >>> # Then we can access all Volume Backup API
    >>> client.backup_mgr.create('volume-1', name='volume-1-backup')
    {"job_id" : "xxxxx"}




    >>> from keystoneauth1 import session
    >>> from keystoneauth1 import client
    >>> from kmclient.v2 import client

    >>> # Use Keystone API v3 for authentication as example
    >>> auth = identity.v3.Password(auth_url=u'http://localhost:5000/v3',
    ...                             username=u'admin_user',
    ...                             user_domain_name=u'Default',
    ...                             password=u'password',
    ...                             project_name=u'demo',
    ...                             project_domain_name=u'Default')

    >>> # Next create a Keystone session using the auth plugin we just created
    >>> session = session.Session(auth=auth)

    >>> # Now we use the session to create a CloudEye client
    >>> client = client.Client(session=session)

    >>> # Then we can access all Volume Backup API
    >>> client.backup_mgr.create('volume-1', name='volume-1-backup')
    {"job_id" : "xxxxx"}


.. note::

    The example above must be running and configured to use the Keystone Middleware.

    For more information on setting this up please visit: `KeyStone`_


* License: Apache License, Version 2.0
* `OpenStack Client`_
* `Volume Backup Official Document`_
* `KeyStone`_

.. _OpenStack Client: https://github.com/openstack/python-openstackclient
.. _Volume Backup Official Document: http://support.hwclouds.com/vbs/
.. _KeyStone: http://docs.openstack.org/developer/keystoneauth/
