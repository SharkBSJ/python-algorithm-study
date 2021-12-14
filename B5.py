# https://programmers.co.kr/learn/courses/30/lessons/17677
# 뉴스 클러스터링

from collections import Counter

def solution(str1, str2):
    answer = 0
    
    str1_arrs = []
    str2_arrs = []
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            str1_arrs.append(str1[i].lower() + str1[i + 1].lower())
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            str2_arrs.append(str2[i].lower() + str2[i + 1].lower())
    
    str1_counter = Counter(str1_arrs)
    str2_counter = Counter(str2_arrs)
    
    sum_count = 0
    intersect_count = 0
    for key in str1_counter:
            if key in str2_counter:
                intersect_count += min(str1_counter[key], str2_counter[key])
                sum_count += max(str1_counter[key], str2_counter[key])
            else:
                sum_count += str1_counter[key]
    for key in str2_counter:
        if key in str1_counter:
            continue
        sum_count += str2_counter[key]

    if sum_count == 0:
        return 65536
    # print(intersect_count, sum_count)
    answer = int(intersect_count / sum_count * 65536)
    return answer

str1 = 'E=M*C^2'
str2 = 'e=m*c^2'
print(solution(str1, str2))