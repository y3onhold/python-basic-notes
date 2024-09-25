print("")

#              Basic Notes 6

# 스타크래프트 전반전
# 스타크래프트 후반전
# Quiz 8(부동산 프로그램)
# 예외처리
# 에러 발생 시키기
# 사용자 정의 예외처리
# Finally

from random import*

# 일반 유닛
class Unit:
     def __init__(self, name, hp, speed):
          self.name = name
          self.hp = hp
          self.speed = speed
          print("{0} 유닛이 생성되었습니다.".format(name))

     def move(self, location):
          print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
                .format(self.name, location, self.speed))

     def damaged(self, damage):
          print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
          self.hp -= damage
          print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
          if self.hp <= 0:
               print("{0} : 파괴되었습니다".format(self.name))

# 공격 유닛
class AttackUnit(Unit):
     def __init__(self, name, hp, speed, damage):
          Unit.__init__(self, name, hp, speed)
          self.damage = damage

     def attack(self, location):
          print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 : {2}]"\
                .format(self.name, location, self.damage))
          
# 마린
class Marine(AttackUnit):
     def __init__(self):
          AttackUnit.__init__(self, "마린", 40, 1, 5)

     # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
     def stimpack(self):
          if self.hp > 10:
               self.hp -= 10
               print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
          else:
               print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# 탱크
class Tank(AttackUnit):
     # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가.
     seize_developed = False # 시즈모드 개발여부

     def __init__(self):
          AttackUnit.__init__(self, "탱크", 150, 1, 35)
          self.seize_mode = False

     def set_seize_mode(self):
          if Tank.seize_developed == False:
               return
          # 현재 시즈모드 아님 -> 시즈모드
          if self.seize_mode == False:
               print("{0} : 시즈모드로 전환 합니다.".format(self.name))
               self.damage *= 2
               self.seize_mode = True
          # 현재 시즈모드 -> 시즈모드 해제
          else:
               print("{0} : 시즈모드를 해제합니다.".format(self.name))
               self.damage /= 2
               self.seize_mode = False

# 공중 유닛
class Flyable:
     def __init__(self, flying_speed):
          self.flying_speed = flying_speed

     def fly(self, name, location):
          print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]"\
                .format(name, location, self.flying_speed))

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
     def __init__(self, name, hp, damage, flying_speed):
          AttackUnit.__init__(self, name, hp, 0, damage) # 지상 스피드 0
          Flyable.__init__(self, flying_speed)

     def move(self, location):
          self.fly(self.name, location)

class Wraith(FlyableAttackUnit):
     def __init__(self):
          FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
          self.clocked = False # 클로킹 모드 (해제 상태)

     def clocking(self):
          if self.clocked == True : # 클로킹 모드 -> 모드 해제
               print("{0} : 클로킹 모드 해제합니다.".format(self.name))
               self.clocked = False
          else: # 클로킹 모드 해제 -> 모드 설정
               print("{0} : 클로킹 모드 설정합니다.".format(self.name))
               self.clocked = True

#              스타크래프트 후반전
               
def game_start():
     print("[알림] 새로운 게임을 시작합니다.")

def game_over():
     print("Player : gg")
     print("[Player] 님이 게임에서 퇴장 하셨습니다.")

# 게임 진행
game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

# 유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
     unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# 공격 모드 준비 (스팀팩, 시즈모드, 클로킹)
for unit in attack_units:
     if isinstance(unit, Marine):
          unit.stimpack()
     elif isinstance(unit, Tank):
          unit.set_seize_mode()
     elif isinstance(unit, Wraith):
          unit.clocking()

# 전군 공격
for unit in attack_units:
     unit.attack("1시")

# 전군 피해
for unit in attack_units:
     unit.damaged(randint(5,21)) # 공격은 랜덤으로 받음 (5~20)

# 게임 종료
game_over()
print()
print()

#              Quiz 8(부동산 프로그램)

print("              Quiz 8(부동산 프로그램)")
print()

# Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

# (출력 예제)
# 총 3 대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# [코드]
class House:
     # 매물 초기화
     def __init__(self, location, house_type, deal_type, price, completion_year):
          self.location = location
          self.house_type = house_type
          self.deal_type = deal_type
          self.price = price
          self.completion_year = completion_year

     # 매물 정보 표시
     def show_detail(self):
          print(self.location, self.house_type, self.deal_type, self.price, \
                self.completion_year)

houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")
houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}대의 매물이 있습니다".format(len(houses)))
for house in houses:
     house.show_detail()
print()
print()


#              예외처리

print("              예외처리")
print()

'''       주석처리 해재 후 보기       '''

# try:
#      print("나누기 전용 계산기입니다.")
#      nums = []
#      nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#      nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
#      nums.append(int(nums[0]/nums[1])) # 만약 주석처리될시, 리스트 인덱스 에러 발생
#      print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError: # 숫자가 아닌 값을 입력했을시
#      print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err: # 0 으로 수를 나누었을시
#      print(err) # err로 프로그램이 알려준 에러 프린트 가능
# except Exception as err: # 모든 오류를 받음
#      print("알 수 없는 에러가 발생하였습니다.")
#      print(err)
print()
print()


#              에러 발생 시키기

print("              에러 발생 시키기")
print()

'''       주석처리 해재 후 보기       '''

# try:
#      print("한 자리 숫자 나누기 전용 계산기입니다.")
#      num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#      num2 = int(input("두 번째 숫자를 입력하세요 : "))
#      if num1 >= 10 or num2 >=10:
#           raise ValueError
#      print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#      print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
print()
print()


#              사용자 정의 예외처리

print("              사용자 정의 예외처리")
print()

'''       주석처리 해재 후 보기       '''

# class BigNumberError(Exception):
#      def __init__(self, msg):
#           self.msg = msg
#      def __str__(self):
#           return self.msg

# try:
#      print("한 자리 숫자 나누기 전용 계산기입니다.")
#      num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#      num2 = int(input("두 번째 숫자를 입력하세요 : "))
#      if num1 >= 10 or num2 >=10:
#           raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
#      print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#      print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#      print("에러가 발생 하였습니다. 한 자리 숫자만 입력하세요.")
#      print(err)
print()
print()


#              Finally

print("              Finally")
print()

# 예외처리가 어떻게 되든 마지막에 무조건 실행되는 부문
'''       주석처리 해재 후 보기       '''

# class BigNumberError(Exception):
#      def __init__(self, msg):
#           self.msg = msg
#      def __str__(self):
#           return self.msg

# try:
#      print("한 자리 숫자 나누기 전용 계산기입니다.")
#      num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#      num2 = int(input("두 번째 숫자를 입력하세요 : "))
#      if num1 >= 10 or num2 >=10:
#           raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
#      print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#      print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#      print("에러가 발생 하였습니다. 한 자리 숫자만 입력하세요.")
#      print(err)
# finally:
#      print("계산기를 이용해 주셔서 감사합니다.")