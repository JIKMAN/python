## 클래스의 성질

![class](../img/class.jpg)

> ## 추상화(Abstraction)

사용에 꼭 필요한 정보만 드러는 것.
즉, 필수적인 사항을 제외한 복잡한 내부 사항을 가리는 것 변수, 함수, 클래스 모두 추상화의 예시라고 할 수 있다. 
예를들어 append 함수의 경우 내부적으로 어떠한 로직이 있지만, 그 구조를 몰라도 사용할 수 있다.



> ## 캡슐화(Encapsulation)

1. 객체의 일부 구현 내용에 대한 외부로부터의 직접적인 엑세스를 차단하는 것

2. 객체의 속성과 그것을 사용하는 행동을 하나로 묶는 것

* __age 변수를 외부에서 접근할 수는 없지만 can_drink, get_age, set_age 메소드를 통해 가려진 __age 변수에 접근할 수 있다.

* **즉, 캡슐화된 변수에 접근할 수 있는 메소드를 만드는 것!**

  ```python
  class Citizen:
      """주민 클래스"""
      drinking_age = 19  # 음주 가능 나이
      
      def __init__(self, name, age, resident_id):
          """이름, 나이, 주민번호"""
          self.name = name
          self.__age = age
          self.__resident_id = resident_id
      ## 인스턴트 변수앞에 __를 설정하면 캡슐화가 적용되어 값은 저장되나 외부로 보여지지 않음.
      
      def authenticate(self, id_field):
          """본인이 맞는지 확인하는 메소드"""
          return self.__resident_id == id_field
      
      def can_drink(self):
          """음주 가능 나이인지 확인하는 메소드"""
          return self.__age >= Citizen.drinking_age
      
      def __str__(self):
          """주민 정보를 문자열로 리터낳는 메소드"""
          return f"{self.name}씨는 {str(self.__age)}살입니다."
      
      def get_age(self): # getter 메소드 - 변수의 값을 읽음
          return self.__age
      
      def set_age(self, value): # setter 메소드 - 변수의 값을 설정함
          if value < 0:
              print("나이는 0보다 작을 수 없습니다. 기본 값 0으로 나이를 설정합니다.")
          else:
              self.__age = value
  ```

  

> ## 상속

* 두 클래스 사이에 __부모-자식 관계__를 설정해서

- 부모 클래스의 변수, 메소드를 자식 클래스가 그대로 물려받아 사용할 수 있게 하는 것

### **오버라이딩**

- 부모클래스에게서 상속받은 메소드를 자식클래스가 자신의 클래스에 맞게 내용을 바꿔 정의하는 것

```python
#부모 클래스 설정
class Employee:
    """전체 직원 클래스"""
    company_name = "맥도날드" # 가게 이름
    raise_percentage = 1.05 # 시급 인상률3
    
    def __init__(self, name, wage):
        self.name = name # 이름
        self.wage = wage # 시급
        
    def raise_pay(self):
        """시급을 인상한다"""
        self.wage *= Employee.raise_percentage
        
    def __str__(self):
        return Employee.company_name + " 직원: " + self.name

class Cashier(Employee): # Employee 클래스를 상속!
    raise_percentage = 1.1 # 변수를 새로 지정
    
    def __init__(self, name, wage, number_sold = 0):
        # Employee.__init__(self, name, wage)
        super().__init__(name, wage)
        # 부모클래스를 상속받을때 super()함수로 사용가능, 이때는 self가 필요없음.
        self.number_sold = number_sold
    
#     def raise_pay(self): # 부모 클래스에서 상속받아서 쓰기 때문에 안써도됌
#         self.wage *= Cashier.raise_percentage
        
    def take_order(self, money_received): 
        """주문과 돈을 받고 거스름돈을 리턴한다"""
        if Cashier.burger_price > money_received:
            print('돈이 충분하지 않습니다.')
            return money_received
        else:
            self.number_sold += 1
            change = money_received - Cashier.burger_price
            return change
    
#     def __str__(self): # 상속받음
#         return Employee.company_name + "  직원: " + self.name

```



> ## 다형성(Polymorphism)

- 같은 모양의 코드가 다른 동작을 하는 것
- 키보드의 예로
  - push(keyboard): 키보드를 누룬다는 동일한 코드에 대해
    - ENTER, ESC, A 등 실제 키에 따라 동작이 다른 것을 의미함
- 다형성은 코드의 양을 줄이고, 여러 객체 타입을 하나의 타입으로 관리가 가능하여 유지보수에 좋음

```python
# 클래스 선언
class Person:
    def __init__(self, name):
        self.name = name

    def work(self):
        print (self.name + " works hard")        

class Student(Person):
    def work(self):
        print (self.name + " studies hard")

class Engineer(Person):
    def work(self):
        print (self.name + " develops something")     
        
# 객체 생성
student1 = Student("Dave")
developer1 = Engineer("David")
student1.work()
developer1.work()

----------------------------------------

>>> Dave studies hard
>>>David develops something
```



> ## 추상클래스

- 여러 클래스들의 공통점을 추상화 해서 모아놓은 클래스

추상클래스를 상속 받은 자식 클래스의 경우

##### 추상클래스의 자식클래스들은 추상메소드 사용시 반드시 오버라이딩 하도록 강제화된다.

- 추상클래스는 최소 한개 이상의 추상 메소드를 가지고 있어야한다.
- 추상클래스는 인스턴스를 가질 수 없다.
- 추상클래스도 일반메서드를 만들 수 있다.

```python
from math import sqrt
from abc import ABC, abstractmethod # 추상클래스 선언하기 위한 라이브러리

class Shape(ABC): # 추상클래스 설정
    """도형 클래스"""
    @abstractmethod # 추상메소드 설정
    def area(self) -> float:
        """도형의 넓이를 리턴한다: 자식 클래스가 반드시 오버라이딩 할 것"""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """도형의 둘레를 리턴한다: 자식 클래스가 반드시 오버라이딩할 것"""
        pass
    
    def larger_than(self, shape): # 추상 클래스의 일반 메소드
        """해당 인스턴스의 넓이가 파라미터 인스턴스의 넓이보다 큰지를 불린으로 나타낸다"""
        return self.area() > shape.area()
    
    
class Paint:
    """그림판 프로그램 클래스"""
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape : Shape): 
        # Shape 클래스의 인스턴스만 파라미터로 가져올 수 있도록 추상화 !
        """도형 인스턴스만 그림판에 추가한다"""
        if isinstance(shape, Shape):
            self.shapes.append(shape)
        else:
            print("도형 클래스가 아닌 인스턴스는 추가할 수 없습니다!")

    def total_area_of_shapes(self):
        """그림판에 있는 모든 도형의 넓이의 합을 구한다"""
        return sum([shape.area() for shape in self.shapes])

    def total_perimeter_of_shapes(self):
        """그림판에 있는 모든 도형의 둘레의 합을 구한다"""
        return sum([shape.perimeter() for shape in self.shapes])

    
class RightTriangle(Shape):   # 추상클래스를 상속받은 자식 클래스
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return self.base * self.height / 2
        
    def perimeter(self):
        return sqrt(self.base**2 + self.height**2) + self.base + self.height
    
class Circle(Shape):  # 추상클래스를 상속받은 자식 클래스
    """원 클래스"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """원의 넓이를 리턴한다"""
        return pi * self.radius * self.radius

    def perimeter(self):
        """원의 둘레를 리턴한다"""
        return 2 * pi * self.radius
    
right_triangle_1 = RightTriangle(3, 4)
right_triangle_2 = RightTriangle(5, 12)
right_triangle_3 = RightTriangle(6, 8)

paint_program = Paint()

paint_program.add_shape(right_triangle_1)
paint_program.add_shape(right_triangle_2)
paint_program.add_shape(right_triangle_3)

print(paint_program.total_area_of_shapes())
print(paint_program.total_perimeter_of_shapes())

--------------------------------------------

>>> 60.0
>>> 66.0
```

* 추상 메소드에 내용을 추가할수도 있다.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    """도형 클래스"""
    @abstractmethod
    def area(self) -> float:
        """도형의 넓이를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        print("도형의 넓이 계산 중!")   # ---------------- 추가된 코드
        
class Rectangle(Shape):
    """직사각형 클래스"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """직사각형의 넓이를 리턴한다"""
        super().area() # ---------------- 부모의 메소드를 가져다 씀
        return self.width * self.height

rectangle = Rectangle(3, 4)
print(rectangle.area())
    
-----------------------------------------------

>>> 도형의 넓이 계산 중!
>>> 12
```



### 추상클래스에서의 다중상속

* 일반클래스에서는 함수가 겹치는 경우 의도한대로 되지 않을 경우가 있어 다중상속을 잘 사용하지 않지만,

- 자식클래스에서 추상메소드를 반드시 오버라이딩 해야되기 때문에 겹칠 문제가 없다. 따라서 추상클래스에서의 다중상속은 자주 쓰이는 방법이다.

```python
from abc import ABC, abstractmethod

class Message(ABC):
    @abstractmethod
    def print_message(self) -> None:
        pass
    @abstractmethod
    def send(self, destination: str) -> None:  # ----- 중복되는 추상 메소드
        pass

class Sendable(ABC):
    @abstractmethod
    def send(self, destination: str) -> None:
        pass

class Email(Message, Sendable): # 추상클래스 다중 상속을 받았음, 오버라이딩 해야함.
    def __init__(self, content, user_email):
        self.content = content
        self.user_email = user_email

    def print_message(self):
        print("이메일 내용입니다:\n{}".format(self.content))

    def send(self, destination):
        print("이메일을 주소 {}에서 {}로 보냅니다!".format(self.user_email, destination))
        
# 이메일 인스턴스를 생성한다.
email = Email("안녕? 오랜만이야 잘 지내니?", "young@codeit.kr")

# 메시지 내용 출력
email.print_message()
# 메시지 전송
email.send("captain@codeit.kr")

-----------------------------------------------------

>>> 이메일 내용입니다:
>>> 안녕? 오랜만이야 잘 지내니?
>>> 이메일을 주소 young@codeit.kr에서 captain@codeit.kr로 보냅니다!

```



## 함수, 메소드 다형성

- 하나의 메소드로 여러 파라미터를 가질 수 있다.

1. 옵셔널 파라미터를 정의

- 이 경우 옵셔널 파라미터를 가장 뒤에 정의해야 함.

```python
def new_print(v1, v2=None, v3=None): # optional 파라미터를 정의
    if v3 is None:
        if v2 is None:
            print(v1)
        else:
            print(f'{v1} {v2}')
    else:
        print(f'{v1} {v2} {v3}')

new_print('alpha')
new_print('alpha', 'beta')
new_print('alpha', 'beta', 'omega')
new_print('this', 100)

--------------------------------------------
>>> alpha
>>> alpha beta
>>> alpha beta omega
>>> this 100
```

2. 파라미터 이름을 명시

```python
def print_name(first_name, last_name, email=""):
    print(f'{last_name}{first_name} {email}')

print_name('흥민', '손', 'hm@naver.com')
print_name(last_name='손', email='hm@naver.com', first_name='흥민')

------------------------------------------

>>> 손흥민 hm@naver.com
>>> 손흥민 hm@naver.com
```

3. 개수가 확정되지 않은 파라미터

```python
def add_numbers(message, *numbers): # * 한개는 튜플형태, **는 딕셔너리 형태
    print(message)
    return sum(numbers)

print(add_numbers('test1', 7, 3, 5)) # 파라미터 여러개가 들어갈 수 있음
print(add_numbers('test1', 7, 3, 5, 11))
print(add_numbers('test1', 2, 2))

def add_names(message, **names): # * 한개는 튜플형태, **는 딕셔너리 형태
    print(message)
    return (names)

print(add_names('친구사전', cheolsu='철수', younghee='영희'))

dict_names = {'사과' : 'apple', '오렌지' : 'orange'}
print(add_names('과일사전', **dict_names))

-------------------------------------------------

test1
15
test1
26
test1
4
친구사전
{'cheolsu': '철수', 'younghee': '영희'}
과일사전
{'사과': 'apple', '오렌지': 'orange'}

```



