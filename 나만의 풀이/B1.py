# https://programmers.co.kr/learn/courses/30/lessons/17681?language=python3
# 비밀 지도

def solution(n, arr1, arr2):
    temp_answer = [arr1[i] | arr2[i] for i in range(n)]
    answer = []
    
    for i in range(n):
        temp = ''
        for j in range(n - 1, -1, -1):
            if temp_answer[i] & 2 ** j:
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)
        
    return answer

n = 5
arr1 =[9,20,28,18,11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))