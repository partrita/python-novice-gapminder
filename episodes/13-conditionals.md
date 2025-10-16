---
title: 조건문
teaching: 10
exercises: 15
---

::::::::::::::::::::::::::::::::::::::: objectives

- if 및 else 문과 간단한 부울 표현식(논리 연산자 없이)을 사용하는 프로그램을 올바르게 작성합니다.
- 중첩되지 않은 조건문 및 루프 내부의 조건문 실행을 추적합니다.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- 프로그램이 다른 데이터에 대해 다른 작업을 수행하도록 하려면 어떻게 해야 하나요?

::::::::::::::::::::::::::::::::::::::::::::::::::

## `if` 문을 사용하여 코드 블록 실행 여부를 제어합니다.

- `if` 문(더 정확하게는 *조건문*이라고 함)은 일부 코드 블록이 실행되는지 여부를 제어합니다.
- 구조는 `for` 문과 유사합니다.
  - 첫 번째 줄은 `if`로 시작하고 콜론으로 끝납니다.
  - 하나 이상의 문을 포함하는 본문은 들여쓰기됩니다(보통 4칸).

```python
mass = 3.54
if mass > 3.0:
    print(mass, 'is large')

mass = 2.07
if mass > 3.0:
    print (mass, 'is large')
```

```output
3.54 is large
```

## 조건문은 종종 루프 내부에서 사용됩니다.

- 위와 같이 값을 알 때 조건문을 사용하는 것은 별 의미가 없습니다.
- 그러나 처리할 컬렉션이 있을 때 유용합니다.

```python
masses = [3.54, 2.07, 9.22, 1.86, 1.71]
for m in masses:
    if m > 3.0:
        print(m, 'is large')
```

```output
3.54 is large
9.22 is large
```

## `if` 조건이 참이 *아닐* 때 코드 블록을 실행하려면 `else`를 사용합니다.

- `if` 뒤에 `else`를 사용할 수 있습니다.
- `if` *분기*가 선택되지 않았을 때 실행할 대안을 지정할 수 있습니다.

```python
masses = [3.54, 2.07, 9.22, 1.86, 1.71]
for m in masses:
    if m > 3.0:
        print(m, 'is large')
    else:
        print(m, 'is small')
```

```output
3.54 is large
2.07 is small
9.22 is large
1.86 is small
1.71 is small
```

## 추가 테스트를 지정하려면 `elif`를 사용합니다.

- 각각 고유한 테스트가 있는 여러 대안을 제공하고 싶을 수 있습니다.
- 이를 지정하려면 `elif`("else if"의 줄임말)와 조건을 사용합니다.
- 항상 `if`와 연결됩니다.
- `else`("모든 것을 포괄하는" 것) 앞에 와야 합니다.

```python
masses = [3.54, 2.07, 9.22, 1.86, 1.71]
for m in masses:
    if m > 9.0:
        print(m, 'is HUGE')
    elif m > 3.0:
        print(m, 'is large')
    else:
        print(m, 'is small')
```

```output
3.54 is large
2.07 is small
9.22 is HUGE
1.86 is small
1.71 is small
```

## 조건은 순서대로 한 번 테스트됩니다.

- 파이썬은 조건문의 분기를 순서대로 단계별로 실행하며 각 분기를 차례로 테스트합니다.
- 따라서 순서가 중요합니다.

```python
grade = 85
if grade >= 90:
    print('grade is A')
elif grade >= 80:
    print('grade is B')
elif grade >= 70:
    print('grade is C')
```

```output
grade is B
```

- 값이 변경되면 자동으로 돌아가서 다시 평가하지 *않습니다*.

```python
velocity = 10.0
if velocity > 20.0:
    print('moving too fast')
else:
    print('adjusting velocity')
    velocity = 50.0
```

```output
adjusting velocity
```

- 변수의 값을 "진화"시키기 위해 루프에서 조건문을 자주 사용합니다.

```python
velocity = 10.0
for i in range(5): # 루프를 5번 실행
    print(i, ':', velocity)
    if velocity > 20.0:
        print('moving too fast')
        velocity = velocity - 5.0
    else:
        print('moving too slow')
        velocity = velocity + 10.0
print('final velocity:', velocity)
```

```output
0 : 10.0
moving too slow
1 : 20.0
moving too slow
2 : 30.0
moving too fast
3 : 25.0
moving too fast
4 : 20.0
moving too slow
final velocity: 30.0
```

## 변수 값을 보여주는 표를 만들어 프로그램 실행을 추적합니다.

<table>
  <tr>   <td><strong>i</strong></td>   <td>0</td>   <td>.</td>   <td>1</td>   <td>.</td>   <td>2</td>   <td>.</td>   <td>3</td>   <td>.</td>   <td>4</td>   <td>.</td>
  </tr>
  <tr>   <td><strong>velocity</strong></td>   <td>10.0</td>   <td>20.0</td>   <td>.</td>   <td>30.0</td>   <td>.</td>   <td>25.0</td>   <td>.</td>   <td>20.0</td>   <td>.</td>   <td>30.0</td>
  </tr>
</table>

- 프로그램은 루프 본문 *외부*에 `print` 문이 있어야 최종 `velocity` 값을 표시할 수 있습니다.
  왜냐하면 그 값은 루프의 마지막 반복에 의해 업데이트되기 때문입니다.

:::::::::::::::::::::::::::::::::::::::::  callout

## `and`, `or` 및 괄호를 사용한 복합 관계

종종 어떤 것들의 조합이 참이 되기를 원합니다. `and`와 `or`를 사용하여 조건문 내의 관계를 결합할 수 있습니다. 위의 예제를 계속해서 다음과 같다고 가정합니다.

```python
mass     = [ 3.54,  2.07,  9.22,  1.86,  1.71]
velocity = [10.00, 20.00, 30.00, 25.00, 20.00]

i = 0
for i in range(5):
    if mass[i] > 5 and velocity[i] > 20:
        print("Fast heavy object.  Duck!")
    elif mass[i] > 2 and mass[i] <= 5 and velocity[i] <= 20:
        print("Normal traffic")
    elif mass[i] <= 2 and velocity[i] <= 20:
        print("Slow light object.  Ignore it")
    else:
        print("Whoa!  Something is up with the data.  Check it")
```

산술과 마찬가지로 모호할 수 있는 경우에는 괄호를 사용할 수 있고 사용해야 합니다. 좋은 일반적인 규칙은 동일한 조건에서 `and`와 `or`를 혼합할 때 *항상* 괄호를 사용하는 것입니다. 즉, 다음과 같이 하는 대신:

```python
if mass[i] <= 2 or mass[i] >= 5 and velocity[i] > 20:
```

다음 중 하나를 작성하십시오.

```python
if (mass[i] <= 2 or mass[i] >= 5) and velocity[i] > 20:
if mass[i] <= 2 or (mass[i] >= 5 and velocity[i] > 20):
```

이렇게 하면 독자(그리고 파이썬)에게 당신이 정말로 의미하는 바가 완벽하게 명확해집니다.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 실행 추적

이 프로그램은 무엇을 인쇄합니까?

```python
pressure = 71.9
if pressure > 50.0:
    pressure = 25.0
elif pressure <= 50.0:
    pressure = 0.0
print(pressure)
```

:::::::::::::::  solution

## 해결책

```output
25.0
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 값 다듬기

이 프로그램이 원래 리스트의 값이 음수였던 곳에는 0을, 원래 리스트의 값이 양수였던 곳에는 1을 포함하는 새 리스트를 만들도록 빈칸을 채우십시오.

```python
original = [-1.5, 0.2, 0.4, 0.0, -1.3, 0.4]
result = ____
for value in original:
    if ____:
        result.append(0)
    else:
        ____
print(result)
```

```output
[0, 1, 1, 1, 0, 1]
```

:::::::::::::::  solution

## 해결책

```python
original = [-1.5, 0.2, 0.4, 0.0, -1.3, 0.4]
result = []
for value in original:
    if value < 0.0:
        result.append(0)
    else:
        result.append(1)
print(result)
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 작은 파일 처리

이 프로그램을 수정하여 50개 미만의 레코드가 있는 파일만 처리하도록 하십시오.

```python
import glob
import pandas as pd
for filename in glob.glob('data/*.csv'):
    contents = pd.read_csv(filename)
    ____:
        print(filename, len(contents))
```

:::::::::::::::  solution

## 해결책

```python
import glob
import pandas as pd
for filename in glob.glob('data/*.csv'):
    contents = pd.read_csv(filename)
    if len(contents) < 50:
        print(filename, len(contents))
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 초기화

원래 값의 범위에 관계없이 리스트에서 가장 큰 값과 가장 작은 값을 찾도록 이 프로그램을 수정하십시오.

```python
values = [...some test data...]
smallest, largest = None, None
for v in values:
    if ____:
        smallest, largest = v, v
    ____:
        smallest = min(____, v)
        largest = max(____, v)
print(smallest, largest)
```

데이터의 범위를 찾는 데 이 방법을 사용하는 것의 장점과 단점은 무엇입니까?

:::::::::::::::  solution

## 해결책

```python
values = [-2,1,65,78,-54,-24,100]
smallest, largest = None, None
for v in values:
    if smallest is None and largest is None:
        smallest, largest = v, v
    else:
        smallest = min(smallest, v)
        largest = max(largest, v)
print(smallest, largest)
```

`== None` 대신 `is None`을 작성했다면 그것도 작동하지만, 파이썬 프로그래머는 `None`이 언어에서 작동하는 특별한 방식 때문에 항상 `is None`을 작성합니다.

이 방법을 사용하는 장점은 코드를 더 읽기 쉽게 만드는 것이라고 주장할 수 있습니다.
그러나 단점은 `for` 루프 문의 각 반복 내에 각각 두 개의 숫자에 대해 실행되는 두 개의 루프( `min` 및 `max` 함수)가 더 있기 때문에 이 코드가 효율적이지 않다는 것입니다. 각 숫자를 한 번만 반복하는 것이 더 효율적입니다.

```python
values = [-2,1,65,78,-54,-24,100]
smallest, largest = None, None
for v in values:
    if smallest is None or v < smallest:
        smallest = v
    if largest is None or v > largest:
        largest = v
print(smallest, largest)
```

이제 하나의 루프가 있지만 네 개의 비교 테스트가 있습니다. 더 개선할 수 있는 두 가지 방법이 있습니다.
각 반복에서 비교를 더 적게 사용하거나, 각각 하나의 비교 테스트만 포함하는 두 개의 루프를 사용합니다.
가장 간단한 해결책이 종종 최선입니다.

```python
values = [-2,1,65,78,-54,-24,100]
smallest = min(values)
largest = max(values)
print(smallest, largest)
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- `if` 문을 사용하여 코드 블록 실행 여부를 제어합니다.
- 조건문은 종종 루프 내부에서 사용됩니다.
- `if` 조건이 참이 *아닐* 때 코드 블록을 실행하려면 `else`를 사용합니다.
- 추가 테스트를 지정하려면 `elif`를 사용합니다.
- 조건은 순서대로 한 번 테스트됩니다.
- 변수 값을 보여주는 표를 만들어 프로그램 실행을 추적합니다.

::::::::::::::::::::::::::::::::::::::::::::::::::