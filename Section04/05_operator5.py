"""
비트연산자
    &   |   ^   ~   <<  >>
"""
n1, n2 = 10, 7  # 10-->1010, 7-->0111
print("and : ", n1 & n2)  # --> 2
print("or : ", n1 | n2)   # --> 15
print("xor : ", n1 ^ n2)  # --> 13
print("not : ", ~n1)      # --> -11
# 솔직히 이진수 몰라서 잘 모르겠는데 몰라도 될 듯

n3 = 1
print(n3 << 3)   # 1을 왼쪽으로 3칸 밈 1000--> 8
n4 = 256
print(n4 >> 2)   # 뭐라는겨