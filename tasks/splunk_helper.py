#!/usr/bin/env python

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'python_task_helper', 'files'))
from task_helper import TaskHelper

import requests

class SplunkTask(TaskHelper):
    def task(self, args):
        splunk_endpoint = args['splunk_endpoint']
        splunk_token = args['splunk_token']
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
