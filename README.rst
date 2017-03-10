python-kmclient
=====================

This is a `OpenStack Client`_ plugin for HuaWei Key Manager Management API
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

    $ git clone https://github.com/Huawei/OpenStackClient_KMS python-kmclient
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


Key Manager Client contains commands list below, use -h option to get more usage

1. key create(创建密钥)::

    $ openstack kms key create qianbiao-ng --realm eu-de --description desc
        --sequence 919c82d4-8046-4722-9094-35c3c6524cff
    +-----------+--------------------------------------+
    | Field     | Value                                |
    +-----------+--------------------------------------+
    | Key ID    | b919e712-3743-4f7d-8d9e-8730a94aea0b |
    | Domain Id | bb42e2cd2b784ac4bdc350fb660a2bdb     |
    +-----------+--------------------------------------+


#. Key show(查询密钥信息)::

    $ openstack key show 0a7a3f08-1529-4b30-a7bd-d74d97a908a9
    +-------------------------+--------------------------------------+
    | Field                   | Value                                |
    +-------------------------+--------------------------------------+
    | ID                      | 0a7a3f08-1529-4b30-a7bd-d74d97a908a9 |
    | alias                   | alias_5292                           |
    | type                    | 1                                    |
    | status                  | Enabled                              |
    | description             |                                      |
    | Default Key             | False                                |
    | Realm                   | eu-de                                |
    | Domain ID               | bb42e2cd2b784ac4bdc350fb660a2bdb     |
    | Creation date           | 2017-02-22 13:27:20                  |
    | Scheduled deletion date |                                      |
    +-------------------------+--------------------------------------+


#. Key list(查询密钥列表)::

    $ openstack kms key list --limit 2 --marker 2
    +-------------+--------------------------------------+
    | Field       | Value                                |
    +-------------+--------------------------------------+
    | Key list    | 1c985324-43ff-4f81-bb3f-e818afba65fb |
    |             | 4074f2b5-3455-4f08-bbbf-b5a321114dc4 |
    | Next Marker | 4                                    |
    | Truncated   | true                                 |
    +-------------+--------------------------------------+



#. Key enable(启用密钥)::

    $ openstack key enable 0a7a3f08-1529-4b30-a7bd-d74d97a908a9
        --sequence 0f31a9f0-f9a2-11e6-8448-3c970e4b3294
    Key 0a7a3f08-1529-4b30-a7bd-d74d97a908a9 enabled


#. Key disable(禁用密钥)::

    $ openstack key disable 0a7a3f08-1529-4b30-a7bd-d74d97a908a9
        --sequence 0f31a9f0-f9a2-11e6-8448-3c970e4b3294
    Key 0a7a3f08-1529-4b30-a7bd-d74d97a908a9 disabled

#. key schedule deletion(计划删除密钥)::

    $ openstack kms key schedule deletion b919e712-3743-4f7d-8d9e-8730a94aea0b --pending-days 7
    +--------+--------------------------------------+
    | Field  | Value                                |
    +--------+--------------------------------------+
    | Key ID | b919e712-3743-4f7d-8d9e-8730a94aea0b |
    | Status | Pending Deleted                      |
    +--------+--------------------------------------+

#. key cancel deletion(取消计划删除密钥)::

    $ openstack kms key cancel deletion b919e712-3743-4f7d-8d9e-8730a94aea0b
    +--------+--------------------------------------+
    | Field  | Value                                |
    +--------+--------------------------------------+
    | Key ID | b919e712-3743-4f7d-8d9e-8730a94aea0b |
    | Status | Disabled                             |
    +--------+--------------------------------------+


#. datakey create(创建数据密钥)::

    $ openstack kms datakey create --key-id b919e712-3743-4f7d-8d9e-8730a94aea0b
        --encryption-context v1=k1 --encryption-context v2=k2 --datakey-length 512
    +-------------+------------------------------------------------------------------------------------------------------------------+
    | Field       | Value                                                                                                            |
    +-------------+------------------------------------------------------------------------------------------------------------------+
    | Key ID      | b919e712-3743-4f7d-8d9e-8730a94aea0b                                                                             |
    | Plain Text  | 1E08EEFF1F448C337F96DA0C47BC872CF56C21E94797F8C01905553155502B550E3EE49A512C2D3791FCA6279B794D5A59633EA6B4B7C629 |
    |             | 1EAECEF9CDC87C49                                                                                                 |
    | Cipher Text | 0200980070C9A6B7F45250BAAC58DF5B0E6D919668763C30E13A5798BA26D3CCBB7825AD29AAA122012978D8113428D6B86CD6981FEDB0AB |
    |             | 5288624458BD0781CD3FB57B0AAC3D901CEF558C4899F73436BF9579011AC87E95C78F8E8716ABF5865F7F1A2FEB1AF4570D19B9F3E77659 |
    |             | 48AA01A462393139653731322D333734332D346637642D386439652D383733306139346165613062000000000027E250019B9FE8030DD81A |
    |             | 8A7BED06D7E6DB6F64DF530A3FED2F2980E66F47                                                                         |
    +-------------+------------------------------------------------------------------------------------------------------------------+


    # create encrypt data pair without plain text returned
    $ openstack kms datakey create --key-id b919e712-3743-4f7d-8d9e-8730a94aea0b  --datakey-length 512
        --without-plain-text --encryption-context v1=k1 --encryption-context v2=k2
    +-------------+------------------------------------------------------------------------------------------------------------------+
    | Field       | Value                                                                                                            |
    +-------------+------------------------------------------------------------------------------------------------------------------+
    | Key ID      | b919e712-3743-4f7d-8d9e-8730a94aea0b                                                                             |
    | Cipher Text | 02009800F60C9999C6216A1FEA7DCDD4650A03DD6D40C5C4371036EDDA50934FBD67B6DA60813F879747D0C9DCBE4AA377A8CC28176E71C2 |
    |             | ACBABAC3FE7BAFF2F03C522E29A96BC40B237F63CB5C88F43B1DD08DA5ED789484BD92EC5A31C2485D54E9DACE711EAACE99CB4A1868E1AB |
    |             | 844366FD62393139653731322D333734332D346637642D386439652D3837333061393461656130620000000053105B3AA14552C0A1D2607C |
    |             | 0ECC9032DD3F3517CCE325D2C2B623645519B563                                                                         |
    +-------------+------------------------------------------------------------------------------------------------------------------+


#. datakey encrypt(加密数据密钥)::

    $ openstack kms datakey encrypt --key-id 0d0466b0-e727-4d9c-b35d-f84bb474a37f
        --encryption-context k1=v1 --plain-text plaintext --datakey-plain-length 64
    +-------------+------------------------------------------------------------------------------------------------------------------+
    | Field       | Value                                                                                                            |
    +-------------+------------------------------------------------------------------------------------------------------------------+
    | Key ID      | b919e712-3743-4f7d-8d9e-8730a94aea0b                                                                             |
    | Cipher Text | 0200980070C9A6B7F45250BAAC58DF5B0E6D919668763C30E13A5798BA26D3CCBB7825AD29AAA122012978D8113428D6B86CD6981FEDB0AB |
    |             | 5288624458BD0781CD3FB57B0AAC3D901CEF558C4899F73436BF9579011AC87E95C78F8E8716ABF5865F7F1A2FEB1AF4570D19B9F3E77659 |
    |             | 48AA01A462393139653731322D333734332D346637642D386439652D383733306139346165613062000000000027E250019B9FE8030DD81A |
    |             | 8A7BED06D7E6DB6F64DF530A3FED2F2980E66F47                                                                         |
    +-------------+------------------------------------------------------------------------------------------------------------------+

    $ openstack kms datakey encrypt --key-id 0d0466b0-e727-4d9c-b35d-f84bb474a37f
        --encryption-context k1=v1 --plain-text file://c://1.txt --datakey-plain-length 64
    +-------------+------------------------------------------------------------------------------------------------------------------+
    | Field       | Value                                                                                                            |
    +-------------+------------------------------------------------------------------------------------------------------------------+
    | Key ID      | b919e712-3743-4f7d-8d9e-8730a94aea0b                                                                             |
    | Cipher Text | 0200980070C9A6B7F45250BAAC58DF5B0E6D919668763C30E13A5798BA26D3CCBB7825AD29AAA122012978D8113428D6B86CD6981FEDB0AB |
    |             | 5288624458BD0781CD3FB57B0AAC3D901CEF558C4899F73436BF9579011AC87E95C78F8E8716ABF5865F7F1A2FEB1AF4570D19B9F3E77659 |
    |             | 48AA01A462393139653731322D333734332D346637642D386439652D383733306139346165613062000000000027E250019B9FE8030DD81A |
    |             | 8A7BED06D7E6DB6F64DF530A3FED2F2980E66F47                                                                         |
    +-------------+------------------------------------------------------------------------------------------------------------------+

#. datakey decrypt(解密数据密钥)::

    $ openstack kms datakey decrypt --cipher-text xxxxxx --key-id b919e712-3743-4f7d-8d9e-8730a94aea0b
        --encryption-context v1=k1 --encryption-context v2=k2 --datakey-cipher-length 64
    +-------------+------------------------------------------------------------------------------------------------------------------+
    | Field       | Value                                                                                                            |
    +-------------+------------------------------------------------------------------------------------------------------------------+
    | Key ID      | b919e712-3743-4f7d-8d9e-8730a94aea0b                                                                             |
    | Plain Text  | 0200980070C9A6B7F45250BAAC58DF5B0E6D919668763C30E13A5798BA26D3CCBB7825AD29AAA122012978D8113428D6B86CD6981FEDB0AB |
    |             | 5288624458BD0781CD3FB57B0AAC3D901CEF558C4899F73436BF9579011AC87E95C78F8E8716ABF5865F7F1A2FEB1AF4570D19B9F3E77659 |
    +-------------+------------------------------------------------------------------------------------------------------------------+

    $ openstack kms datakey decrypt --cipher-text file://c://1.txt --key-id b919e712-3743-4f7d-8d9e-8730a94aea0b
        --encryption-context v1=k1 --encryption-context v2=k2 --datakey-cipher-length 64
    +-------------+------------------------------------------------------------------------------------------------------------------+
    | Field       | Value                                                                                                            |
    +-------------+------------------------------------------------------------------------------------------------------------------+
    | Key ID      | b919e712-3743-4f7d-8d9e-8730a94aea0b                                                                             |
    | Plain Text  | 0200980070C9A6B7F45250BAAC58DF5B0E6D919668763C30E13A5798BA26D3CCBB7825AD29AAA122012978D8113428D6B86CD6981FEDB0AB |
    |             | 5288624458BD0781CD3FB57B0AAC3D901CEF558C4899F73436BF9579011AC87E95C78F8E8716ABF5865F7F1A2FEB1AF4570D19B9F3E77659 |
    +-------------+------------------------------------------------------------------------------------------------------------------+

#. random generate(创建随机数)::

    $ openstack kms random generate 512 --sequence 919c82d4-8046-4722-9094-35c3c6524cff
    ABB030187057A4A7DF642BD7F57CE79EDB1BE3DF98E002DF753B6F53DB22FE8A33BD413BF0149BF55260EFDC7BC78446323A95704D81C77A767B25E1DBE74F7A


Python Library Usage
-------------------------------

The full api is documented in the `Key Manager Official Document`_ site

Here's an example of listing antiddos status using Python library with keystone V3 authentication:

.. code:: python

    >>> from keystoneauth1 import session
    >>> from keystoneauth1 import identity
    >>> from kmclient.v1 import client

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

    >>> # Then we can access all Key Manager API
    >>> client.keys.get('key-id-1')
    <Key creation_date=1487741240000 .....>



.. note::

    The example above must be running and configured to use the Keystone Middleware.

    For more information on setting this up please visit: `KeyStone`_


* License: Apache License, Version 2.0
* `OpenStack Client`_
* `Key Manager Official Document`_
* `KeyStone`_

.. _OpenStack Client: https://github.com/openstack/python-openstackclient
.. _Key Manager Official Document: http://support.hwclouds.com/kms/index.html
.. _KeyStone: http://docs.openstack.org/developer/keystoneauth/
