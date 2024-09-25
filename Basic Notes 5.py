print("")

#              Basic Notes 5

# 클래스
# __init__
# 멤버 변수
# 메소드
# 상속
# 다중 상속



#              클래스

print("              클래스")
print()

# # 마린 : 공격 유닛, 군인. 총을 쏠수 있음
# name = "마린" # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반모드 / 시즈모드.
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# # 탱크 1대 추가
# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

# def attack(name, location, damage):
#      print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(\
#           name, location, damage))
     
# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)


# 일반 유닛
class Unit:
     def __init__(self, name, hp, damage):
          self.name = name
          self.hp = hp
          self.damage = damage
          print("{0} 유닛이 생성 되었습미다.".format(self.name))
          print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 15)
print()
print()


#              __init__


# __init__ 은 생성자
# 예) 마린과 탱크라는 객체를 만들때 자동으로 호출됨

# 객체는 클래스로부터 만들어지는 것들
# 마린과 탱크는 Unit의 인스턴스다(instance)

# 객체를 생성할때는 __init__ 함수의 정리된 갯수 만큼 값을 넣어야 한다


#              멤버 변수

print("              멤버 변수")
print()

# 클래스 내에서 정리된 변수(self 뒤에 적힌것들)
# 유닛 식 외부에서도 사용 가능

# 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))
print()

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 빼앗음
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))
print()
print()


#              메소드

print("              메소드")
print()

# 유닛에서 정의된 함수

     # 공격 유닛
class AttackUnit:
     def __init__(self, name, hp, damage):
          self.name = name
          self.hp = hp
          self.damage = damage

     def attack(self, location):
          print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
                .format(self.name, location, self.damage))
# self.xxxx 는 유닛 내의 변수 같은것이다
# 위에 location의 경우 함수 attack의 로케이션을 쓰지만,
# self.name의 경우 위에 정의된 self.name을 씀
     def damaged(self, damage):
          print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
          self.hp -= damage
          print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
          if self.hp <= 0:
               print("{0} : 파괴되었습니다".format(self.name))

# 파이어뱃 : 공격 유닛, 화염방사기.
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)
print()
print()


#              상속

print("              상속")
print()

# 메딕 : 의무병, 공격력 없음

# 일반 유닛
class Unit:
     def __init__(self, name, hp):
          self.name = name
          self.hp = hp

# 공격 유닛
class AttackUnit(Unit):
     def __init__(self, name, hp, damage):
          Unit.__init__(self, name, hp)
          self.damage = damage

     def attack(self, location):
          print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 : {2}]"\
                .format(self.name, location, self.damage))

     def damaged(self, damage):
          print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
          self.hp -= damage
          print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
          if self.hp <= 0:
               print("{0} : 파괴되었습니다".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)

# 위에와 동일하게 실행됨
print()
print()


#              다중 상속

print("              다중 상속")
print()

# 부모 클래스(parent class)
class Unit:
     def __init__(self, name, hp):
          self.name = name
          self.hp = hp

# 자식 클래스(child class)
class AttackUnit(Unit):
     def __init__(self, name, hp, damage):
          Unit.__init__(self, name, hp)
          self.damage = damage

     def attack(self, location):
          print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 : {2}]"\
                .format(self.name, location, self.damage))

     def damaged(self, damage):
          print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
          self.hp -= damage
          print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
          if self.hp <= 0:
               print("{0} : 파괴되었습니다".format(self.name))

# 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 들을 수송. 공격 x

# 날수있는 기능을 가진 클래스
class Flyable:
     def __init__(self, flying_speed):
          self.flying_speed = flying_speed

     def fly(self, name, location):
          print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]"\
                .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
     def __init__(self, name, hp, damage, flying_speed):
          AttackUnit.__init__(self, name, hp, damage)
          Flyable.__init__(self, flying_speed)

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일을 발사.
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")
print()
print()


#              연산자 오버로딩

print("              연산자 오버로딩")
print()

# 부모의 메소드가 자식 클래스에서 동일한 이름으로 다시 정의 될시, 자식의 메소드가 쓰인다

class Unit:
     def __init__(self, name, hp, speed):
          self.name = name
          self.hp = hp
          self.speed = speed

     def move(self, location):
          print("[지상 유닛 이동]")
          print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]"\
                .format(self.name, location, self.speed))
          
class AttackUnit(Unit):
     def __init__(self, name, hp, speed, damage):
          Unit.__init__(self, name, hp, speed)
          self.damage = damage

     def attack(self, location):
          print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 : {2}]"\
                .format(self.name, location, self.damage))

     def damaged(self, damage):
          print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
          self.hp -= damage
          print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
          if self.hp <= 0:
               print("{0} : 파괴되었습니다".format(self.name))

class Flyable:
     def __init__(self, flying_speed):
          self.flying_speed = flying_speed

     def fly(self, name, location):
          print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]"\
                .format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
     def __init__(self, name, hp, damage, flying_speed):
          AttackUnit.__init__(self, name, hp, 0, damage) # 지상 스피드 0
          Flyable.__init__(self, flying_speed)

     def move(self, location):
          print("[공중 유닛 이동]")
          self.fly(self.name, location)

# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중 유닛, 체력 굉장히 좋음, 공격력도 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 5)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시") **fly 와 move를 쓰면서 구분해야함**
battlecruiser.move("9시")
# 재정의 된 move() 함수
print()
print()


#              Pass

print("              Pass")
print()

# 건물
class BuildingUnit(Unit):
     def __init__(self, name, hp, location):
          pass

# 서플라이 디폿 : 건물, 1개 건물 = 8 유닛.
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
     print("[알림] 새로운 게임을 시작합니다.")

def game_over():
     pass

game_start()
game_over()

# 미완성된 함수를 오류 없이 넘어감
print()
print()


#              Super

print("              Super")
print()

# 상속받은 클래스에 대해서 초기화가 필요할때는 super().__init__()으로 간편하게 가능

class Unit:
     def __init__(self):
          print("Unit 생성자")

class Flyable:
     def __init__(self):
          print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
     def __init__(self):
          super().__init__()

dropship = FlyableUnit()

# 다중상속을 받았을 경우 super()는 처음 쓰인 부모의 init을 쓴다,
# 따라서 모든 부모의 클래스의 대해서 초기화가 필요하다면 직접 불러서 초기화 해야한다
# Unit.__init__()
# Flyable.__init__()