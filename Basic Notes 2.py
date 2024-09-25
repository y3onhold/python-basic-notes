print("")

#              Basic Notes 2

# 리스트 []
# 사전 {}
# 튜플()
# 세트{1,2,3}
# 자료구조의 변경
# 셔플, 샘플
# Quiz 4(파이썬 코딩 대회)

#              리스트 []

print("              리스트 []")
print()

# subway1 = 10
# subway2 = 20
# subway3 = 30
subway = [10, 20, 30]  # 여러 변수를 하나로 묶어서 나열
print(subway)
print()

subway = ["유재석", "조세호", "박명수"]
print(subway)          # 스트링도 가능하다
print()

# 조세호씨가 몇 번째 칸에 타고 있는가?
print("조세호씨가 몇 번째 칸에 타고 있는가?")
print(subway.index("조세호"))
print()

# 하하씨가 다음 정류장에서 다음 칸에 탐
print("하하씨가 다음 정류장에서 다음 칸에 탐 :")
subway.append("하하")
print(subway)
print()

# 정형돈씨를 유재석 / 조세호 사이에 태워봄
print("정형돈씨를 유재석 / 조세호 사이에 태워봄 :")
subway.insert(1, "정형돈") # 나머지는 한 칸씩 밀린다
print(subway)
print()

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print("지하철에 있는 사람을 한 명씩 뒤에서 꺼냄 :")
print(subway.pop())
print(subway)
# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway)
print()

# 같은 이름의 사람이 몇 명 있는지 확인
print("같은 이름의 사람이 몇 명 있는지 확인")
subway.append("유재석")
print(subway)
print(subway.count("유재석")) # 2 번
print()

# 정렬도 가능
print("정렬도 가능")
num_list = [5,2,4,3,1,]
num_list.sort()
print(num_list)
# 순서 뒤집기 가능
print("순서 뒤집기 가능")
num_list.reverse()
print(num_list)
# 리스트 모두 지우기
'''
num_list.clear()
print(num_list)
'''

# 다양한 자료형 함께 사용
num_list = [5,2,4,3,1,]
mix_list = ["조세호", 20, True]
# print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)  # num_list 후에 mix_list가 붙여짐
print()
print()


#              사전 {1: "유재석", 72: "김태호"}

print("              사전 {1: \"유재석\", 72: \"김태호\"}")
print()

cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3]) # 유재석
print(cabinet[100]) # 김태호
print(cabinet.get(3)) # 유재석
print()
  # print(cabinet[5])     = KeyError
  # print(cabinet.get(5)) = "None"
print(cabinet.get(5,"사용가능")) # sub* 가능
print()

print(3 in cabinet) # True
print(5 in cabinet) # False
print()

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])
print()

  # 새 손님
print(cabinet)
cabinet["A-3"] = "김종국" # 덮어씌움
cabinet["C-20"] = "조세호"
print(cabinet)
print()
  # 간 손님
del cabinet["A-3"]
print(cabinet)
print()
  # key 들만 출력
print(cabinet.keys())
  # value 들만 출력
print(cabinet.values())
  # key, value 쌍으로 출력
print(cabinet.items())
print()

  #목욕탕 페점
cabinet.clear()
print(cabinet)
print()
print()


#              튜플 ()

print("              튜플 ()")
print()

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])
# menu.add("생선까스")  => 추가/변경 안됨
print()

# name = "김종국"
# age = 20
# hobby = "운동"
# print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "운동")
print(age, name, hobby)
print()
print()


#              세트 {1,2,3} 

print("              세트 {1,2,3}")
# 중복안됨, 순서 없음
print()

my_set = {1,2,3,3,3}
print(my_set) # {1,2,3}
print()

java =  {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))
print()

# 합집합 (java를 할 수 있거나 python을 할 수 있는 개발자)
print(java | python)
print(java.union(python))
print()

# 차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))
print()

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)
print()

# java 를 잊었어요
java.remove("김태호")
print(java)
print()
print()


#              자료구조의 변경
print("              자료구조의 변경")
print()

# 커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))
print()
print()


#              보너스 (shuffle, sample)
from random import *
first = [1,2,3,4,5]
print(first)
shuffle(first)
print(first)
print(sample(first, 2))
#               |   |
#             샘플중  n  개의 수를 랜덤으로 추출
print()
print()



#              Quiz 4 (파이썬 코딩 대회)

print("              Quiz 4 (파이썬 코딩 대회)")

# 학교에서 파이썬 코딩 대회를 주최했다.
# 참석룰을 높이기 위해 댓글 이벤트를 진행
# 댓글 작성자중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 된다

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용

# (출력 예제)
#  -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]
#  -- 축하합니다 --


from random import *
users = range(1,21)   # 1부터 20까지 숮자를 생성
# print(type(users)) => 리스트가 아닌 레인지
users = list(users)
# print(type(users)) => 레인지 에서 리스트로 바뀜
shuffle(users)

winners = sample(users, 4) # 1명은 치킨 3명은 커피
print(" -- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print(" -- 축하합니다 --")


#              내 답안
# users = [1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20]
# from random import *
# shuffle(users)
# print(" -- 당첨자 발표 --")
# print("치킨 당첨자 : " + str(users.pop()))
# print("커피 당첨자 : " + str(sample(users, 3)))
# print(" -- 축하합니다 --")

print()
print()