#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for eos_lacp_interfaces
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'network'
}

DOCUMENTATION = '''
---
module: eos_lacp_interfaces
short_description: Manage Link Aggregation Control Protocol (LACP) attributes of interfaces on Arista EOS devices.
description:
  - This module manages Link Aggregation Control Protocol (LACP) attributes of interfaces on Arista EOS devices.
author: Nathaniel Case (@Qalthos)
notes:
- Tested against Arista EOS 4.20.10M
- This module works with connection C(network_cli). See the
  L(EOS Platform Options,../network/user_guide/platform_eos.html).
options:
  config:
    description: A dictionary of LACP interfaces options.
    type: list
    elements: dict
    suboptions:
      name:
        description:
          - Full name of the interface (i.e. Ethernet1).
        type: str
      port_priority:
        description:
          - LACP port priority for the interface. Range 1-65535.
        type: int
      rate:
        description:
          - Rate at which PDUs are sent by LACP.
            At fast rate LACP is transmitted once every 1 second.
            At normal rate LACP is transmitted every 30 seconds after the link is bundled.
        type: str
        choices: ['fast', 'normal']
  state:
    description:
      - The state of the configuration after module completion.
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    default: merged
'''
EXAMPLES = """
# Using merged
#
#
# ------------
# Before state
# ------------
#
#
# veos#show run | section ^interface
# interface Ethernet1
#    lacp port-priority 30
# interface Ethernet2
#    lacp rate fast

- name: Merge provided configuration with device configuration
  eos_lacp_interfaces:
    config:
      - name: Ethernet1
        rate: fast
      - name: Ethernet2
        rate: normal
    state: merged

#
# -----------
# After state
# -----------
#
# veos#show run | section ^interface
# interface Ethernet1
#    lacp port-priority 30
#    lacp rate fast
# interface Ethernet2


# Using replaced
#
#
# ------------
# Before state
# ------------
#
#
# veos#show run | section ^interface
# interface Ethernet1
#    lacp port-priority 30
# interface Ethernet2
#    lacp rate fast

- name: Replace existing LACP configuration of specified interfaces with provided configuration
  eos_lacp_interfaces:
    config:
      - name: Ethernet1
        rate: fast
    state: replaced

#
# -----------
# After state
# -----------
#
# veos#show run | section ^interface
# interface Ethernet1
#    lacp rate fast
# interface Ethernet2
#    lacp rate fast


# Using overridden
#
#
# ------------
# Before state
# ------------
#
#
# veos#show run | section ^interface
# interface Ethernet1
#    lacp port-priority 30
# interface Ethernet2
#    lacp rate fast

- name: Override the LACP configuration of all the interfaces with provided configuration
  eos_lacp_interfaces:
    config:
      - name: Ethernet1
        rate: fast
    state: overridden

#
# -----------
# After state
#
#
# veos#show run | section ^interface
# interface Ethernet1
#    lacp rate fast
# interface Ethernet2


# Using deleted
#
#
# ------------
# Before state
# ------------
#
#
# veos#show run | section ^interface
# interface Ethernet1
#    lacp port-priority 30
# interface Ethernet2
#    lacp rate fast

- name: Delete LACP attributes of given interfaces (or all interfaces if none specified).
  eos_lacp_interfaces:
    state: deleted

#
# -----------
# After state
# -----------
#
# veos#show run | section ^interface
# interface Ethernet1
# interface Ethernet2


"""
RETURN = """
before:
  description: The configuration as structured data prior to module invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The configuration as structured data after module completion.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['interface Ethernet1', 'lacp rate fast']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.misc.not_a_real_collection.plugins.module_utils.network.eos.argspec.lacp_interfaces.lacp_interfaces import Lacp_interfacesArgs
from ansible_collections.misc.not_a_real_collection.plugins.module_utils.network.eos.config.lacp_interfaces.lacp_interfaces import Lacp_interfaces


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=Lacp_interfacesArgs.argument_spec,
                           supports_check_mode=True)

    result = Lacp_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
