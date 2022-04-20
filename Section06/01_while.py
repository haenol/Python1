"""
< Section06 : 반복문 while >
    목차
    01_while          (0329_6일차_continue)
    02_Ex06_2               (기본 예제)
    03_while_in_while       (구구단 예제)
    04_Practice06     (0331_7일차)
"""
# 01_while
# 파이썬은 초기값, 조건식, 증감 한 줄로 못 씀.
# 선검사 후처리 방식
i = 0           # 초기값
while i < 5:    # 조건식
    print('Hellow World')
    i += 1      # 증감식

# 02_Ex06_2
my_list = []
n = int(input('정수 입력(종료는 0입니다) >>> '))
while n != 0:
    my_list.append(n)
    n = int(input('정수 입력(종료는 0입니다) >>> '))
print(my_list)

# 03_while_in_while (0329_6일차/완)
# 구구단 출력 예제
# 2단만 출력
# dan = 2
# i = 1
# while i < 10:
#     print(f'{dan} * {i} = {dan*i}')
#     i += 1
# 2~9단 출력
dan = 2
while dan < 10:
    i = 1
    while i < 10:
        print(f'{dan} * {i} = {dan*i}')
        i += 1
    dan += 1



