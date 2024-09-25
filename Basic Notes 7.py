print("")

#              Basic Notes 7

# Quiz 9(치킨집)
# 모듈
# 패키지


#              Quiz 9(치킨집)

print("              Quiz 9(치킨집)")
print()

# Quiz) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
# 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작 하였습니다
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올때는 ValueError 로 처리
#        출력 메시지 : "잘못된 값을 입력하였습니다."
# 조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10 마리로 한정
#         치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#         출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

# [코드]
chicken = 10
waiting = 1 # 홀 안에는 현재 만석. 대기번호 1 부터 시작

# 10마리가 다 팔림
class SoldOutError(Exception):
     pass

# 주문이 재고보다 많음
class StockError(Exception):
     def __init__(self, msg):
          self.msg = msg
     def __str__(self):
          return self.msg

     
'''       주석처리 해재 후 보기         '''
# while(True):
#      try:
#           print("[남은 치킨] : {0}".format(chicken))
#           order = int(input("치킨 몇 마리 주문하시겠습니까?"))
          
#           if order > chicken: # 재고보다 주문이 많음
#                raise StockError("주문하신 갯수 : {0}마리; 남은 재료 : {1}마리".format(order, chicken))
#           elif order <= 0:
#                raise ValueError
#           else:
#                print("[대기번호 {0}] {1} 마리 주문이 완료 되었습니다."\
#                     .format(waiting, order))
#                waiting += 1
#                chicken -= order
#           print()
#           if chicken == 0:
#                raise SoldOutError
#      except StockError as err:
#           print("죄송합니다 재료가 부족합니다.")
#           print(err)
#           print()
#      except ValueError:
#           print("잘못된 값을 입력하였습니다, 1 이상의 숫자만 입력해주세요")
#           print()
#      except SoldOutError:
#           print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#           break
print()
print()


#              모듈

print("              모듈")
print()

# 다른 파일의 코드를 불러와 연동하여 씀

import theater_module # 모듈속에 있는것들을 호출해서 사용 가능
theater_module.price(3) # 3명이서 영화보러 갔을때 가격
theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때
theater_module.price_soldier(5) # 5명의 군인이 영화 보러 갔을 때
print()

import theater_module as mv # 모듈을 별명(mv)으로 호출
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)
print()

from theater_module import * # 모듈안에서 코드를 하듯이 이름으로 불러옴
# from random import *
price(3)
price_morning(4)
price_soldier(5)
print()

from theater_module import price, price_morning # 선택 옵션만 불러옴
price(5)
price_morning(6)
# price_soldier(7) # 호출 안되야 하지만 위에 import * 때문에 가능
print()

from theater_module import price_soldier as price # 선택후 별명 입력
price(5)
print()
print()


#              패키지

print("              패키지")
print()

# 한 폴더에 여러가지 모듈을 정리후 불러와서 사용

import travel.thailand # 모듈과 패키지만 호출 가능. 클래스는 밑에서 한번 더 불러야함
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()
print()

from travel.thailand import ThailandPackage # 프롬 임포트를 사용면 클래스만 호출후 사용 가능
trip_to = ThailandPackage()
trip_to.detail()
print()

from travel import vietnam # travel에 위치에서 코드 하듯이 vietnam만 호출하여 쓰기
trip_to = vietnam.VietnamPackage()
trip_to.detail()
print()
print()