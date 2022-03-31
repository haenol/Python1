'''
    목차
    01_print (0324_4일차)
    02_str_format
    03_input
    04_Practice03
'''
# 어떻게 출력을 시키는가
# 이스케이프: 특수문자 표현하는 방식, \로 시작되는 문자열

# 탭: \t --> 정렬할 때 사용
print('번호\t이름\t\t번호')   # 1행2열이 두 글자인데 2열에 세 글자가 있어서 밀림 ... 탭 한 번 더 사용
print('1\t김철수\t1234')
print('2\t이훈\t\t1234')

# " , ' 출력 --> \' \"
print('오늘은 \'파이썬\' 수업이 있는 날입니다.')   # 자바 등에서 많이 사용
print("오늘은 '파이썬' 수업이 있는 날입니다.")     # 파이썬은 이렇게 가능하거든 (반대도 가능)

# 키워드 속성
# 1. sep : 콤마로 데이터를 구분하는 방식에서 데이터 사이에 넣을 문자 설정 가능
print(2022, 3, 24)          # 생략시 공백
print(2022, 3, 24, sep='-')
# 2. end : 출력 끝에 넣을 문자 설정 가능
print('김철수')              # 생략시 줄바꿈
print('김철수', end=',')