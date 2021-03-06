## map 함수

- **list(map(함수, 리스트))**
- **tuple(map(함수, 튜플))**

for 반복문을 사용해서 변환

```python
>>> a = [1.2, 2.5, 3.7, 4.6]
>>> for i in range(len(a)):
...     a[i] = int(a[i])
...
>>> a
[1, 2, 3, 4]
```

for에 range(len(a))를 사용해서 인덱스를 가져오고 인덱스로 요소 하나 하나에 접근한 뒤 int로 변환하여 다시 저장했습니다.

매번 for 반복문으로 반복하면서 요소를 변환하려니 조금 번거롭습니다. 이때는 map을 사용하면 편리합니다.

```
>>> a = [1.2, 2.5, 3.7, 4.6]
>>> a = list(map(int, a))
>>> a
[1, 2, 3, 4]
```

a = list(map(int, a)) 한 줄로 변환이 끝났습니다. map에 int와 리스트를 넣으면 리스트의 모든 요소를 int를 사용해서 변환합니다. 그다음에 list를 사용해서 map의 결과를 다시 리스트로 만들어줍니다.

사실 map에는 리스트뿐만 아니라 모든 반복 가능한 객체를 넣을 수 있습니다.
이번에는 range를 사용해서 숫자를 만든 뒤 숫자를 문자열로 변환해보겠습니다.

```python
>>> a = list(map(str, range(10)))
>>> a
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
```

range로 0부터 9까지 숫자를 만들고, str을 이용해서 모두 문자열로 변환했습니다. 리스트를 출력해보면 각 요소가 ' '(작은따옴표)로 묶인 것을 볼 수 있습니다.

### input().split()과 map

지금까지 input().split()으로 값을 여러 개 입력받고 정수, 실수로 변환할 때도 map을 사용했었죠? 사실 input().split()의 결과가 문자열 리스트라서 map을 사용할 수 있었습니다.

다음과 같이 input().split()을 사용한 뒤에 변수 한 개에 저장해보면 리스트인지 확인할 수 있습니다.

```py
>>> a = input().split()
10 20 (입력)
>>> a
['10', '20']
```

10 20을 입력하면 ['10', '20']처럼 문자열 두 개가 들어있는 리스트가 만들어집니다.

이제 map을 사용해서 정수로 변환해봅니다.

```python
>>> a = map(int, input().split())
10 20 (입력)
>>> a
<map object at 0x03DFB0D0>
>>> list(a)
[10, 20]
```

다시 10 20을 입력하면 맵 객체(map object)가 만들어집니다. 이 상태로는 안에 들어있는 값을 볼 수 없으므로 list를 사용해서 리스트로 출력했습니다. 리스트를 보면 [10, 20]처럼 정수 두 개가 들어있습니다.

이 리스트 [10, 20]을 변수 두 개에 저장하면 지금까지 사용한 a, b = map(int, input().split())와 같은 동작이 됩니다.

```python
>>> a, b = [10, 20]
>>> a
10
>>> b
20
```

사실 map이 반환하는 맵 객체는 이터레이터라서 변수 여러 개에 저장하는 언패킹(unpacking)이 가능합니다. 그래서 a, b = map(int, input().split())처럼 list를 생략한 것입니다

a, b = map(int, input().split())을 풀어서 쓰면 다음과 같은 코드가 됩니다.

```python
x = input().split()    # input().split()의 결과는 문자열 리스트
m = map(int, x)        # 리스트의 요소를 int로 변환, 결과는 맵 객체
a, b = m               # 맵 객체는 변수 여러 개에 저장할 수 있음
```