# Copyright: (c) 2019, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

import json

import pytest

from ansible_collections.misc.not_a_real_collection.plugins.modules import terraform
from ansible_collections.misc.not_a_real_collection.tests.unit.modules.utils import set_module_args


def test_terraform_without_argument(capfd):
    set_module_args({})
    with pytest.raises(SystemExit) as results:
        terraform.main()

    out, err = capfd.readouterr()
    assert not err
    assert json.loads(out)['failed']
    assert 'project_path' in json.loads(out)['msg']
