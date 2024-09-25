print("")

#              Basic Notes 4

# Quiz 6(표준 체중)
# 표준 입출력
# 다양한 출력 포멧
# 파일 입출력
# pickle
# with (한줄 파일)
# Quiz 7(보고서 파일 !!파일생성주의!!)


#              Quiz 6 (표준 체중)

print("              Quiz 6 (표준 체중)")
print()

# 표준 체중을 구하는 프로그램을 작성하시오

# (성별에 따른 공식)
#  남자 : 키(m) x 키(m) x 22
#  여자 : 키(m) x 키(m) x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#        * 함수명 : std_weight
#        * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175의 남자의 표준 체중은 67.38kg 입니다.


def std_weight(height, gender):
     if gender == "남자":
          return height * height * 22
     elif gender == "여자":
          return height * height * 21

height = 175
gender = "남자"
weight = round(std_weight(height / 100,gender), 2)

print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
print()
print()


#              표준입출력

print("              표준입출력")
print()

print("Python", "Java", "Javascript", sep=" vs ")
print()

print("Python", "Java", sep=",", end="?")
print("무엇이 더 재밌을까요?")
print()

# import sys
# print("Python", "Java", file=sys.stdout) # 표준 출력
# print("Python", "Java", file=sys.stderr) # 표준 에러

# 시험 성적
print("시험 성적")
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items(): # 사전의 for 루프 쓸때는 "사전.items()" 로 튜플 출력 
     # print(subject, score)
     print(subject.ljust(8), str(score).rjust(4), sep=":") # 과목은 8칸 뒤에 왼쪽 정령, 스코어는 4칸 뒤에 오른쪽 정렬
print()

# 은행 대기순번표
print("은행 대기순번표")
# 001, 002, 003, ...
for num in range(1,21):
     print("대기번호 : " + str(num).zfill(3)) # 값이 3 자리가 되게 앞에 0을 채워줌
  
# answer = input("아무 값이나 입력하세요 : ")
# print("입력하신 값은 " + answer + "입니다.")

# !!!   input으로 숫자를 받게 되면 스트링으로 입력됨   !!!
print()
print()


#              다양한 출력 포멧

print("              다양한 출력 포멧")
print()

# *프리셋*
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보")
print("{0: >10}".format(500))
print()

# 양수일 땐 +로 표시, 음수일 땐 -로 표시; 오른쪽 정렬
print("양수일 땐 +로 표시, 음수일 땐 -로 표시; 오른쪽 정렬")
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
print()

# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("왼쪽 정렬하고, 빈칸으로 _로 채움")
print("{0:_<10}".format(500))
print()

# 세자리 마다 콤마를 찍어주기
print("세자리 마다 콤마를 찍어주기")
print("{0:,}".format(100000000000))
print("{0:+,}".format(100000000000)) # +,- 붙이기
print()

# 세자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# 빈자리는 ^로 채워주기
print("세자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기 \n빈자리는 ^로 채워주기")
print("{0:^<+30,}".format(100000000000))
print()

# 소수점 출력
print("소수점 출력")
print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3))
print()

#              파일 입출력

print("              파일 입출력")
print()

score_file = open("score.txt", "w", encoding="utf8") # w는 쓰기, 한글 정보는 utf8로 엔코딩 하는게 좋음
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8") # a 는 어펜드로 이어쓰기
score_file.write("과학 : 80")                         # .write는 줄바꿈이 안됨
score_file.write("\n코딩 : 100")

# 전체 읽기
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()
print()

# 줄별로읽기, 커서는 다음줄로 이동
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end=" ")
print(score_file.readline(), end=" ")
print(score_file.readline(), end=" ")
print(score_file.readline())
score_file.close()
print()


# 몇줄일지 모를때 다 읽는법
score_file = open("score.txt", "r", encoding="utf8")
while True:
     line = score_file.readline()
     if not line:
          break
     print(line, end="")
score_file.close()
print()
print()

# 리스트에 값을 넣는법
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # readlines()사용해서 리스트로 저장
for line in lines:
     print(line, end="")
score_file.close()
print()
print()
print()


#              Pickle

print("              Pickle")
print()

import pickle
profile_file = open("profile.pickle", "wb")
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
prifile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()
print()
print()


#              With

print("              With")
print()

import pickle
with open("profile.pickle", "rb") as profile_file:
     print(pickle.load(profile_file))
# with 에서 자동으로 파일을 닫아준다
print()

with open("study.txt", "w", encoding="utf8") as study_file:
     study_file.write("파이썬을 열심히 공부하고 있어요")
with open("study.txt", "r", encoding="utf8") as study_file:
     print(study_file.read())
print()
print()


#              Quiz 7 (보고서 파일)

print("              Quiz 7 (보고서 파일)")
print()

# Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습미다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - x 주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :

# 1주차부터 50주차가지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다

# 내 답변
# for report in range(1,51):
#      report_file = open(str(report) + "주차.txt", "w", encoding="utf8")
#      print("- " + str(report) + "주차 주간보고 -", file=report_file)
#      print("부서 :", file=report_file)
#      print("이름 :", file=report_file)
#      print("업무 요약 :", file=report_file)
#      report_file.close()

# 답안지
for i in range(1,51):
     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
          report_file.write("- {0} 주차 주간보고 -".format(i))
          report_file.write("\n부서 :")
          report_file.write("\n이름 :")
          report_file.write("\n업무 요약 :")