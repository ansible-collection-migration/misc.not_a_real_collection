#!/usr/bin/python
#
# @author: Gaurav Rastogi (grastogi@avinetworks.com)
#          Eric Anderson (eanderson@avinetworks.com)
# module_check: supported
# Avi Version: 17.1.1
#
# Copyright: (c) 2017 Gaurav Rastogi, <grastogi@avinetworks.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_cloudconnectoruser
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>

short_description: Module for setup of CloudConnectorUser Avi RESTful Object
description:
    - This module is used to configure CloudConnectorUser object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent", "present"]
    avi_api_update_method:
        description:
            - Default method for object update is HTTP PUT.
            - Setting to patch will override that behavior to use HTTP PATCH.
        default: put
        choices: ["put", "patch"]
    avi_api_patch_op:
        description:
            - Patch operation to use when using avi_api_update_method as patch.
        choices: ["add", "replace", "delete"]
    azure_serviceprincipal:
        description:
            - Field introduced in 17.2.1.
    azure_userpass:
        description:
            - Field introduced in 17.2.1.
    gcp_credentials:
        description:
            - Credentials for google cloud platform.
            - Field introduced in 18.2.1.
    name:
        description:
            - Name of the object.
        required: true
    oci_credentials:
        description:
            - Credentials for oracle cloud infrastructure.
            - Field introduced in 18.2.1,18.1.3.
    private_key:
        description:
            - Private_key of cloudconnectoruser.
    public_key:
        description:
            - Public_key of cloudconnectoruser.
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
    tencent_credentials:
        description:
            - Credentials for tencent cloud.
            - Field introduced in 18.2.3.
    url:
        description:
            - Avi controller URL of the object.
    uuid:
        description:
            - Unique object identifier of the object.

extends_documentation_fragment:
- misc.not_a_real_collection.avi
'''

EXAMPLES = """
  - name: Create a Cloud connector user that is used for integration into cloud platforms
    avi_cloudconnectoruser:
      controller: '{{ controller }}'
      name: root
      password: '{{ password }}'
      private_key: |
        -----BEGIN RSA PRIVATE KEY-----
        -----END RSA PRIVATE KEY-----'
      public_key: 'ssh-rsa ...'
      tenant_ref: admin
      username: '{{ username }}'
"""

RETURN = '''
obj:
    description: CloudConnectorUser (api/cloudconnectoruser) object
    returned: success, changed
    type: dict
'''

from ansible.module_utils.basic import AnsibleModule
try:
    from ansible_collections.misc.not_a_real_collection.plugins.module_utils.network.avi.avi import (
        avi_common_argument_spec, avi_ansible_api, HAS_AVI)
except ImportError:
    HAS_AVI = False


def main():
    argument_specs = dict(
        state=dict(default='present',
                   choices=['absent', 'present']),
        avi_api_update_method=dict(default='put',
                                   choices=['put', 'patch']),
        avi_api_patch_op=dict(choices=['add', 'replace', 'delete']),
        azure_serviceprincipal=dict(type='dict',),
        azure_userpass=dict(type='dict',),
        gcp_credentials=dict(type='dict',),
        name=dict(type='str', required=True),
        oci_credentials=dict(type='dict',),
        private_key=dict(type='str', no_log=True,),
        public_key=dict(type='str',),
        tenant_ref=dict(type='str',),
        tencent_credentials=dict(type='dict',),
        url=dict(type='str',),
        uuid=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    return avi_ansible_api(module, 'cloudconnectoruser',
                           set(['private_key']))


if __name__ == '__main__':
    main()
