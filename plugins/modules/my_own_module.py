#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_test

short_description: This module creates file and fills it

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: This modele creates file in "path" and fills it with "content"

options:
    path:
        description: Path of the new file
        required: true
        type: str
    content:
        description:
            - Content to be placed into new file
            - If this is empty, new file will be empty
        required: false
        type: str
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
extends_documentation_fragment:
    - metsger.ansible_collection.my_test

author:
    - Fedor Metsger
'''

EXAMPLES = r'''
# Pass in a message
- name: Test with some content
  metsger.ansible_collection.my_test:
    path: /tmp/file
    content: "Some content"
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
path:
    description: The file path that was passed in.
    type: str
    returned: always
    sample: /tmp/file
message:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample: 'Created'
'''

from ansible.module_utils.basic import AnsibleModule


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=False, default=False)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        ok=False,
        failed=False,
        path="",
        message=""
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    try:
        with open(module.params['path'], "r") as f:
            cont = f.read()
        if cont == module.params['content']:
            result['ok'] = True
            result['message'] = 'Not changed'
            module.exit_json(**result)
    except FileNotFoundError:
        pass
    except Exception as e:
        result['message'] = 'Failed'
        module.fail_json(msg='Exception while opening a file: ' + str(e), **result)

    try:
        with open(module.params['path'], "w") as f:
            f.write(module.params['content'])
        result['message'] = 'Created'
        result['changed'] = True
    except Exception as e:
        result['message'] = 'Failed'
        result['failed'] = True
        module.fail_json(msg='Exception while creating a file: ' + str(e), **result)
        
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
