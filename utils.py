import requests
import time, datetime
import random

def getFundData(fund_id):
    fund_id = str(fund_id)
    recent_time = time.time()*1000 - random.randint(1,500)
    recent_time = str(int(recent_time))
    url = "http://fundgz.1234567.com.cn/js/%s.js?rt=%s" % (fund_id, recent_time)
    return requests.get(url)

def decodeFundData(fund_data):
    data = fund_data.text
    if data[0:8] == 'jsonpgz(':
        return eval(data[8:-2])
    else:
        print("[ERROR] Not jsonpgz type")
        return None

def pipeline(fund_id):
    d = getFundData(fund_id)
    if d.status_code != 200:
        print("[ERROR] HTTP Response Error %d" % d.status_code)
        return None
    d = decodeFundData(d)
    if not d:
        return None
    return d

def printFundData(jsonfile):
    print("基金代码: %s" % jsonfile['fundcode'])
    print("基金名称: %s" % jsonfile['name'])
    print("截止日期: %s" % jsonfile['jzrq'])
    print("单位净值: %s" % jsonfile['dwjz'])
    print("估值时间: %s" % jsonfile['gztime'])
    print("估算值: %s" % jsonfile['gsz'])
    print("估算增值率: %s" % jsonfile['gszzl'])

# demo
printFundData(pipeline("005963"))
