import time


def getMinIntFromList(l, isPositive=False):
    """
    :param l: List[int] -86400 - 86400
    :param isPositive: 是否要正数
    :return: 返回数组中的最小整数
    """
    max = 100000
    res = max
    for i in l:
        if i < res:
            if isPositive:
                if i > 0:
                    res = i
            else:
                res = i
    if res == max:
        return None
    else:
        return res


class TimedtaskPattern(object):
    def __init__(self, name, tasktimes, method):
        self.name = name
        self.tasktimes = tasktimes
        self.method = method
        self.defaultStartTime = "00:00:00"
        self.defaultSeconds = 0
        self.defaultMinutes = 0
        self.defaultHours = 0
        self.defaultDays = 0
        self.defaultWeeks = 0

    def get_name(self):
        return self.name

    def get_next_distance(self):
        taskTimestampList = []
        nowTimeStamp_1970 = (int(time.time()) + 28800) % 86400
        if isinstance(self.tasktimes, str):
            timeArray = time.strptime(self.tasktimes, "%H:%M:%S")
            taskTimeStamp_1970 = int(time.mktime(timeArray) + 2209017943)
            timeDistance = taskTimeStamp_1970 - nowTimeStamp_1970
            if timeDistance <= 0:
                timeDistance += 86400
            return timeDistance
        elif isinstance(self.tasktimes, tuple):
            for tasktime in self.tasktimes:
                timeArray = time.strptime(tasktime, "%H:%M:%S")
                taskTimeStamp_1970 = int(time.mktime(timeArray) + 2209017943)
                taskTimestampList.append(taskTimeStamp_1970 - nowTimeStamp_1970)
            timeDistance = getMinIntFromList(taskTimestampList, isPositive=True)
            if timeDistance:
                return timeDistance
            else:
                return getMinIntFromList(taskTimestampList) + 86400
        elif isinstance(self.tasktimes, dict):
            startTime = self.tasktimes.get("start", self.defaultStartTime)
            seconds = self.tasktimes.get("seconds", self.defaultSeconds)
            minutes = self.tasktimes.get("minutes", self.defaultMinutes)
            hours = self.tasktimes.get("hours", self.defaultHours)
            days = self.tasktimes.get("days", self.defaultDays)
            startTimeArray = time.strptime(startTime, "%H:%M:%S")
            startTimestamp_1970 = int(time.mktime(startTimeArray) + 2209017943)
            l = []
            t = startTimestamp_1970
            s = seconds + minutes*60 + hours*3600 + days*86400
            if s <= 0:
                raise ValueError
            while True:
                if t > 86400:
                    break
                if t != 0:
                    l.append(t)
                    taskTimestampList.append(t - nowTimeStamp_1970)
                t += s
            timeDistance = getMinIntFromList(taskTimestampList, isPositive=True)
            if timeDistance:
                return timeDistance
            else:
                return getMinIntFromList(taskTimestampList) + 86400
        else:
            raise TypeError


if __name__ == "__main__":
    # ttp = TimedtaskPattern("10:00:00", test)# 每天10点触发
    # ttp = TimedtaskPattern(("8:00:00", "12:00:00"), test)# 每天8点和12点触发
    # ttp = TimedtaskPattern({"seconds": 600}, test)# 每天00:10:00 00:20:00... 每过600秒触发一次
    # ttp = TimedtaskPattern({"start": "8:00:00", "seconds": 60, "minutes": 10}, test) #每天8:11:00 8:22:00...每过660秒触发一次
    # nextt = ttp.get_next_distance()
    # print(str(nextt))

    # if isinstance({"a": 100, "b": 200}, dict):
    #     print("yes")
    pass
