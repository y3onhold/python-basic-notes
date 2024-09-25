print("")

#              Basic Notes 8

# __all__
# 패키지, 모듈 위치
# pip install
# 내장 함수
# 외장 함수
# Quiz 10(시그니처 모듈)


#              __all__

print("              __all__")
print()

# travel.__init__ 에서 무었이 import* 에 포함되는지 정리해줌

# from random import *
from travel import *
trip_to = vietnam.VietnamPackage() # 만약 패키지 노트 전부가 주석 처리 될시, 호출 되지 않음
                                   # travel.__init__ 에서   __all__ = ["vietnam"] 이라고 *(모든것) 이 무엇인지 정의해 줘야함
trip_to = thailand.ThailandPackage() # thailand.py 파일 열어서 함께 보기
trip_to.detail()
print()
print()


#              패키지, 모듈 위치

print("              패키지, 모듈 위치")
print()

# 어느 폴더 밑에 파일이 저장 되있는지 알고, 용이하게 파일을 옮길줄 알아야함
# 내장함수 노트와 간섭되서 주석 처리

'''       주석처리 해재 후 보기         '''
# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))
# print()
# print()


#              pip install

print("              pip install")
print()

# 파이썬은 이미 검증된 패키지가 많기 때문에 다 수동으로 만들기보다, 여러 pip를 찾아 쓰는것이 더 효율적이다.
# 예) from random imports *

# pypi 에서 여러 언어의 패키지들을 사용가능.
# beautifulsoup 이라는 웹스크레이핑으로 유명한 pip가 있음
# pip xxxx xxx 가 안될땐 pip3 로 다시 해보기

# pip3 list 로 현재 패키지 내용 볼수있음
# pip3 show xxxx 로 다운된 패키지 디테일 보기
# pip3 install --upgrade xxxx 로 새버전 업데이트
# pip3 uninstall xxxx 로 다운한 패키지 삭제

# 현재 pip3 install beautifulsoup4 안되있음
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())
# pip3 install beautifulsoup4 로 가지고 놀아보기

print()
print()


#              내장함수

print("              내장함수")
print()

# 이미 기본 파이썬에 포함되있기에 임포트가 필요없는 함수

# 예) input()
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다!".format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random # 외장 함수
print(dir())
import pickle
print(dir())
print()

print("랜덤 관련 커멘드 :")
print(dir(random)) # 랜덤 내에서 쓸수 있는 함수들을 알려줌
print()

print("리스트 관련 커멘드 :")
lst = [1, 2, 3] # list 관련 쓸수 있는 커멘드
print(dir(lst))
print()

print("네임 관련 커멘드 :")
name = "Jim"
print(dir(name)) # name 관련 쓸수 있는 커멘드

# 구글에서 list of python builtins 로 파이썬 내장함수 검색 가능
print()
print()


#              외장 함수

print("              외장 함수")
print()

# 구글에서 list of python modules 로 외장함수 목록 볼수 있음

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
import glob
print(glob.glob("*.py")) # 확장자기 py 인 모든 파일
print()

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) # 현재 디렉토리(현재 파이썬 워크 스페이스)
print()

# os 모듈로 폴더 만들고 지우기
'''       주석처리 해재 후 보기'''
# folder = "sample_dir"
# if os.path.exists(folder):
#      print("이미 존재하는 폴더입니다")
#      os.rmdir(folder) # 폴더 삭제
#      print(folder, "폴더를 삭제하였습니다.")
# else:
#      os.makedirs(folder) # 폴더 생성
#      print(folder, "폴더를 생성하였습니다.")
# print(os.listdir()) # 디렉토리 보기

# time : 시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print("우리가 만난지 100일은", today + td) # 오늘부터 100일 후
print()
print()


#              Quiz 10(시그니처 모듈)

print("              Quiz 10(시그니처 모듈)")
print()

# Quiz) 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오

# 조건 : 모듈 파일명은 byme.py 로 작성

# (모듈 사용 예제)
# import byme
# byme.sign()

# (출력 예제)
# 이 프로그램은 이연호에 의해 만들어졌습니다
# 유튜브 : http://www.youtube.com
# 이메일 : yeonho.724l@gmail.com

import byme
byme.sign()
print()
print()