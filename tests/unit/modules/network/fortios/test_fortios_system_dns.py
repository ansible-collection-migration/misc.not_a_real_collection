# Copyright 2019 Fortinet, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <https://www.gnu.org/licenses/>.

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os
import json
import pytest
from mock import ANY
from ansible_collections.misc.not_a_real_collection.plugins.module_utils.network.fortios.fortios import FortiOSHandler

try:
    from ansible_collections.misc.not_a_real_collection.plugins.modules import fortios_system_dns
except ImportError:
    pytest.skip("Could not load required modules for testing", allow_module_level=True)


@pytest.fixture(autouse=True)
def connection_mock(mocker):
    connection_class_mock = mocker.patch('ansible_collections.misc.not_a_real_collection.plugins.modules.fortios_system_dns.Connection')
    return connection_class_mock


fos_instance = FortiOSHandler(connection_mock)


def test_system_dns_creation(mocker):
    schema_method_mock = mocker.patch('ansible_collections.misc.not_a_real_collection.plugins.module_utils.network.fortios.fortios.FortiOSHandler.schema')

    set_method_result = {'status': 'success', 'http_method': 'POST', 'http_status': 200}
    set_method_mock = mocker.patch('ansible_collections.misc.not_a_real_collection.plugins.module_utils.network.fortios.fortios.FortiOSHandler.set', return_value=set_method_result)

    input_data = {
        'username': 'admin',
        'state': 'present',
        'system_dns': {
            'cache_notfound_responses': 'disable',
            'dns_cache_limit': '4',
            'dns_cache_ttl': '5',
            'ip6_primary': 'test_value_6',
            'ip6_secondary': 'test_value_7',
            'primary': 'test_value_8',
            'retry': '9',
            'secondary': 'test_value_10',
            'source_ip': '84.230.14.11',
            'timeout': '12'
        },
        'vdom': 'root'}

    is_error, changed, response = fortios_system_dns.fortios_system(input_data, fos_instance)

    expected_data = {
        'cache-notfound-responses': 'disable',
        'dns-cache-limit': '4',
        'dns-cache-ttl': '5',
        'ip6-primary': 'test_value_6',
        'ip6-secondary': 'test_value_7',
        'primary': 'test_value_8',
        'retry': '9',
        'secondary': 'test_value_10',
        'source-ip': '84.230.14.11',
        'timeout': '12'
    }

    set_method_mock.assert_called_with('system', 'dns', data=expected_data, vdom='root')
    schema_method_mock.assert_not_called()
    assert not is_error
    assert changed
    assert response['status'] == 'success'
    assert response['http_status'] == 200


def test_system_dns_creation_fails(mocker):
    schema_method_mock = mocker.patch('ansible_collections.misc.not_a_real_collection.plugins.module_utils.network.fortios.fortios.FortiOSHandler.schema')

    set_method_result = {'status': 'error', 'http_method': 'POST', 'http_status': 500}
    set_method_mock = mocker.patch('ansible_collections.misc.not_a_real_collection.plugins.module_utils.network.fortios.fortios.FortiOSHandler.set', return_value=set_method_result)

    input_data = {
        'username': 'admin',
        'state': 'present',
        'system_dns': {
            'cache_notfound_responses': 'disable',
            'dns_cache_limit': '4',
            'dns_cache_ttl': '5',
            'ip6_primary': 'test_value_6',
            'ip6_secondary': 'test_value_7',
            'primary': 'test_value_8',
            'retry': '9',
            'secondary': 'test_value_10',
            'source_ip': '84.230.14.11',
            'timeout': '12'
        },
        'vdom': 'root'}

    is_error, changed, response = fortios_system_dns.fortios_system(input_data, fos_instance)

    expected_data = {
        'cache-notfound-responses': 'disable',
        'dns-cache-limit': '4',
        'dns-cache-ttl': '5',
        'ip6-primary': 'test_value_6',
        'ip6-secondary': 'test_value_7',
        'primary': 'test_value_8',
        'retry': '9',
        'secondary': 'test_value_10',
        'source-ip': '84.230.14.11',
        'timeout': '12'
    }

    set_method_mock.assert_called_with('system', 'dns', data=expected_data, vdom='root')
    schema_method_mock.assert_not_called()
    assert is_error
    assert not changed
    assert response['status'] == 'error'
    assert response['http_status'] == 500


def test_system_dns_idempotent(mocker):
    schema_method_mock = mocker.patch('ansible_collections.misc.not_a_real_collection.plugins.module_utils.network.fortios.fortios.FortiOSHandler.schema')

    set_method_result = {'status': 'error', 'http_method': 'DELETE', 'http_status': 404}
    set_method_mock = mocker.patch('ansible_collections.misc.not_a_real_collection.plugins.module_utils.network.fortios.fortios.FortiOSHandler.set', return_value=set_method_result)

    input_data = {
        'username': 'admin',
        'state': 'present',
        'system_dns': {
            'cache_notfound_responses': 'disable',
            'dns_cache_limit': '4',
            'dns_cache_ttl': '5',
            'ip6_primary': 'test_value_6',
            'ip6_secondary': 'test_value_7',
            'primary': 'test_value_8',
            'retry': '9',
            'secondary': 'test_value_10',
            'source_ip': '84.230.14.11',
            'timeout': '12'
        },
        'vdom': 'root'}

    is_error, changed, response = fortios_system_dns.fortios_system(input_data, fos_instance)

    expected_data = {
        'cache-notfound-responses': 'disable',
        'dns-cache-limit': '4',
        'dns-cache-ttl': '5',
        'ip6-primary': 'test_value_6',
        'ip6-secondary': 'test_value_7',
        'primary': 'test_value_8',
        'retry': '9',
        'secondary': 'test_value_10',
        'source-ip': '84.230.14.11',
        'timeout': '12'
    }

    set_method_mock.assert_called_with('system', 'dns', data=expected_data, vdom='root')
    schema_method_mock.assert_not_called()
    assert not is_error
    assert not changed
    assert response['status'] == 'error'
    assert response['http_status'] == 404


def test_system_dns_filter_foreign_attributes(mocker):
    schema_method_mock = mocker.patch('ansible_collections.misc.not_a_real_collection.plugins.module_utils.network.fortios.fortios.FortiOSHandler.schema')

    set_method_result = {'status': 'success', 'http_method': 'POST', 'http_status': 200}
    set_method_mock = mocker.patch('ansible_collections.misc.not_a_real_collection.plugins.module_utils.network.fortios.fortios.FortiOSHandler.set', return_value=set_method_result)

    input_data = {
        'username': 'admin',
        'state': 'present',
        'system_dns': {
            'random_attribute_not_valid': 'tag',
            'cache_notfound_responses': 'disable',
            'dns_cache_limit': '4',
            'dns_cache_ttl': '5',
            'ip6_primary': 'test_value_6',
            'ip6_secondary': 'test_value_7',
            'primary': 'test_value_8',
            'retry': '9',
            'secondary': 'test_value_10',
            'source_ip': '84.230.14.11',
            'timeout': '12'
        },
        'vdom': 'root'}

    is_error, changed, response = fortios_system_dns.fortios_system(input_data, fos_instance)

    expected_data = {
        'cache-notfound-responses': 'disable',
        'dns-cache-limit': '4',
        'dns-cache-ttl': '5',
        'ip6-primary': 'test_value_6',
        'ip6-secondary': 'test_value_7',
        'primary': 'test_value_8',
        'retry': '9',
        'secondary': 'test_value_10',
        'source-ip': '84.230.14.11',
        'timeout': '12'
    }

    set_method_mock.assert_called_with('system', 'dns', data=expected_data, vdom='root')
    schema_method_mock.assert_not_called()
    assert not is_error
    assert changed
    assert response['status'] == 'success'
    assert response['http_status'] == 200
