name = '홍길동'
age = 20

# format 함수
msg1 = '이름 : {}\t\t나이 : {}'.format(name, age)       # %연산자가 {}이 된 느낌
# msg1 = '이름 : {0}\t\t나이 : {1}'.format(name, age)
# msg1 = '이름 : {1}\t\t나이 : {0}'.format(name, age)
print(msg1)

# 3.6 버전 이상: 변수명 바로 넣기
msg2 = f'이름 : {name}\t\t나이 : {age}'
print(msg2)

# %연산자 수업에서 생략함. 체크해놓고 읽어보래...