## 스크립트 vs 모듈

> ### 스크립트란?

스크립트는 __프로그램을 작동시키는 코드__를 담은 실행 파일

> ### 모듈이란?

모듈은 프로그램에 __필요한 코드를 정의__해 놓은, import 용도의 파일이며,
함수들을 정의하기만 하고 함수를 사용하지는 않는다.

```python
# 함수가 정의 되어 있는 모듈 area.py

PI = 3.14

def square(length):
    return length * length
```

```python
# 모듈을 import하여 사용하는 스크립트 run.py

x = float(input('정사각형 변의 길이를 입력하시오 : '))
print(f"변의 길이가 {x}인 정사각형의 면적은 : {area.square(x)})
```

* 사실 스크립트와 모듈은 그 안에 담을 내용을 정의한 것이지 파일 자체에 특별한 차이가 있는 것은 아니다. 어떤 파이썬 파일이든 직접 실행할 수 있고 불러올 수 있다.

---

> ### name이란?

`__name__`은 모듈의 이름을 저장해 놓은 변수이다.

* 파일을 직접 실행하면 `__name__`은 `__main__`으로 설정된다.
* 파일을 import하면 `__name__`은 모듈 이름으로 설정된다.
  

> #### `if __name__ == '__main__'`

해당 조건을 이용하면

* 파일이 직접 실행될 때만 실행할 수 있다.

```python
# area.py

PI = 3.14 

# 정사각형의 면적을 구해 주는 함수
def square(length):
    return length * length

if __name__ == '__main__':

    # square 함수 테스트
    print(square(2) == 4)
    print(square(5) == 25)
```

해당 파일을 직접 실행시키면 파일의 \_\_name\__ 은 \_\_main__이 되기 때문에 조건문 안의 코드가 실행되지만,
 다른 파일에서 import해서 사용할 경우 \_\_name\_\_이 area가 되기 때문에 조건문 안의 코드가 실행되지 않는다. 