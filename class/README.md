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

