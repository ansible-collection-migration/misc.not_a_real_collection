#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Google
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    AUTO GENERATED CODE     ***
#
# ----------------------------------------------------------------------------
#
#     This file is automatically generated by Magic Modules and manual
#     changes will be clobbered when the file is regenerated.
#
#     Please read more about how to change this file at
#     https://www.github.com/GoogleCloudPlatform/magic-modules
#
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function

__metaclass__ = type

################################################################################
# Documentation
################################################################################

ANSIBLE_METADATA = {'metadata_version': '1.1', 'status': ["preview"], 'supported_by': 'community'}

DOCUMENTATION = '''
---
module: gcp_spanner_instance
description:
- An isolated set of Cloud Spanner resources on which databases can be hosted.
short_description: Creates a GCP Instance
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  state:
    description:
    - Whether the given object should exist in GCP
    choices:
    - present
    - absent
    default: present
    type: str
  name:
    description:
    - A unique identifier for the instance, which cannot be changed after the instance
      is created. The name must be between 6 and 30 characters in length.
    required: true
    type: str
  config:
    description:
    - The name of the instance's configuration (similar but not quite the same as
      a region) which defines defines the geographic placement and replication of
      your databases in this instance. It determines where your data is stored. Values
      are typically of the form `regional-europe-west1` , `us-central` etc.
    - In order to obtain a valid list please consult the [Configuration section of
      the docs](U(https://cloud.google.com/spanner/docs/instances)).
    required: true
    type: str
  display_name:
    description:
    - The descriptive name for this instance as it appears in UIs. Must be unique
      per project and between 4 and 30 characters in length.
    required: true
    type: str
  node_count:
    description:
    - The number of nodes allocated to this instance.
    required: false
    default: '1'
    type: int
  labels:
    description:
    - 'An object containing a list of "key": value pairs.'
    - 'Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.'
    required: false
    type: dict
  project:
    description:
    - The Google Cloud Platform project to use.
    type: str
  auth_kind:
    description:
    - The type of credential used.
    type: str
    required: true
    choices:
    - application
    - machineaccount
    - serviceaccount
  service_account_contents:
    description:
    - The contents of a Service Account JSON file, either in a dictionary or as a
      JSON string that represents it.
    type: jsonarg
  service_account_file:
    description:
    - The path of a Service Account JSON file if serviceaccount is selected as type.
    type: path
  service_account_email:
    description:
    - An optional service account email address if machineaccount is selected and
      the user does not wish to use the default email.
    type: str
  scopes:
    description:
    - Array of scopes to be used
    type: list
  env_type:
    description:
    - Specifies which Ansible environment you're running this module within.
    - This should not be set unless you know what you're doing.
    - This only alters the User Agent string for any API requests.
    type: str
notes:
- 'API Reference: U(https://cloud.google.com/spanner/docs/reference/rest/v1/projects.instances)'
- 'Official Documentation: U(https://cloud.google.com/spanner/)'
- for authentication, you can set service_account_file using the C(gcp_service_account_file)
  env variable.
- for authentication, you can set service_account_contents using the C(GCP_SERVICE_ACCOUNT_CONTENTS)
  env variable.
- For authentication, you can set service_account_email using the C(GCP_SERVICE_ACCOUNT_EMAIL)
  env variable.
- For authentication, you can set auth_kind using the C(GCP_AUTH_KIND) env variable.
- For authentication, you can set scopes using the C(GCP_SCOPES) env variable.
- Environment variables values will only be used if the playbook values are not set.
- The I(service_account_email) and I(service_account_file) options are mutually exclusive.
'''

EXAMPLES = '''
- name: create a instance
  gcp_spanner_instance:
    name: testinstance
    display_name: My Spanner Instance
    node_count: 2
    labels:
      cost_center: ti-1700004
    config: regional-us-central1
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
'''

RETURN = '''
name:
  description:
  - A unique identifier for the instance, which cannot be changed after the instance
    is created. The name must be between 6 and 30 characters in length.
  returned: success
  type: str
config:
  description:
  - The name of the instance's configuration (similar but not quite the same as a
    region) which defines defines the geographic placement and replication of your
    databases in this instance. It determines where your data is stored. Values are
    typically of the form `regional-europe-west1` , `us-central` etc.
  - In order to obtain a valid list please consult the [Configuration section of the
    docs](U(https://cloud.google.com/spanner/docs/instances)).
  returned: success
  type: str
displayName:
  description:
  - The descriptive name for this instance as it appears in UIs. Must be unique per
    project and between 4 and 30 characters in length.
  returned: success
  type: str
nodeCount:
  description:
  - The number of nodes allocated to this instance.
  returned: success
  type: int
labels:
  description:
  - 'An object containing a list of "key": value pairs.'
  - 'Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.'
  returned: success
  type: dict
'''

################################################################################
# Imports
################################################################################

from ansible_collections.misc.not_a_real_collection.plugins.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, replace_resource_dict
import json
import time

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            name=dict(required=True, type='str'),
            config=dict(required=True, type='str'),
            display_name=dict(required=True, type='str'),
            node_count=dict(default=1, type='int'),
            labels=dict(type='dict'),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/spanner.admin']

    state = module.params['state']

    fetch = fetch_resource(module, self_link(module))
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module))
                fetch = fetch_resource(module, self_link(module))
                changed = True
        else:
            delete(module, self_link(module))
            fetch = {}
            changed = True
    else:
        if state == 'present':
            fetch = create(module, collection(module))
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link):
    auth = GcpSession(module, 'spanner')
    return wait_for_operation(module, auth.post(link, resource_to_create(module)))


def update(module, link):
    module.fail_json(msg="Spanner objects can't be updated to ensure data safety")


def delete(module, link):
    auth = GcpSession(module, 'spanner')
    return return_if_object(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'name': module.params.get('name'),
        u'config': module.params.get('config'),
        u'displayName': module.params.get('display_name'),
        u'nodeCount': module.params.get('node_count'),
        u'labels': module.params.get('labels'),
    }
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, allow_not_found=True):
    auth = GcpSession(module, 'spanner')
    return return_if_object(module, auth.get(link), allow_not_found)


def self_link(module):
    return "https://spanner.googleapis.com/v1/projects/{project}/instances/{name}".format(**module.params)


def collection(module):
    return "https://spanner.googleapis.com/v1/projects/{project}/instances".format(**module.params)


def return_if_object(module, response, allow_not_found=False):
    # If not found, return nothing.
    if allow_not_found and response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError):
        module.fail_json(msg="Invalid JSON response with error: %s" % response.text)

    result = decode_response(result, module)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


def is_different(module, response):
    request = resource_to_request(module)
    response = response_to_hash(module, response)
    request = decode_response(request, module)

    # Remove all output-only from response.
    response_vals = {}
    for k, v in response.items():
        if k in request:
            response_vals[k] = v

    request_vals = {}
    for k, v in request.items():
        if k in response:
            request_vals[k] = v

    return GcpRequest(request_vals) != GcpRequest(response_vals)


# Remove unnecessary properties from the response.
# This is for doing comparisons with Ansible's current parameters.
def response_to_hash(module, response):
    return {
        u'name': module.params.get('name'),
        u'config': response.get(u'config'),
        u'displayName': response.get(u'displayName'),
        u'nodeCount': response.get(u'nodeCount'),
        u'labels': response.get(u'labels'),
    }


def async_op_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    url = "https://spanner.googleapis.com/v1/{op_id}"
    combined = extra_data.copy()
    combined.update(module.params)
    return url.format(**combined)


def wait_for_operation(module, response):
    op_result = return_if_object(module, response)
    if op_result is None:
        return {}
    status = navigate_hash(op_result, ['done'])
    wait_done = wait_for_completion(status, op_result, module)
    raise_if_errors(wait_done, ['error'], module)
    return navigate_hash(wait_done, ['response'])


def wait_for_completion(status, op_result, module):
    op_id = navigate_hash(op_result, ['name'])
    op_uri = async_op_url(module, {'op_id': op_id})
    while not status:
        raise_if_errors(op_result, ['error'], module)
        time.sleep(1.0)
        op_result = fetch_resource(module, op_uri, False)
        status = navigate_hash(op_result, ['done'])
    return op_result


def raise_if_errors(response, err_path, module):
    errors = navigate_hash(response, err_path)
    if errors is not None:
        module.fail_json(msg=errors)


def resource_to_create(module):
    instance = resource_to_request(module)
    instance['name'] = "projects/{0}/instances/{1}".format(module.params['project'], module.params['name'])
    instance['config'] = "projects/{0}/instanceConfigs/{1}".format(module.params['project'], instance['config'])
    return {'instanceId': module.params['name'], 'instance': instance}


def resource_to_update(module):
    instance = resource_to_request(module)
    instance['name'] = "projects/{0}/instances/{1}".format(module.params['project'], module.params['name'])
    instance['config'] = "projects/{0}/instanceConfigs/{1}".format(module.params['project'], instance['config'])
    return {'instance': instance, 'fieldMask': "'name' ,'config' ,'displayName' ,'nodeCount' ,'labels'"}


def decode_response(response, module):
    if not response:
        return response

    if '/operations/' in response['name']:
        return response

    response['name'] = response['name'].split('/')[-1]
    response['config'] = response['config'].split('/')[-1]
    return response


if __name__ == '__main__':
    main()
