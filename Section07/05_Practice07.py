# (0405_8일차_시작) p.129 응용예제
"""
# 1. 1부터 5사이에 존재하는 모든 정수를 역순으로 출력하는 프로그램
for i in range(5, 0, -1):
    print(i)


# 2. 임의의 양의 정수 입력. 1부터 입력받은 정수까지 모든 정수의 합계 출력
no = int(input('임의의 양수를 입력하세요 >>> '))
Sum = 0
for i in range(1, no + 1):
    Sum += i
print(f'1부터 {no}까지 모든 정수의 합계는 {Sum}입니다.')


# 3. 양의 정수 입력. 그 숫자만큼 '과일 이름'을 입력받아 'basket'리스트에 저장
basket = []
n = int(input('몇 개의 과일을 보관할까요? >>> '))
for count in range(1, n+1):
    fruit = input(f'{count}번째 과일을 입력하세요 >>> ')
    basket.append(fruit)
    count += 1
print(f'입력받은 과일들은 {basket}입니다.')


# 4. 10명 학생의 국어 점수 번호순으로 나열.(exam) 100점 제외 나머지 점수를 5점씩 증가시킨 'score'리스트 출력. (100점 초과X)
exam = [99, 78, 100, 91, 81, 85, 54, 100, 71, 50]
score = []
for i in range(0, 10):
    plus = exam[i] + 5
    if plus >= 100:
        plus = 100
    score.append(plus)
print(score)
"""

# 5. 1~99 사이의 모든 정수로 369게임 결과 출력
print(1//10)
print(1%10)
for i in range(1, 100):
    if (i // 10) == (3 or 6 or 9):      # i//10(일의 자리)
        print('짝', end='\t')
    elif (i % 10) == (3 or 6 or 9):     # i%10(십의 자리)
        print('짝', end='\t')
    else:
        print(i, end='\t')
# 일의 자리가 369인 경우, 짝만 출력하고 조건문이 끝나는 문제
# 10의 배수마다 줄바꿈이 안되어 있는 문제

