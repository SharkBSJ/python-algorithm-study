# https://programmers.co.kr/learn/courses/30/lessons/17680
# 캐시

class Cache:
    def __init__(self, cacheSize):
        self.cache = {}
        self.cahceSize = cacheSize
        
    def checkCache(self, s):
        return s in self.cache
    
    def insertCache(self, s, idx):
        min_key = ''
        size = 0
        
        for key in self.cache:
            size += 1
            if min_key == '' or self.cache[key] < self.cache[min_key]:
                min_key = key
        
        if min_key != '' and size >= self.cahceSize:
            self.cache.pop(min_key)
        if self.cahceSize != 0:
            self.cache[s] = idx
        
    def updateCache(self, s, idx):
        if s in self.cache:
            self.cache[s] = idx
        

def solution(cacheSize, cities):
    answer = 0
    cache = Cache(cacheSize)
    
    for idx in range(len(cities)):
        city = cities[idx].lower()
        if cache.checkCache(city):
            answer += 1
            cache.updateCache(city, idx)
        else:
            answer += 5
            cache.insertCache(city, idx)
    
    return answer

cacheSize = 0
cities = ["Jeju", "jeju", "jeju"]
print(solution(cacheSize, cities))