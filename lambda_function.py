import json
import requests
import os

username = os.environ['USERNAME']
access_token = os.environ['ACCESS_TOKEN']
def lambda_handler(event, context):
    url = 'https://api.meethue.com/route/api/' + username + '/lights/1/state'
    headers = {
        'Authorization':'Bearer ' + access_token,
        'Content-Type':'application/json'
    }
    payload = {'on':event['flg'] == "True"}
    response = requests.put(url=url, headers=headers, data = json.dumps(payload))
    return json.dumps(response,default=str)