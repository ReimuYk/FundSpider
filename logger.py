import utils
import time

def getTimeStr():
    now = int(time.time())
    timeArray = time.localtime(now)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime

class Logger:
    def  __init__(self, log_file, fund_list):
        self.log_file = log_file
        self.fund_list = fund_list
        print("[INFO] Logger Init Success")
    def log_block(self):
        # generate datas
        funddata_list = []
        for fund_id in self.fund_list:
            data = utils.pipeline(fund_id)
            if data:
                funddata_list.append(data)
        # write log
        f = open(self.log_file, 'a')
        f.write(getTimeStr())
        f.write('\n')
        for j in funddata_list:
            f.write(j['fundcode'])
            f.write('\t')
            f.write(j['name'])
            f.write('\t')
            f.write(j['jzrq'])
            f.write('\t')
            f.write(j['dwjz'])
            f.write('\t')
            f.write(j['gztime'])
            f.write('\t')
            f.write(j['gsz'])
            f.write('\t')
            f.write(j['gszzl'])
            f.write('\n')
        f.write('\n\n')
        f.close()
    def run(self, at_time=[1900,1,1,15,30], gap=1800):
        while True:
            timearr = time.localtime(int(time.time()))
            if timearr.tm_year==at_time[0] and \
               timearr.tm_mon==at_time[1] and \
               timearr.tm_mday==at_time[2] and \
               timearr.tm_hour==at_time[3] and \
               timearr.tm_min==at_time[4]:
                break
            else:
                print("[INFO] wait started: %s" % getTimeStr())
                time.sleep(30)
        while True:
            print("[INFO] Log running: %s" % getTimeStr())
            self.log_block()
            time.sleep(gap)

# demo
# logger = Logger('./log.txt', ["005963"])
# logger.run("")

# logger.log_block()
# logger.log_block()