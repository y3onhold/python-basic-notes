print("")

#              Basic Notes 1

# 강아지 예
# 주석
# 특수연산
# 간단한 수식 단축식
# 숫자 처리 함수
# 랜덤 함수
# 문자열
# 슬라이싱
# 문자열 처리함수
# 문자열 포멧
# 탈출 문자
# Quiz 3(비번 프로그램)



#              완전 기초

print("              완전 기초")
print()
print("문자열 자료도 숫자와 연결됨: ")
print("ㅋ" * 7) # ㅋㅋㅋㅋㅋㅋㅋ
print()

print("Boolean 반대로 뽑기: ")
print(not True)
print(not (5 > 10))
print()
print()


#              강아지 예

print("              강아지 예:")
name = "번개"
age = 6
is_adult = age >= 4

print("우리집 강아지의 이름은 " + name  + "예요")
print(name + "는", str(age), "살이고 산책을 좋아해요")
print(name + "는 어른일까요? : " + str(is_adult))
print()
print()


#              주석
'''이렇게 하면은 
여러 문장이 주석이 됩니다

여러문장을 드래그 후 
command + / 로 단축이 가능합니다'''


#              특수연산

print("              특수연산")
print(2**3) # 2^3
print(10%3) # (1) 나누기 후 나머지
print(5//3) # (1) 나머지 없는 몫
print()
print()


#              간단한 수식 단축식

print("              간단한 수식 단축식")
num = 14
print(num) # 14
num = num + 2 # OR num += 2  ->  16
print(num) #16
'''
사직연산 다 똑같음:
    +=    -=
    *=    /=    %=
'''
print()
print()


#              숫자 처리 함수

print("              숫자 처리 함수")
print(abs(-5)) # 5
print(pow(4,2)) # 16
print(max(5,12)) # 12
print(min(5,12)) # 5
print(round(3.14)) # 3
print()
print()


#              랜덤함수

print("              랜덤함수")
from random import * # 불러오기
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 부터 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1 부터 10 이하의 임의의 값 생성
  # 단축식
print(randrange(1,46)) # 1 ~ 46 미만의 임의의 값 생성
print(randint(1,45)) # 1 ~ 46 미만의 임의의 값 생성
print()
print()


#              문자열

print("              문자열")
sentence = '''
나는 소년이고,
파이썬은 쉬워요
'''
print(sentence)
print()
print()


#              슬라이싱

print("              슬라이싱")
jumin = "050724-1234567"
print("성별 : " + jumin[7]) # 7번째 자리 수 (0부터 시작)
print("월 : " + jumin[0:2]) # 0 부터 2 직전까지
print("생년월일 : " + jumin[:6]) # 0 은 스킵 가능
print("뒤 7 자리 : " + jumin[7:]) # 맨 뒷자리도 스킵 가능
print("뒤 7 자리(뒤에부터) : " + jumin[-7:]) # 맨 뒤부터 0, -1, -2, etc.
print()
print()


#              문자열 처리함수

print("              문자열 처리함수")
python = "Python is Amazing"
print(python.lower()) # python is amazing
print(python.upper()) # PYTHON IS AMAZING
print(python[0].isupper()) # 0번째 자리가 대문자 인가? (True)
print(len(python)) # 얼마나 긴가? (17)
print(python.replace("Python", "Java"))
print()

index = python.index("n") # n 이 몇번째에 나오나?
print(index)
index = python.find("n", index + 1) # 두번째 n은 언제 나오나?
print(index)                        # index는 못찾으면 오류
print(python.count("n")) # 2          find는 못찾으면 -1
print()
print()


#              문자열 포멧

print("              문자열 포멧")
  # 방법 1
print("나는 %d살입니다" % 20)           # %d 는 수를 받는다
print("나는 %s을 좋아해요" % "파이썬")    # %s 는 문장이지만 다 된다
print("Apple은 %c로 시작해요" % "A")    # #c 는 캐릭터(글자)
print("나는 %s색과 %s색을 좋아해요" % ("파란", "하얀"))
print()
  # 방법 2
print("나는 {}살입니다".format(20))
print("나는 {0}색과 {1}색을 좋아해요".format("파란", "하얀"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란", "하얀"))
  # 방법 3
print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color = "하얀"))
  # 방법 4
age = 20
color = "하얀"
print(f"나는 {age}살이며, {color}색을 좋아해요")
print()
print()


#              탈출문자

print("              탈출문자")
print("백문이 불여일견 \n백견이 불여일타") # \n : 한줄 떨구기
# print("저는 '나도코딩' 입니다")
# print('저는 "나도코딩" 입니다')
print("저는 \"나도코딩\" 입니다")

  # \\ : 문장 내에서 \ 나올때
print("\\Users\\yeonholee\\Desktop\\PythonWorkspace\\Basic Notes.py")
print()
  # \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # (Red ) 덮어 씌우기
print()
  # \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")
print()
  # \t : 탭
print("Red\tApple")
print()
print()

#              Quiz 3 비번 프로그램

print("              Quiz 3 비번 프로그램")

# 규칙1 : http:// 부분 제외
# 규칙2 : 처음 만나는 점(.) 이후는 제외
# 규칙3 : 글자중 처음 세자리 + 글자 갯수 + 글자 내 "e" 수 + "!"" 로 구성
#             (nav)         (5)         (1)       (!)
# 예) 비번 : nav51!

url = "http://naver.com"

site = url.replace("http://", "")    # 규칙 1
siteEnd = site.find(".")
site = site[:siteEnd]                # 규칙 2

countE = site.count("e")

password = site[:3] + str(siteEnd) + str(countE) + "!" # 규칙 3
print("{}의 비밀번호는 {}입니다".format(url, password))
print()
print()
print()