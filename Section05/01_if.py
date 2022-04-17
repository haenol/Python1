"""
< Section05 : 조건문 >
    목차
    01_if         (0325_5일차/완)
    02_else1      (0329_6일차)
    03_else2        (생략;걍 else 다른 예제)
    04_elif
    05_Practice05 (0329_6일차_continue)
"""
""" 알고 있으니까 설명 생략
    if 조건식 :
        실행할 코드1
        ...
"""
# 01_if
no = int(input('숫자 입력 : '))
if no > 0:
    print('입력하신 숫자는 양수입니다.')
# 생략

# 02_else
n = int(input('숫자를 입력하세요 : '))
if (n % 2) == 0:
    message = '짝수'
else:
    message = '홀수'
print(f'입력하신 숫자는 {message}입니다.')

# 04_elif (p.98_기본예제)
age = int(input('나이 입력: '))
if age >= 20:
    m = '성인'
elif age >= 17:
    m = '고등학생'
elif age >= 14:
    m = '중학생'
elif age >= 8:
    m = '초등학생'
else:
    m = '미취학 아동'
print(f'{m}입니다.')
# 코드는 위에서 아래로 차례대로 처리
# 이런 층이 져있는 범위에 조건식을 둘 땐, 아예 ~부터 ~까지로 범위를 두 개 두거나 차례대로 작성하기
