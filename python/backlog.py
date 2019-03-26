#coding:utf-8

import json
import requests

def generate_backlog_wiki_url(spaceid,wikiid,apikey):
    backlog_apiurl_prefix = 'https://' + spaceid + '.backlog.com/api/v2/wikis/'
    return backlog_apiurl_prefix + wikiid + '?apiKey=' + apikey

def get_backlog_wiki_content(backlog_url):
    response_json = requests.get(backlog_url)
    response = json.loads(response_json.text)
    return response['content']

def update_backlog_wiki(backlog_url,markdown_text):
    backlog_patch_header = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.patch(
        backlog_url,
        headers=backlog_patch_header,
        data={'content': markdown_text}
    )
    return response
