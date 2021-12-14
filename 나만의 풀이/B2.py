# https://programmers.co.kr/learn/courses/30/lessons/17682
# 다트 게임

def solution(dartResult):
    answer = 0
    
    idx = 0
    prev = 0
    prev_option_star = False
    while idx < len(dartResult):
        temp = ''
        score = 0
        bonus = ''
        option = ''
        
        # Get Score and Bonus
        if dartResult[idx + 1] == '0':
            score = 10
            bonus = dartResult[idx + 2]
            idx += 3
        else:
            score = int(dartResult[idx])
            bonus = dartResult[idx + 1]
            idx += 2
        # Get Option 
        if idx < len(dartResult) and \
                (dartResult[idx] == '*' or dartResult[idx] == '#'):
            option = dartResult[idx]
            idx += 1  
        
        temp_score = 0
        if bonus == 'S':
            temp_score = score
        elif bonus == 'D':
            temp_score = score ** 2
        elif bonus == 'T':
            temp_score = score ** 3
        
        if option == '#':
            temp_score = -temp_score
        
        answer += temp_score
        if option == '*':
            if prev_option_star:
                answer += prev
            answer += prev
            answer += temp_score
            prev_option_star = True
        else:
            prev_option_star = False
            
        prev = temp_score
    return answer

dartResult = '1S*2T*3S'
print(solution(dartResult))