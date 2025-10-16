---
title: 변수 범위
teaching: 10
exercises: 10
---

::::::::::::::::::::::::::::::::::::::: objectives

- 지역 변수와 전역 변수를 식별합니다.
- 매개변수를 지역 변수로 식별합니다.
- 트레이스백을 읽고 오류가 발생한 파일, 함수, 줄 번호, 오류 유형 및 오류 메시지를 확인합니다.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- 함수 호출은 실제로 어떻게 작동합니까?
- 오류가 발생한 위치를 어떻게 확인할 수 있습니까?

::::::::::::::::::::::::::::::::::::::::::::::::::

## 변수의 범위는 해당 변수를 '볼' 수 있는 프로그램의 일부입니다.

- 변수에 대한 합리적인 이름은 그리 많지 않습니다.
- 함수를 사용하는 사람들은 함수 작성자가 사용한 변수 이름에 대해 걱정할 필요가 없습니다.
- 함수를 작성하는 사람들은 함수 호출자가 사용하는 변수 이름에 대해 걱정할 필요가 없습니다.
- 변수가 보이는 프로그램의 부분을 *범위*라고 합니다.

```python
pressure = 103.9

def adjust(t):
    temperature = t * 1.43 / pressure
    return temperature
```

- `pressure`는 *전역 변수*입니다.
  - 특정 함수 외부에서 정의됩니다.
  - 어디에서나 볼 수 있습니다.
- `t`와 `temperature`는 `adjust`의 *지역 변수*입니다.
  - 함수에 정의되어 있습니다.
  - 주 프로그램에서는 보이지 않습니다.
  - 기억하십시오: 함수 매개변수는 함수가 호출될 때 자동으로 값이 할당되는 변수입니다.

```python
print('adjusted:', adjust(0.9))
print('temperature after call:', temperature)
```

```output
adjusted: 0.01238691049085659
```

```error
Traceback (most recent call last):
  File "/Users/swcarpentry/foo.py", line 8, in <module>
    print('temperature after call:', temperature)
NameError: name 'temperature' is not defined
```

:::::::::::::::::::::::::::::::::::::::  challenge

## 지역 및 전역 변수 사용

이 프로그램이 실행될 때 모든 변수의 값을 추적하십시오.
(변수가 존재하기 전과 후에 변수 값으로 '---'를 사용하십시오.)

```python
limit = 100

def clip(value):
    return min(max(0.0, value), limit)

value = -22.5
print(clip(value))
```

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 오류 메시지 읽기

아래 트레이스백을 읽고 다음을 식별하십시오.

1. 트레이스백에는 몇 개의 수준이 있습니까?
2. 오류가 발생한 파일 이름은 무엇입니까?
3. 오류가 발생한 함수 이름은 무엇입니까?
4. 이 함수에서 오류가 발생한 줄 번호는 무엇입니까?
5. 오류 유형은 무엇입니까?
6. 오류 메시지는 무엇입니까?

```error
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-2-e4c4cbafeeb5> in <module>()
      1 import errors_02
----> 2 errors_02.print_friday_message()

/Users/ghopper/thesis/code/errors_02.py in print_friday_message()
     13
     14 def print_friday_message():
---> 15     print_message("Friday")

/Users/ghopper/thesis/code/errors_02.py in print_message(day)
      9         "sunday": "Aw, the weekend is almost over."
     10     }
---> 11     print(messages[day])
     12
     13

KeyError: 'Friday'
```

:::::::::::::::  solution

## 해결책

1. 세 가지 수준.
2. `errors_02.py`
3. `print_message`
4. 11번 줄
5. `KeyError`. 이러한 오류는 존재하지 않는 키를 찾으려고 할 때 발생합니다(일반적으로 사전과 같은 데이터 구조에서). `KeyError` 및 기타 내장 예외에 대한 자세한 정보는 [파이썬 문서](https://docs.python.org/3/library/exceptions.html#KeyError)에서 찾을 수 있습니다.
6. `KeyError: 'Friday'`
  
:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- 변수의 범위는 해당 변수를 '볼' 수 있는 프로그램의 일부입니다.

::::::::::::::::::::::::::::::::::::::::::::::::::