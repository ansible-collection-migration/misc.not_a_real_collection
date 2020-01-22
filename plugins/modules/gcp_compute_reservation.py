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
module: gcp_compute_reservation
description:
- Represents a reservation resource. A reservation ensures that capacity is held in
  a specific zone even if the reserved VMs are not running.
- Reservations apply only to Compute Engine, Cloud Dataproc, and Google Kubernetes
  Engine VM usage.Reservations do not apply to `f1-micro` or `g1-small` machine types,
  preemptible VMs, sole tenant nodes, or other services not listed above like Cloud
  SQL and Dataflow.
short_description: Creates a GCP Reservation
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
  description:
    description:
    - An optional description of this resource.
    required: false
    type: str
  name:
    description:
    - Name of the resource. Provided by the client when the resource is created. The
      name must be 1-63 characters long, and comply with RFC1035. Specifically, the
      name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
      which means the first character must be a lowercase letter, and all following
      characters must be a dash, lowercase letter, or digit, except the last character,
      which cannot be a dash.
    required: true
    type: str
  specific_reservation_required:
    description:
    - When set to true, only VMs that target this reservation by name can consume
      this reservation. Otherwise, it can be consumed by VMs with affinity for any
      reservation. Defaults to false.
    required: false
    default: 'false'
    type: bool
  specific_reservation:
    description:
    - Reservation for instances with specific machine shapes.
    required: true
    type: dict
    suboptions:
      count:
        description:
        - The number of resources that are allocated.
        required: true
        type: int
      instance_properties:
        description:
        - The instance properties for the reservation.
        required: true
        type: dict
        suboptions:
          machine_type:
            description:
            - The name of the machine type to reserve.
            required: true
            type: str
          min_cpu_platform:
            description:
            - The minimum CPU platform for the reservation. For example, `"Intel Skylake"`.
              See U(https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform#availablezones)
              for information on available CPU platforms.
            required: false
            type: str
          guest_accelerators:
            description:
            - Guest accelerator type and count.
            required: false
            type: list
            suboptions:
              accelerator_type:
                description:
                - 'The full or partial URL of the accelerator type to attach to this
                  instance. For example: `projects/my-project/zones/us-central1-c/acceleratorTypes/nvidia-tesla-p100`
                  If you are creating an instance template, specify only the accelerator
                  name.'
                required: true
                type: str
              accelerator_count:
                description:
                - The number of the guest accelerator cards exposed to this instance.
                required: true
                type: int
          local_ssds:
            description:
            - The amount of local ssd to reserve with each instance. This reserves
              disks of type `local-ssd`.
            required: false
            type: list
            suboptions:
              interface:
                description:
                - The disk interface to use for attaching this disk, one of `SCSI`
                  or `NVME`. The default is `SCSI`.
                - 'Some valid choices include: "SCSI", "NVME"'
                required: false
                default: SCSI
                type: str
              disk_size_gb:
                description:
                - The size of the disk in base-2 GB.
                required: true
                type: int
  zone:
    description:
    - The zone where the reservation is made.
    required: true
    type: str
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
- 'API Reference: U(https://cloud.google.com/compute/docs/reference/rest/v1/reservations)'
- 'Reserving zonal resources: U(https://cloud.google.com/compute/docs/instances/reserving-zonal-resources)'
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
- name: create a reservation
  gcp_compute_reservation:
    name: test_object
    zone: us-central1-a
    specific_reservation:
      count: 1
      instance_properties:
        min_cpu_platform: Intel Cascade Lake
        machine_type: n2-standard-2
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
'''

RETURN = '''
creationTimestamp:
  description:
  - Creation timestamp in RFC3339 text format.
  returned: success
  type: str
description:
  description:
  - An optional description of this resource.
  returned: success
  type: str
id:
  description:
  - The unique identifier for the resource.
  returned: success
  type: int
name:
  description:
  - Name of the resource. Provided by the client when the resource is created. The
    name must be 1-63 characters long, and comply with RFC1035. Specifically, the
    name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
    which means the first character must be a lowercase letter, and all following
    characters must be a dash, lowercase letter, or digit, except the last character,
    which cannot be a dash.
  returned: success
  type: str
commitment:
  description:
  - Full or partial URL to a parent commitment. This field displays for reservations
    that are tied to a commitment.
  returned: success
  type: str
specificReservationRequired:
  description:
  - When set to true, only VMs that target this reservation by name can consume this
    reservation. Otherwise, it can be consumed by VMs with affinity for any reservation.
    Defaults to false.
  returned: success
  type: bool
status:
  description:
  - The status of the reservation.
  returned: success
  type: str
specificReservation:
  description:
  - Reservation for instances with specific machine shapes.
  returned: success
  type: complex
  contains:
    count:
      description:
      - The number of resources that are allocated.
      returned: success
      type: int
    inUseCount:
      description:
      - How many instances are in use.
      returned: success
      type: int
    instanceProperties:
      description:
      - The instance properties for the reservation.
      returned: success
      type: complex
      contains:
        machineType:
          description:
          - The name of the machine type to reserve.
          returned: success
          type: str
        minCpuPlatform:
          description:
          - The minimum CPU platform for the reservation. For example, `"Intel Skylake"`.
            See U(https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform#availablezones)
            for information on available CPU platforms.
          returned: success
          type: str
        guestAccelerators:
          description:
          - Guest accelerator type and count.
          returned: success
          type: complex
          contains:
            acceleratorType:
              description:
              - 'The full or partial URL of the accelerator type to attach to this
                instance. For example: `projects/my-project/zones/us-central1-c/acceleratorTypes/nvidia-tesla-p100`
                If you are creating an instance template, specify only the accelerator
                name.'
              returned: success
              type: str
            acceleratorCount:
              description:
              - The number of the guest accelerator cards exposed to this instance.
              returned: success
              type: int
        localSsds:
          description:
          - The amount of local ssd to reserve with each instance. This reserves disks
            of type `local-ssd`.
          returned: success
          type: complex
          contains:
            interface:
              description:
              - The disk interface to use for attaching this disk, one of `SCSI` or
                `NVME`. The default is `SCSI`.
              returned: success
              type: str
            diskSizeGb:
              description:
              - The size of the disk in base-2 GB.
              returned: success
              type: int
zone:
  description:
  - The zone where the reservation is made.
  returned: success
  type: str
'''

################################################################################
# Imports
################################################################################

from ansible_collections.misc.not_a_real_collection.plugins.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, remove_nones_from_dict, replace_resource_dict
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
            description=dict(type='str'),
            name=dict(required=True, type='str'),
            specific_reservation_required=dict(type='bool'),
            specific_reservation=dict(
                required=True,
                type='dict',
                options=dict(
                    count=dict(required=True, type='int'),
                    instance_properties=dict(
                        required=True,
                        type='dict',
                        options=dict(
                            machine_type=dict(required=True, type='str'),
                            min_cpu_platform=dict(type='str'),
                            guest_accelerators=dict(
                                type='list',
                                elements='dict',
                                options=dict(accelerator_type=dict(required=True, type='str'), accelerator_count=dict(required=True, type='int')),
                            ),
                            local_ssds=dict(
                                type='list',
                                elements='dict',
                                options=dict(interface=dict(default='SCSI', type='str'), disk_size_gb=dict(required=True, type='int')),
                            ),
                        ),
                    ),
                ),
            ),
            zone=dict(required=True, type='str'),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

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
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.post(link, resource_to_request(module)))


def update(module, link):
    delete(module, self_link(module))
    create(module, collection(module))


def delete(module, link):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'zone': module.params.get('zone'),
        u'description': module.params.get('description'),
        u'name': module.params.get('name'),
        u'specificReservationRequired': module.params.get('specific_reservation_required'),
        u'specificReservation': ReservationSpecificreservation(module.params.get('specific_reservation', {}), module).to_request(),
    }
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, allow_not_found=True):
    auth = GcpSession(module, 'compute')
    return return_if_object(module, auth.get(link), allow_not_found)


def self_link(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/zones/{zone}/reservations/{name}".format(**module.params)


def collection(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/zones/{zone}/reservations".format(**module.params)


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

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


def is_different(module, response):
    request = resource_to_request(module)
    response = response_to_hash(module, response)

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
        u'creationTimestamp': response.get(u'creationTimestamp'),
        u'description': response.get(u'description'),
        u'id': response.get(u'id'),
        u'name': response.get(u'name'),
        u'commitment': response.get(u'commitment'),
        u'specificReservationRequired': response.get(u'specificReservationRequired'),
        u'status': response.get(u'status'),
        u'specificReservation': ReservationSpecificreservation(response.get(u'specificReservation', {}), module).from_response(),
    }


def async_op_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    url = "https://www.googleapis.com/compute/v1/projects/{project}/zones/{zone}/operations/{op_id}"
    combined = extra_data.copy()
    combined.update(module.params)
    return url.format(**combined)


def wait_for_operation(module, response):
    op_result = return_if_object(module, response)
    if op_result is None:
        return {}
    status = navigate_hash(op_result, ['status'])
    wait_done = wait_for_completion(status, op_result, module)
    return fetch_resource(module, navigate_hash(wait_done, ['targetLink']))


def wait_for_completion(status, op_result, module):
    op_id = navigate_hash(op_result, ['name'])
    op_uri = async_op_url(module, {'op_id': op_id})
    while status != 'DONE':
        raise_if_errors(op_result, ['error', 'errors'], module)
        time.sleep(1.0)
        op_result = fetch_resource(module, op_uri, False)
        status = navigate_hash(op_result, ['status'])
    return op_result


def raise_if_errors(response, err_path, module):
    errors = navigate_hash(response, err_path)
    if errors is not None:
        module.fail_json(msg=errors)


class ReservationSpecificreservation(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict(
            {
                u'count': self.request.get('count'),
                u'instanceProperties': ReservationInstanceproperties(self.request.get('instance_properties', {}), self.module).to_request(),
            }
        )

    def from_response(self):
        return remove_nones_from_dict(
            {
                u'count': self.request.get(u'count'),
                u'instanceProperties': ReservationInstanceproperties(self.request.get(u'instanceProperties', {}), self.module).from_response(),
            }
        )


class ReservationInstanceproperties(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict(
            {
                u'machineType': self.request.get('machine_type'),
                u'minCpuPlatform': self.request.get('min_cpu_platform'),
                u'guestAccelerators': ReservationGuestacceleratorsArray(self.request.get('guest_accelerators', []), self.module).to_request(),
                u'localSsds': ReservationLocalssdsArray(self.request.get('local_ssds', []), self.module).to_request(),
            }
        )

    def from_response(self):
        return remove_nones_from_dict(
            {
                u'machineType': self.request.get(u'machineType'),
                u'minCpuPlatform': self.request.get(u'minCpuPlatform'),
                u'guestAccelerators': ReservationGuestacceleratorsArray(self.request.get(u'guestAccelerators', []), self.module).from_response(),
                u'localSsds': ReservationLocalssdsArray(self.request.get(u'localSsds', []), self.module).from_response(),
            }
        )


class ReservationGuestacceleratorsArray(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = []

    def to_request(self):
        items = []
        for item in self.request:
            items.append(self._request_for_item(item))
        return items

    def from_response(self):
        items = []
        for item in self.request:
            items.append(self._response_from_item(item))
        return items

    def _request_for_item(self, item):
        return remove_nones_from_dict({u'acceleratorType': item.get('accelerator_type'), u'acceleratorCount': item.get('accelerator_count')})

    def _response_from_item(self, item):
        return remove_nones_from_dict({u'acceleratorType': item.get(u'acceleratorType'), u'acceleratorCount': item.get(u'acceleratorCount')})


class ReservationLocalssdsArray(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = []

    def to_request(self):
        items = []
        for item in self.request:
            items.append(self._request_for_item(item))
        return items

    def from_response(self):
        items = []
        for item in self.request:
            items.append(self._response_from_item(item))
        return items

    def _request_for_item(self, item):
        return remove_nones_from_dict({u'interface': item.get('interface'), u'diskSizeGb': item.get('disk_size_gb')})

    def _response_from_item(self, item):
        return remove_nones_from_dict({u'interface': item.get(u'interface'), u'diskSizeGb': item.get(u'diskSizeGb')})


if __name__ == '__main__':
    main()
