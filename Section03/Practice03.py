'''
# 1. 사용자로부터 2개의 실수 입력, 합계 구하기
fl1 = input('첫 번째 실수를 입력하세요 >>> ')
fl2 = input('두 번째 실수를 입력하세요 >>> ')
print(f'{fl1}와 {fl2}의 합은 {float(fl1)+float(fl2)}입니다.')
# @@@@@@@고칠점@@@@@@@
# 나중에 언제 연산할지 모르니까 처음에 입력 받을 때부터 float형으로 바꿔놓기
# fl1 = float(input('첫 번째 실수를 입력하세요 >>> '))

# 2. 사용자로부터 1에서 12 사이의 월을 입력받아 해당 월이 며칠까지 있는지 출력하는 프로그램 구현
month = int(input('1~12 사이의 월을 입력하세요 >>> '))
day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(f'{month}월은 {day[month-1]}일까지 있습니다.')
# if문만 생각했는데 리스트에 저장하는 방법은 생각못함---> 리스트 활용을 많이 해볼 것

# 3. 영어사전 구현. Dict 생성 후 실행 예처럼 동작하는 프로그램 구현
english_dict = {
    'flower': '꽃',
    'fly': '날다',
    'floor': '바닥'
}
e = input('영어 단어를 입력하세요 >>> ')
print(f'{e}: {english_dict[e]}')
'''
# 4. 원하는 장소를 입력받아 "동일한 입력은 무시"하고 모든 입력 저장. 학생 3명, 실행 예처럼 구현 => set
place = {}
place = input('희망하는 수학여행지를 입력하세요 >>> ')
place = input('희망하는 수학여행지를 입력하세요 >>> ')
place = input('희망하는 수학여행지를 입력하세요 >>> ')
l_place = list(place)
print(f'조사된 수학여행지는 {l_place}입니다.')
# 작업중 (3/24듣는중)