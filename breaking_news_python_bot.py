import urllib.request
import json
import pymsteams
import time
import yaml
import datetime

with open('settings.yaml') as f:
    yml = yaml.safe_load(f)
    webhook_url = yml['webhookUrl']
today_str = datetime.date.today().strftime('%Y-%m-%d')[:10]
yesterday_str = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')[:10]
url = "https://qiita.com/api/v2/items?per_page=100&query=tag:Python%20created:%3E=" + yesterday_str + "%20created:%3C" + today_str
res = urllib.request.urlopen(url)
entries = json.loads(res.read().decode('utf8'))
for entry in entries:
    message = pymsteams.connectorcard(webhook_url)
    message.title(entry['title'])
    message.text(entry['url'])
    message.send()
    time.sleep(1)