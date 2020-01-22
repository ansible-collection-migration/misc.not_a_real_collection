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
The module file for exos_vlans
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: exos_vlans
short_description:  Manage VLANs on Extreme Networks EXOS devices.
description: This module provides declarative management of VLANs on Extreme Networks EXOS network devices.
author: Jayalakshmi Viswanathan (@jayalakshmiV)
notes:
  - Tested against EXOS 30.2.1.8
  - This module works with connection C(httpapi).
    See L(EXOS Platform Options,../network/user_guide/platform_exos.html)
options:
  config:
    description: A dictionary of VLANs options
    type: list
    elements: dict
    suboptions:
      name:
        description:
          - Ascii name of the VLAN.
        type: str
      vlan_id:
        description:
          - ID of the VLAN. Range 1-4094
        type: int
        required: True
      state:
        description:
          - Operational state of the VLAN
        type: str
        choices:
          - active
          - suspend
        default: active
  state:
    description:
      - The state the configuration should be left in
    type: str
    choices:
      - merged
      - replaced
      - overridden
      - deleted
    default: merged
'''
EXAMPLES = """
# Using deleted

# Before state:
# -------------
#
# path: /rest/restconf/data/openconfig-vlan:vlans/
# method: GET
# data:
# {
#   "openconfig-vlan:vlans": {
#     "vlan": [
#       {
#         "config": {
#           "name": "Default",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 1
#         },
#       },
#       {
#         "config": {
#           "name": "vlan_10",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 10
#         },
#       },
#       {
#         "config": {
#           "name": "vlan_20",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 20
#         },
#       },
#       {
#         "config": {
#           "name": "vlan_30",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 30
#         },
#       }
#     ]
#   }
# }

- name: Delete attributes of given VLANs
  exos_vlans:
    config:
      - vlan_id: 10
      - vlan_id: 20
      - vlan_id: 30
    state: deleted

# Module Execution Results:
# -------------------------
#
# "after": [
#     {
#         "name": "Default",
#         "state": "active",
#         "vlan_id": 1
#     }
# ],
#
# "before": [
#     {
#         "name": "Default",
#         "state": "active",
#         "vlan_id": 1
#     },
#     {
#         "name": "vlan_10",
#         "state": "active",
#         "vlan_id": 10
#     },
#     {
#         "name": "vlan_20",
#         "state": "active",
#         "vlan_id": 20
#     }
#     {
#         "name": "vlan_30",
#         "state": "active",
#         "vlan_id": 30
#     }
# ],
#
# "requests": [
#     {
#        "data": null,
#        "method": "DELETE",
#        "path": "/rest/restconf/data/openconfig-vlan:vlans/vlan=10"
#     },
#     {
#	 "data": null,
#        "method": "DELETE",
#        "path": "/rest/restconf/data/openconfig-vlan:vlans/vlan=20"
#     },
#     {
#	 "data": null,
#        "method": "DELETE",
#        "path": "/rest/restconf/data/openconfig-vlan:vlans/vlan=30"
#     }
# ]
#
#
#  After state:
# -------------
#
# path: /rest/restconf/data/openconfig-vlan:vlans/
# method: GET
# data:
# {
#   "openconfig-vlan:vlans": {
#     "vlan": [
#       {
#         "config": {
#           "name": "Default",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 1
#         },
#       }
#     ]
#   }
# }


# Using merged

# Before state:
# -------------
# path: /rest/restconf/data/openconfig-vlan:vlans/
# method: GET
# data:
# {
#   "openconfig-vlan:vlans": {
#     "vlan": [
#       {
#         "config": {
#           "name": "Default",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 1
#         },
#       }
#     ]
#   }
# }

- name: Merge provided configuration with device configuration
  exos_vlans:
    config:
      - name: vlan_10
        vlan_id: 10
        state: active
      - name: vlan_20
        vlan_id: 20
        state: active
      - name: vlan_30
        vlan_id: 30
        state: active
    state: merged

# Module Execution Results:
# -------------------------
#
# "after": [
#     {
#         "name": "Default",
#         "state": "active",
#         "vlan_id": 1
#     },
#     {
#         "name": "vlan_10",
#         "state": "active",
#         "vlan_id": 10
#     },
#     {
#         "name": "vlan_20",
#         "state": "active",
#         "vlan_id": 20
#     },
#     {
#         "name": "vlan_30",
#         "state": "active",
#         "vlan_id": 30
#     }
# ],
#
# "before": [
#     {
#         "name": "Default",
#         "state": "active",
#         "vlan_id": 1
#     }
# ],
#
# "requests": [
#     {
#        "data": {
#          "openconfig-vlan:vlan": [
#            {
#              "config": {
#                "name": "vlan_10",
#                "status": "ACTIVE",
#                "tpid": "oc-vlan-types:TPID_0x8100",
#                "vlan-id": 10
#             }
#            }
#          ]
#        },
#        "method": "POST",
#        "path": "/rest/restconf/data/openconfig-vlan:vlans/"
#      },
#      {
#        "data": {
#          "openconfig-vlan:vlan": [
#            {
#              "config": {
#                "name": "vlan_20",
#                "status": "ACTIVE",
#                "tpid": "oc-vlan-types:TPID_0x8100",
#                "vlan-id": 20
#              }
#            }
#          ]
#        },
#        "method": "POST",
#        "path": "/rest/restconf/data/openconfig-vlan:vlans/"
#      },
#        "data": {
#          "openconfig-vlan:vlan": [
#            {
#              "config": {
#                "name": "vlan_30",
#                "status": "ACTIVE",
#                "tpid": "oc-vlan-types:TPID_0x8100",
#                "vlan-id": 30
#              }
#            }
#          ]
#        },
#        "method": "POST",
#        "path": "/rest/restconf/data/openconfig-vlan:vlans/"
#      }
#    ]
#
#
# After state:
# -------------
#
# path: /rest/restconf/data/openconfig-vlan:vlans/
# method: GET
# data:
# {
#   "openconfig-vlan:vlans": {
#     "vlan": [
#       {
#         "config": {
#           "name": "Default",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 1
#         },
#       },
#       {
#         "config": {
#           "name": "vlan_10",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 10
#         },
#       },
#       {
#         "config": {
#           "name": "vlan_20",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 20
#         },
#       },
#       {
#         "config": {
#           "name": "vlan_30",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 30
#         },
#       }
#     ]
#   }
# }


# Using overridden

# Before state:
# -------------
#
# path: /rest/restconf/data/openconfig-vlan:vlans/
# method: GET
# data:
# {
#   "openconfig-vlan:vlans": {
#     "vlan": [
#       {
#         "config": {
#           "name": "Default",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 1
#         },
#       },
#       {
#         "config": {
#           "name": "vlan_10",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 10
#         },
#       },
#       {
#         "config": {
#           "name": "vlan_20",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 20
#         },
#       },
#       {
#         "config": {
#           "name": "vlan_30",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 30
#         },
#       }
#     ]
#   }
# }

- name: Override device configuration of all VLANs with provided configuration
  exos_vlans:
    config:
      - name: TEST_VLAN10
        vlan_id: 10
    state: overridden

# Module Execution Results:
# -------------------------
#
# "after": [
#     {
#         "name": "Default",
#         "state": "active",
#         "vlan_id": 1
#     },
#     {
#         "name": "TEST_VLAN10",
#         "state": "active",
#         "vlan_id": 10
#     },
# ],
#
# "before": [
#     {
#         "name": "Default",
#         "state": "active",
#         "vlan_id": 1
#     },
#     {
#         "name": "vlan_10",
#         "state": "active",
#         "vlan_id": 10
#     },
#     {
#         "name": "vlan_20",
#         "state": "active",
#         "vlan_id": 20
#     },
#     {
#         "name": "vlan_30",
#         "state": "active",
#         "vlan_id": 30
#     }
# ],
#
# "requests": [
#     {
#        "data": {
#          "openconfig-vlan:vlan": {
#	     "vlan": [
#              {
#                "config": {
#                  "name": "TEST_VLAN10",
#                  "status": "ACTIVE",
#                  "tpid": "oc-vlan-types:TPID_0x8100",
#                  "vlan-id": 10
#                }
#              }
#            ]
#          }
#        }
#     },
#        "method": "PATCH",
#        "path": "/rest/restconf/data/openconfig-vlan:vlans/"
#     },
#     {
#	 "data": null,
#        "method": "DELETE",
#        "path": "/rest/restconf/data/openconfig-vlan:vlans/vlan=20"
#     },
#     {
#	 "data": null,
#        "method": "DELETE",
#        "path": "/rest/restconf/data/openconfig-vlan:vlans/vlan=30"
#     }
#  ]
#
#
# After state:
# -------------
#
# path: /rest/restconf/data/openconfig-vlan:vlans/
# method: GET
# data:
# {
#   "openconfig-vlan:vlans": {
#     "vlan": [
#       {
#         "config": {
#           "name": "Default",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 1
#         },
#       },
#       {
#         "config": {
#           "name": "TEST_VLAN10",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 10
#         },
#       }
#     ]
#   }
# }


# Using replaced

# Before state:
# -------------
#
# path: /rest/restconf/data/openconfig-vlan:vlans/
# method: GET
# data:
# {
#   "openconfig-vlan:vlans": {
#     "vlan": [
#       {
#         "config": {
#           "name": "Default",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 1
#         },
#       },
#       {
#         "config": {
#           "name": "vlan_10",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 10
#         },
#       },
#       {
#         "config": {
#           "name": "vlan_20",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 20
#         },
#       },
#       {
#         "config": {
#           "name": "vlan_30",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 30
#         },
#       }
#     ]
#   }
# }

- name: Replaces device configuration of listed VLANs with provided configuration
  exos_vlans:
    config:
      - name: Test_VLAN20
        vlan_id: 20
      - name: Test_VLAN30
        vlan_id: 30
    state: replaced

# Module Execution Results:
# -------------------------
#
# "after": [
#     {
#         "name": "Default",
#         "state": "active",
#         "vlan_id": 1
#     },
#     {
#         "name": "vlan_10",
#         "state": "active",
#         "vlan_id": 10
#     },
#     {
#         "name": "TEST_VLAN20",
#         "state": "active",
#         "vlan_id": 20
#     },
#     {
#         "name": "TEST_VLAN30",
#         "state": "active",
#         "vlan_id": 30
#     }
# ],
#
# "before": [
#     {
#         "name": "Default",
#         "state": "active",
#         "vlan_id": 1
#     },
#     {
#         "name": "vlan_10",
#         "state": "active",
#         "vlan_id": 10
#     },
#     {
#         "name": "vlan_20",
#         "state": "active",
#         "vlan_id": 20
#     },
#     {
#         "name": "vlan_30",
#         "state": "active",
#         "vlan_id": 30
#     }
# ],
#
# "requests": [
#    {
#       "data": {
#          "openconfig-vlan:vlan": {
#             "vlan": [
#                 {
#                   "config": {
#                      "name": "TEST_VLAN20",
#                      "status": "ACTIVE",
#                      "tpid": "oc-vlan-types:TPID_0x8100",
#                      "vlan-id": 20
#                   }
#                   "config": {
#                      "name": "TEST_VLAN30",
#                      "status": "ACTIVE",
#                      "tpid": "oc-vlan-types:TPID_0x8100",
#                      "vlan-id": 30
#                   }
#                }
#             ]
#          },
#       "method": "PATCH",
#       "path": "/rest/restconf/data/openconfig-vlan:vlans/"
#    }
# ]
#
# After state:
# -------------
#
# path: /rest/restconf/data/openconfig-vlan:vlans/
# method: GET
# data:
# {
#   "openconfig-vlan:vlans": {
#     "vlan": [
#       {
#         "config": {
#           "name": "Default",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 1
#         },
#       },
#       {
#         "config": {
#           "name": "vlan_10",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 10
#         },
#       },
#       {
#         "config": {
#           "name": "TEST_VLAN20",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 20
#         },
#       },
#       {
#         "config": {
#           "name": "TEST_VLAN30",
#           "status": "ACTIVE",
#           "tpid": "oc-vlan-types:TPID_0x8100",
#           "vlan-id": 30
#         },
#       }
#     ]
#   }
# }


"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
  type: list
after:
  description: The resulting configuration model invocation.
  returned: when changed
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
  type: list
requests:
  description: The set of requests pushed to the remote device.
  returned: always
  type: list
  sample: [{"data": "...", "method": "...", "path": "..."}, {"data": "...", "method": "...", "path": "..."}, {"data": "...", "method": "...", "path": "..."}]
"""


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.network.exos.argspec.vlans.vlans import VlansArgs
from ansible_collections.misc.not_a_real_collection.plugins.module_utils.network.exos.config.vlans.vlans import Vlans


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    required_if = [('state', 'merged', ('config',)),
                   ('state', 'replaced', ('config',))]
    module = AnsibleModule(argument_spec=VlansArgs.argument_spec, required_if=required_if,
                           supports_check_mode=True)

    result = Vlans(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
