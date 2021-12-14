# https://programmers.co.kr/learn/courses/30/lessons/17676
# 추석 트래픽

from typing import List
from datetime import datetime, timedelta

class Log:
    def __init__(self, start: datetime, end: datetime):
        self.start = start
        self.end = end

def solution(lines):
    answer: int = 0
    logs: List[Log] = []
    for line in lines:
        # year, month, day[, hour[, minute[, second[, microsecond
        time_delta = float(line[24:-1]) * 1000 - 1  
        end_datetime: datetime = datetime(year = int(line[0:4]), \
            month = int(line[5:7]), \
            day = int(line[8:10]), \
            hour = int(line[11:13]), \
            minute = int(line[14:16]), \
            second = int(line[17:19]), \
            microsecond = (int(line[20:23])) * 1000)
        logs.append(Log(end_datetime.__sub__(timedelta(milliseconds=time_delta)), end_datetime))
    
    # print(logs[0].start, logs[0].end)
    # print(logs[1].start, logs[1].end)
    for log in logs:
        temp_count: int = 0
        for temp in logs:
            #print('<==========================')
            #print(log.start, log.end, temp.start, temp.end)
            #print(log.start, temp.end, log.start.__add__(timedelta(seconds=1)), temp.start)
            if log.start <= temp.end and log.start.__add__(timedelta(seconds=0.999)) >= temp.start:
                temp_count += 1
        if temp_count > answer:
            answer = temp_count
    
    for log in logs:
        temp_count: int = 0
        for temp in logs:
            if log.end <= temp.end and log.end.__add__(timedelta(seconds=0.999)) >= temp.start:
                temp_count += 1
        if temp_count > answer:
            answer = temp_count
                
    return answer

lines = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]
print(solution(lines))