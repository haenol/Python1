# p.99 응용예제
"""
# 1. 점수 입력, 학점 출력
score = int(input('점수를 입력하세요 >>> '))
if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score <= 89:
    grade = 'B'
elif 70 <= score <= 79:
    grade = 'C'
elif 60 <= score <= 69:
    grade = 'D'
elif 0 <= score <= 59:
    grade = 'F'
print(f'점수는 {score}점이고, 학점은 {grade}학점입니다.')

# 2. 정수 입력, 3의 배수 여부 판별
num = int(input('정수를 입력하세요 >>> '))
if num % 3 == 0:
    print(f'{num}는 3의 배수입니다.')
else:
    print(f'{num}는 3의 배수가 아닙니다.')

# 3. 정수 3개 입력, 가장 큰 수 출력
num1 = int(input('정수1 입력 >>> '))
num2 = int(input('정수2 입력 >>> '))
num3 = int(input('정수3 입력 >>> '))
if num3 < num1 > num2:
    print(f'가장 큰 수는 {num1}입니다.')
elif num1 < num2 > num3:
    print(f'가장 큰 수는 {num2}입니다.')
else:
    print(f'가장 큰 수는 {num3}입니다.')
# 방법2. if문을 이용해 차례대로 비교
# 방법3. 삼항 연산자를 이용해 차례대로 비교하는 방법
# result = num1 if num1 > num2 else num2
# result = num3 if num3 > result else result
# print(f'가장 큰 수는 {result}입니다.')
"""

# 4. 차량2부제. 차량번호 입력, 끝자리 짝->'운행가능', 홀->'운행불가'
carN = input('차량번호를 입력하세요 >>> ')
if (int(carN[-1]) % 2) == 0:
    message = '운행가능'
else:
    message = '운행불가'
print(f'차량번호 \'{carN}\'는 오늘 {message}입니다. ')
