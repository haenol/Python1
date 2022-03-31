'''
    목차
    01_variable_type (0317_2일차)
    02_convert
    03_str_index
    04_str_slice
    05_list
    06_tuple (0322_3일차)
    07_set
    08_dict
    09_address
    10_Practice02 (0322_3일차/완)
'''

# 01_variable_type
name = '김하늘'
print(name, type(name))     # 김하늘 <class 'str'>



# 02_convert
'''
    데이터 형변환: 자료형을 바꿈
    1. 정수로 변환: int(데이터or변수)
     - int(1.9): 소숫점 제거=> 1
     - int('200')=> 200
     - int('3.1425')=> 에러(문자열 내용이 정수가 아님)
    2. 실수로 변환: float(데이터or변수)
    3. 문자열로 변환: str(데이터or변수)
    4. 논리값으로 변환: bool(데이터or변수)=> 데이터의 유무
     - bool(-1)=> True
     - bool('')=> False
'''



# 03_str_index
'''
    index
    - 각 문자마다 부여된 번호
    - 맨 뒤에서부터는 -1로 번호 시작
'''
s = 'Hello'
print(s[0], s[-5])  # H
# 숫자열을 하나하나 뽑고 싶을 때: str형으로 변환
num = 100
one = str(num)[0]
print(type(one))



# 04_str_slice: 주석 설명 생략
s = 'Hello_World'
print(s[0:6])   # 0~5 index print
print(s[0:2:8])   # 0, 2, 4, 6 index print
print(s[-5:])   # -5~-1 index
print(s[-5:-1])   # -5~-2 index
# 내장함수 len(문자열): 문자열 개수
print(len(s))

tel = '010-1234-5678'
print(len(tel))
print(tel[-4:])  # 전화번호 뒷 4자리
print(tel[:9])  # 전화번호 뒷 4자리 제외: len은 13개이지만 인덱스는 0부터 시작인 것 주의!
print(tel[:-4], tel[:len(tel)-4])  # 생각 못한 방법



# 05_list
'''
    List: 여러개 데이터를 순서대로 저장      # 사용처: 조회했던 데이터를 가지고 있을 때 많이 사용
     - 중복된 데이터를 저장할 수 있음
     - 데이터를 추가한 순서대로 저장
     - 추가, 삭제, 수정 가능
'''
lst = [1, 2, 'Hello', 4, 5, True, False, 'World']
print(lst)

# 추가, 삭제, 수정
# 추가: append(맨 뒤에),insert(인덱스 번호를 지정하여 저장)
lst.append('Append'), print(lst)
lst.insert(3,'Test'), print(lst)    # 3번 인덱스에 데이터를 추가하고 나머지는 밀어넣는다.
# 수정: 인덱스를 지정하여 내용을 바꿔줌
lst[3] = 1
print(lst)                                               #QQ. 왜 나는 (1, None)로 바뀌집...=> print를 옆에 같이 둬서!
# 삭제: pop, remove
# pop: 인덱스 번호를 지정하여 삭제, 인덱스 번호 생략시 마지막 데이터 삭제
lst.pop(), print(lst)
lst.pop(5), print(lst)
# remove: 지정한 데이터의 첫 번째로 검색되는 데이터만 삭제
lst.remove(1), print(lst)
# 검색: 찾고자 하는 데이터의 인덱스 번호를 알려줌.                 QQ. True 찾으려면 어떻게? (애초에 두번째 True임)
print(lst.index('World'))
print(lst.index(True))                                     # => True=1이므로 1을 먼저 찾아서 2라는 결과가 나오는 것.
# print(lst.index('test')): list에 데이터가 없으므로 error
# 데이터 전체 삭제
lst.clear(), print(lst)



# 06_tuple
'''
    Tuple                               # 사용처: 고정값(상수)이 필요할 때 많이 사용
     - 데이터를 리스트처럼 저장
     - 데이터를 읽는 방식도 리스트와 동일
     - 단, 최초에 저장한 데이터만 유지=> 데이터 추가, 삭제, 수정 불가능
'''
# tuple 생성
tup1 = (1, 41, 'Hello', False, 'Test', True)    # 괄호 없어도 생성 가능 (0317까지)
print(tup1)
lst = [100, 'Test', True, 3.1415]               # (0322~)
tup3 = tuple(lst)  # 리스트를 튜플로 생성
# tup3[2] = 300 : 데이터 수정 불가능



# 07_set
'''
    set(세트): 집합 형태의 자료형           # 사용처: 로또번호 생성기(중복X)
     - 중복된 데이터가 저장될 수 없음 --> 고유값만 저장됨
     - 데이터가 자동정렬 --> 저장되는 순서가 보장되지 않음
     - 인덱스 사용X
     - lst 등 다른 자료형으로 저장 가능(양방향)    *주의)순서는 매번 달라짐
     - 트리 형태로 저장됨(자료구조: 리스트, 튜플 등 이미 만들어져있는 것의 원리를 공부한다고 생각하면 될 듯)
'''
# set 생성, 추가: add
set1 = {1, 2, 3, 2, 3, 5, 6, -5, 100}
print(set1)     # 중복값 제외, 순서X
set1.add(300)
print(set1)
# 삭제: remove, discard
set1.remove(300)        # remove, 삭제할 데이터가 없으면 error로 처리
set1.discard(300)       # discard, 삭제할 데이터가 없어도 error로 처리하지 않음->
print(set1)



# 08_dict
'''
    딕셔너리(dictionary)
     - 데이터1: 데이터2 한 쌍으로 저장
       키(key): 값(value)
     - key는 중복X, value는 중복O
     - key를 이용하여 데이터 읽기, 저장, 삭제, 수정
'''
# 딕셔너리 생성: 1){key:value}  2)dict()함수 사용-> (key=value)
dict1 = {'홍길동': 20, '김철수': 33, '이영희': 45}
dict2 = dict(A='TEST', B=False)
# 딕셔너리 읽기: 변수(dict)[key값] --> key에 대응되는 값을 읽음
print(dict1['홍길동'])
# 추가: 2가지 방법
dict1['김영희'] = 46
dict1.setdefault('이용수', 999)
# 삭제: pop
dict1.pop('김영희')    # key를 이용하여 삭제(삭제할 key값이 없으면 error)
dict1.popitem()       # 맨 마지막 key 값 삭제: 근데 사용할 일 없음
# 수정
dict1['홍길동'] = 333  # 데이터 추가하는 방법과 동일



# 09_address: 크게 기억못해도 ㄱㅊ
# mutable: 메모리 주소변경X (list, set, dict)
lst = [1, 2, 3, 4, 5]
print(id(lst))
lst.append(100)
print(id(lst))  #---> 값이 추가/삭제되어도 같은 메모리

# immutable: 메모리 주소변경O (int, float, str, tuple)
num = 10
print(num, id(num))
num = 20
print(num, id(num)) #---> 데이터 추가시 메모리 주소변경되어 다른 곳에 저장됨
newNUM = num        #---> 동일한 메모리 주소 사용
print(id(newNUM), id(num))



# 10_Practice02 (0322_3일차/완)
# 1. '31025'를 학년, 반, 번호로 나누어 출력하는 프로그램 구현
num = '31025'
print(num[0], '학년 ', num[1:3], '반 ', num[3:], '번')

# 2. 차량번호 뒤 4자리만 출력
carNO = ['서울2가1234', '10가1234', '288가1234']
# 랜덤 추출해서 인덱스로 가져오면 좋을 것 같은데.. 흠
carNO = '서울2가1234'
carback = carNO[-4:]
print(carNO+'의 차량번호 4자리는 '+carback+'입니다.')

# 3. 문자열 s = 'maple', s의 가운데 글자 출력
# 아무 문자열을 입력해도 가운데 글자 출력하는 프로그램도 (len이 홀수인지, 짝수인지) 구현할 수 있어보임
s = 'maple'
mid = len(s)//2
print(s+'의 가운데 글자는 '+s[mid]+'입니다.')

# 4. 리스트의 3~7번째 요소만 추출한 결과, 리스트에서 2번째 요소를 출력
lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print('3번째 요소부터 7번째 요소=', lst[2:7])     # print에서 +는 문자열일 때만
print('3번째 요소부터 7번째 요소 중 2번째 요소=', lst[2:7][1])

# 5. 주말 할인 메뉴- 금:탕수육, 토:유산슬, 일:팔보채
DisMenu = {'금요일': '탕수육', '토요일': '유산슬', '일요일': '팔보채'}
print('금요일:', DisMenu['금요일'],
      '\n토요일:', DisMenu['토요일'],
      '\n일요일:', DisMenu['일요일'])
