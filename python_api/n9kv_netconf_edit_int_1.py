#!/usr/bin/env python3

from ncclient import manager
from ncclient.operations.rpc import RPCError


def main():
    with manager.connect(host='192.168.181.21',
                         port=830,
                         username="admin",
                         password="cisco",
                         hostkey_verify=False,
                         device_params={'name': 'nexus'},
                         allow_agent=False,
                         look_for_keys=False
                         ) as cisco_manager:

        descr_cfg = '''
        <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
          <interfaces xmlns="http://openconfig.net/yang/interfaces">
              <interface>
                  <name>eth1/33</name>
                  <config>
                      <description>NEW INPUT</description>
                  </config>
              </interface>
          </interfaces>
        </config>
        '''

        try:
            resp = cisco_manager.edit_config(descr_cfg, target='running',
                                             default_operation='merge')
            print(resp)
            print('*' * 30)
        except RPCError as err:
            for attr in dir(err):
                if not attr.startswith('__'):
                    print(attr, ':   ', getattr(err, attr))


if __name__ == '__main__':
    main()
