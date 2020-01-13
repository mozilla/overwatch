import os
import requests
import json


os.environ['config'] = f"{os.environ['variables_path']}overwatch_slack_env_variables.json"

config = os.environ['config']

with open(config, 'r') as file:
    variables = json.load(file)
    webhook_url = variables['webhook_url']


slack_data = {'text': "Sup! This is quite successful"}

# Docs for formatting messages can be found here: https://api.slack.com/docs/message-formatting#variables
# To notify channel: slack_data = {'text': "Sup! This is quite successful <!here> or <!channel>"}


response = requests.post(
    webhook_url, data=json.dumps(slack_data),
    headers={'Content-Type': 'application/json'}
)

if response.status_code != 200:
    raise ValueError(
        'Request to slack returned an error %s, the response is:\n%s'
        %(response.status_code, response.text)
    )