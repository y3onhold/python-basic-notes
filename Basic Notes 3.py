print("")

#              Basic Notes 3

# if
# for 루프
# while 루프
# continue 와 break
# 한줄 for 루프
# Quiz 5(택시기사)
# 함수
# 전달값과 반환값
# 기본값
# 키워드값
# 가변 인자
# 지역변수 전역변수

#              If (분기)

print("             If(분기)")
print()

'''       주석처리 해재 후 보기       '''
# weather = input("오늘 날씨는 어때요? ")

# if weather == "비" or weather == "눈":
#      print("우산을 챙기세요")
# elif weather == "미세먼지":
#      print("마스크를 챙기세요")
# else:
#      print("준비물 필요 없어요.")

# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#      print("너무 더워요, 나가지 마세요")
# elif 10 <= temp and temp < 30:
#      print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#      print("외투를 챙기세요")
# else:
#      print("너무 추워요. 나가지 마세요")
print()
print()

#              For(루프)

print("             For(루프)")
print()

for waiting_no in range(1,6):   # [1,2,3,4,5]
     print("대기번호 : {0}".format(waiting_no))
print()

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
     print("{0}, 커피가 준비되었습니다".format(customer))
print()
print()


#              While(루프)

print("             While(루프)")
print()

'''       주석처리 해재 후 보기       '''
# customer = "토르"
# index = 5
# while index >= 1:
#      print("{0}, 커피가 준비 되었습니다, {1} 번 남았어요".format(customer, index))
#      index -= 1
#      if index == 0:
#           print("커피는 폐기처분 되었습니다.")

 # 무한루프
# customer = "아이언맨 "
# index = 1
# while True:
#      print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))
#      index += 1

 # 무한루프 수정
# customer = "토르"
# person = "Unknown"

# while person != customer :
#      print("{0}, 커피가 준비 되었습니다.".format(customer))
#      person = input("이름이 어떻게 되세요? ")
print()
print()


#              Continue 와 Break

print("             Continue 와 Break")
print()

absent = [2,5]
no_book = [7]
for student in range(1,11):
     if student in absent:
          continue
     elif student in no_book:
          print("오늘 수업 여기까지. {0}은 교무실로 따라와.".format(no_book))
          break
     print("{0}, 책을 읽어봐".format(student))
print()
print()


#              한줄 for

print("             한줄 for")
print()

# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101 102 103 104.
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)
print()

# 학생 이름을 길이로 변환
students1 = ["Iron man", "Thor", "I am groot"]
students1 = [len(i) for i in students1]
print(students1)
print()

# 학생 이름을 대문자로 변환
students2 = ["Iron man", "Thor", "I am groot"]
students2 = [i.upper() for i in students2]
print(students2)
print()
print()


#              Quiz 5 (Cocoa 택시 기사)

print("             Quiz 5 (Cocoa 택시 기사)")
print()

# 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 구하시요

# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매치 해야 합니다.

# (출력문 예제)
# [0] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [0] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2 분

 # 내 답변
# complete = 0
# for customer in range(1,51):
#      from random import *
#      time = randrange(5,51)
#      if 5 <= time <= 15:
#           print("[0] {0}번째 손님 (소요시간 : {1}분)".format(customer, time))
#           complete += 1
#      else:
#           print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(customer, time))
# print()
# print("총 탑승 승객 : {0}분".format(complete))

 # 답안지
from random import *
cnt = 0
for i in range(1,51):
     time = randrange(5,51)
     if 5 <= time <= 15:
          print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
          cnt += 1
     else:
          print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0}분".format(cnt))
print()
print()


#              함수

print("             함수")
print()

def open_account():
     print("새로운 계좌가 셍성되었습니다.")
open_account() # 함수 호출 -> 실행
print()

#              전달값과 반환값

print("             전달값과 반환값")
print()

def deposit(balance, money): # 입금
     print("입금이 완료 되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
     return balance + money

def withdraw(balance, money): # 출금
     if balance >= money:
          print("출금이 완료 되었습니다. 잔액은 {0}원 입니다".format(balance - money))
          return balance - money
     else:
          print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
          return balance
     
def withdraw_night(balance, money):
     commission = 100
     return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500) # 튜플 반환값
print("수수료는 {0} 원이며, 잔액은 {1} 원 입니다".format(commission, balance))
print()
print()


#              기본값

print("             기본값")
print()

# def profile(name, age, main_lang):
#      print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
#      .format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업.

def profile(name, age=17, main_lang="파이썬"):
     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
           .format(name, age, main_lang))
     
profile("유재석")
profile("김태호",20)
print()
print()


#              키워드값

print("             키워드값")
print()

def profile(name, age, main_lang):
     print(name,age,main_lang)

profile(name="유재석", main_lang="파이썬", age=20) # name, age, lang 순서가 상관 없어짐
profile(main_lang="자바", age=25, name="김태호")
print()
print()


#              가변 인자

print("             가변 인자")
print()

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#      print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end=" " 때문에 밑에줄도 연결되서 적힘(lang1,lang2...)
#      print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language): # *language 가변인자
     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
     for lang in language:
          print(lang, end=" ")
     print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")
print()
print()


#              지역변수 전역변수

print("             지역변수 전역변수")
print()

gun = 10

def checkpoint(soldiers): # 경계근무
     global gun # 전역 공간에 있는 gun 사용
     gun = gun - soldiers
     print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
     gun = gun - soldiers
     print("[함수 내] 남은 총 : {0}".format(gun))
     return gun

print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계근무 나감
gun = checkpoint_ret(gun, 2) # 전역 gun의 값을 업데이트
print("남은 총 : {0}".format(gun))