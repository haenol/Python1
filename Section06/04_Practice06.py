# (0331_7일차_시작) p.111 응용예제
"""
# 1. 정수 입력. 그 횟수만큼 'Hello' 출력
num = int(input('정수를 입력하세요 >>> '))
i = 1
if num >= 1:
    while i <= num:
        print(f'{i}번째 Hello')
        i += 1
else:
    print('잘못된 입력입니다.')

# 2. 1부터 100 사이의 정수 중 7의 배수만 출력
i = 1
while i <= 100:
    if i % 7 == 0:
        print(i)
    i += 1
# 조건식에서 or 사용시 앞의 조건식이 참이면 뒤의 조건식 계산X ... 경우에 따라 elif도 방법

# 3. 커피1잔=300원. 돈 입력. 구매 가능한 잔 개수, 잔돈 출력
money = int(input('자판기에 얼마를 넣을까요? (300원이상) >>> '))
cup = 1
while cup <= (money // 300):
    print(f'커피 {cup}잔, 잔돈 {money - (300 * cup)}원')
    cup += 1

# 4. 0-9 정수 중복값 없이 5개까지 입력.
limit5 = set()
while len(limit5) < 5:
    n = int(input('0~9 사이 정수를 입력하세요 >>> '))
    if 0 <= n <= 9:
        limit5.add(n)
print('모두 입력되었습니다.')
print(f'입력된 값은 {limit5}입니다.')
# 0~9 사이 제한을 두는 걸 까먹음.

# 5. 1부터 100 사이의 모든 정수를 한 줄에 10개씩 출력
i = 1
while i <= 100:
    print(i, end='\t')  # @@@@@ print() 함수의 end 속성 이용!!!! 기본값인 줄바꿈을 변경
    i += 1
    if i % 10 == 1:          # 10으로 나눴을 때 나머지가 1인 경우, 줄바꿈
        print('\n')
"""

# 6. 전체 구구단을 예시처럼 출력 (단 이름은 그냥 새로 만들어봄)
j = 1
dan = 2
while dan <= 9:     # 단 이름 만들기.
    print(f'-{dan}단-', end='\t')
    dan += 1
print()

while j <= 9:
    dan = 2
    while dan <= 9:
        print(f'{dan}X{j}={dan*j}', end='\t')
        dan += 1
    print()     # 단순 print()는 줄바꿈 하나, print('\n')는 줄바꿈 두 번.
    j += 1


