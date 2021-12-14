# https://programmers.co.kr/learn/courses/30/lessons/17678
# 셔틀버스

def solution(n, t, m, timetable):
    arrs = []
    for temp in timetable:
        arrs.append(int(temp[0:2]) * 60 + int(temp[3:5]))
    arrs.sort(reverse=True)
    
    bus_time = 9 * 60 - t
    last_arrs = []
    for i in range(n):
        bus_time += t
        
        last_arrs = []
        for _ in range(m):
            if arrs and arrs[-1] <= bus_time:
                last_arrs.append(arrs.pop())
    
    if len(last_arrs) < m:
        hour = f'{bus_time // 60}'.zfill(2)
        min = f'{bus_time % 60}'.zfill(2)
    else:
        last_arrs[-1] -= 1
        hour = f'{last_arrs[-1] // 60}'.zfill(2)
        min = f'{last_arrs[-1]  % 60}'.zfill(2)
        
    return f'{hour}:{min}'

n = 1
t = 1
m = 5
timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]
print(solution(n, t, m, timetable))