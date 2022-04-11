# input : 데이터 입력 받는 함수
name = input('이름을 입력하세요 : ')    # '': 안내문, name: 입력받은 데이터 저장
print(f'입력된 이름 : {name}')
print(type(name))                    # input함수로 입력받은 데이터는 모두 문자열 ... 반드시 형변환 필요

# 정수 입력 - int
# 실수 입력도 동일 float()
num = int(input('숫자 하나 입력 : '))
print(f'입력된 숫자{num}', type(num))

