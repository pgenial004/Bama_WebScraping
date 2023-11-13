import requests
import re
import random
import net
import json
import pandas as pd
from pandas import json_normalize
request = net.Net()

print("Each page contains information on 30 vehicles.")
pages = int(input("How many pages of information do you want to extract? "))
def random_us():
    IE_USER_AGENT = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
    FF_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
    OPERA_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 OPR/67.0.3575.97'
    IOS_USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Mobile/15E148 Safari/604.1'
    ANDROID_USER_AGENT = 'Mozilla/5.0 (Linux; Android 9; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36'
    EDGE_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'
    CHROME_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4136.7 Safari/537.36'
    SAFARI_USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15'
    _USER_AGENTS = [FF_USER_AGENT, OPERA_USER_AGENT, EDGE_USER_AGENT, CHROME_USER_AGENT, SAFARI_USER_AGENT]
    return (random.choice(_USER_AGENTS))

headers = {'Origin': 'https://www.accessengllc.com/projects-bidding','User-Agent': random_us()}
add = []
for page in range(1,pages+1):
    data = request.http_GET(f"https://bama.ir/api/car/search?pageIndex={page}", headers=headers).content
    for i in  json.loads(data)['data']['ads']:
        df = json_normalize(i['detail'])
        add.append(df)
    print(f"page {page} extracted.")
merged_df = pd.concat(add)
merged_df.to_excel("output.xlsx")
