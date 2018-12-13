#!/usr/bin/env python

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'python_task_helper', 'files'))
from task_helper import TaskHelper

import requests

class SplunkTask(TaskHelper):
    def task(self, args):
        # Bolt passes connection information to the task in the '_target' metaparameter
        # The name of the target in inventory will be passed as 'uri'
        splunk_endpoint = args['_target']['uri']
        # The token value from the remote config will also be included.
        splunk_token = args['_target']['token']
        data = args['data']

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Splunk ' + splunk_token
        }

        response = requests.post(
            splunk_endpoint, headers=headers, json=data, verify=False)

        # TODO: verify we get json back from splunk
        return response.text

if __name__ == '__main__':
    SplunkTask().run()
