"""
< Section07 : 반복문 for >
    목차
    01_for_ex_1         (0331_7일차_continue)
    02_Ex07_1               (기본 예제)
    03_for_ex_2             (for문 이론설명, ft.range)
    04_Ex07_2           (0331_7일차/완)
    05_Practice07
"""
# 01_for_ex_1 (0331_7일차_continue)
# for문은 연속된 데이터가 필요할 때 사용하기 때문에 조건식X. 다른 언어에선 쓰긴함.
for n in [1, 2, 3, 4, 5]:   # lst 데이터를 하나씩 꺼내서 n에 반복해서 저장
    print(n, end='\t')      # 리스트, 문자열, 튜플, 세트, 딕셔너리 가능.
print('\n-----------------------')
dic = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
for n in dic:
    print(f'{n} - {dic[n]}', end='\t')  # 딕셔너리는 n print시 키값만 출력
print()


# 02_Ex07_1 (기본예제)
# 문자열 비밀번호 입력. 숫자, 문자 모두 포함하면 가능한 비밀번호.
pwd = input('비밀번호를 입력하세요 >>> ')
ch_count = 0
num_count = 0
sp_count = 0
sp_str = '`~!@#$%^&*()_-+=[]|'

for ch in pwd:
    if ch.isalpha():      # ch가 문자인 경우, True 반환
        ch_count += 1
    elif ch.isnumeric():  # ch가 숫자인 경우, True 반환
        num_count += 1
    elif ch in sp_str:    # ch가 sp_str에 있는 경우
        sp_count += 1

if ch_count > 0 and num_count > 0 and sp_count > 0:
    print('가능한 비밀번호입니다.')
else:
    print('불가능한 비밀번호입니다.')


# 03_for_ex_2 (원하는만큼 반복할 때 쓰는 for문)
for i in range(5):      # range(n): 0 ~ n-1까지 순서대로
    print(i, end='')
print('\n-----------------------')
range(1, 10)            # range(s,e): s ~ e-1까지
range(1, 10, 2)         # (시작값, 종료값, 증감값) --> 2씩 증가


# 04_Ex07_2 (while문 예제를 for문으로 작성) (0331_7일차/완)
dan = int(input('출력할 구구단을 입력하세요 >>> '))
for n in range(1, 10):
    print(f'{dan} X {n} = {dan*n}')
# while문은 프로그램 제어, for문은 데이터를 이용할 때
