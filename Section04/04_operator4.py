""" 0325_5일차
논리연산자
    - 조건식이 두 개 이상일 때 처리하는 연산자
    and: 그냥 우리가 아는
    or: 수학에서의 의미 그대로
    not a: a가 참이면 False, 거짓이면 True
"""
n1, n2 = 10, 7
print(n1 > 5 and n2 < 7)    # False
result = n1 > 10    # False
print(not result)   # True
# 강의 코드 생략

# 강사님 예제
# n1이 5보다 크고 n2가 10보다 작고 n1이 n2와 다른가?
print(5 < n1 != n2 < 10)
# 밑줄 쳐져서 simply 옵션 썼더니 엄청 간추려짐

"""
연산자 우선순위(p.71)
그냥 생략해도 될 듯. 수학이랑 똑같음.
"""

