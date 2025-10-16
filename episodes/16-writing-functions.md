---
title: 함수 작성하기
teaching: 10
exercises: 15
---

::::::::::::::::::::::::::::::::::::::: objectives

- 함수 정의와 함수 호출의 차이점을 설명하고 식별합니다.
- 작고 고정된 수의 인수를 받아 단일 결과를 생성하는 함수를 작성합니다.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- 나만의 함수는 어떻게 만들 수 있나요?

::::::::::::::::::::::::::::::::::::::::::::::::::

## 프로그램을 함수로 나누어 이해하기 쉽게 만듭니다.

- 인간은 한 번에 몇 개의 항목만 작업 메모리에 유지할 수 있습니다.
- 조각을 이해하고 결합하여 더 크고 복잡한 아이디어를 이해합니다.
  - 기계의 부품.
  - 정리를 증명할 때의 보조 정리.
- 함수는 프로그램에서 동일한 목적을 수행합니다.
  - 복잡성을 *캡슐화*하여 단일 "사물"로 취급할 수 있도록 합니다.
- 또한 *재사용*을 가능하게 합니다.
  - 한 번 작성하고 여러 번 사용합니다.

## `def`를 사용하여 이름, 매개변수 및 코드 블록으로 함수를 정의합니다.

- `def`로 새 함수 정의를 시작합니다.
- 함수 이름이 뒤따릅니다.
  - 변수 이름과 동일한 규칙을 따라야 합니다.
- 그런 다음 괄호 안에 *매개변수*가 옵니다.
  - 함수가 입력을 받지 않으면 빈 괄호입니다.
  - 잠시 후에 자세히 설명하겠습니다.
- 그런 다음 콜론이 옵니다.
- 그런 다음 들여쓰기된 코드 블록이 옵니다.

```python
def print_greeting():
    print('Hello!')
    print('The weather is nice today.')
    print('Right?')
```

## 함수를 정의해도 실행되지는 않습니다.

- 함수를 정의해도 실행되지는 않습니다.
  - 변수에 값을 할당하는 것과 같습니다.
- 함수에 포함된 코드를 실행하려면 함수를 호출해야 합니다.

```python
print_greeting()
```

```output
Hello!
```

## 함수 호출의 인수는 정의된 매개변수와 일치합니다.

- 함수는 다른 데이터에서 작동할 수 있을 때 가장 유용합니다.
- 함수를 정의할 때 *매개변수*를 지정합니다.
  - 함수가 실행될 때 변수가 됩니다.
  - 호출의 인수에 할당됩니다(즉, 함수에 전달된 값).
  - 호출에서 인수를 사용할 때 이름을 지정하지 않으면 인수는 함수에 정의된 순서대로 매개변수와 일치합니다.

```python
def print_date(year, month, day):
    joined = str(year) + '/' + str(month) + '/' + str(day)
    print(joined)

print_date(1871, 3, 19)
```

```output
1871/3/19
```

또는 함수를 호출할 때 인수의 이름을 지정할 수 있습니다. 이렇게 하면
순서에 상관없이 지정할 수 있고 호출 사이트에 명확성을 더합니다. 그렇지 않으면
코드를 읽는 동안 두 번째 인수가 월인지 일인지 잊어버릴 수 있습니다.

```python
print_date(month=3, day=19, year=1871)
```

```output
1871/3/19
```

- [트위터](https://twitter.com/minisciencegirl/status/693486088963272705)를 통해:
  `()`에는 함수의 재료가 포함되어 있고
  본문에는 레시피가 포함되어 있습니다.

## 함수는 `return`을 사용하여 호출자에게 결과를 반환할 수 있습니다.

- `return ...`을 사용하여 호출자에게 값을 반환합니다.
- 함수 어디에서나 발생할 수 있습니다.
- 그러나 `return`이 다음과 같은 경우 함수를 이해하기가 더 쉽습니다.
  - 특수한 경우를 처리하기 위해 처음에.
  - 최종 결과와 함께 맨 끝에.

```python
def average(values):
    if len(values) == 0:
        return None
    return sum(values) / len(values)
```

```python
a = average([1, 3, 4])
print('average of actual values:', a)
```

```output
average of actual values: 2.6666666666666665
```

```python
print('average of empty list:', average([]))
```

```output
average of empty list: None
```

- 기억하십시오: [모든 함수는 무언가를 반환합니다](04-built-in.md).
- 명시적으로 값을 `return`하지 않는 함수는 자동으로 `None`을 반환합니다.

```python
result = print_date(1871, 3, 19)
print('result of call is:', result)
```

```output
1871/3/19
result of call is: None
```

:::::::::::::::::::::::::::::::::::::::  challenge

## 구문 오류 식별

1. 아래 코드를 읽고 실행하지 않고 오류가 무엇인지 확인해 보십시오.
2. 코드를 실행하고 오류 메시지를 읽으십시오.
  `SyntaxError`입니까, 아니면 `IndentationError`입니까?
3. 오류를 수정하십시오.
4. 모든 오류를 수정할 때까지 2단계와 3단계를 반복하십시오.

```python
def another_function
  print("Syntax errors are annoying.")
   print("But at least python tells us about them!")
  print("So they are usually not too hard to fix.")
```

:::::::::::::::  solution

## 해결책

```python
def another_function():
  print("Syntax errors are annoying.")
  print("But at least Python tells us about them!")
  print("So they are usually not too hard to fix.")
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 정의 및 사용

다음 프로그램은 무엇을 인쇄합니까?

```python
def report(pressure):
    print('pressure is', pressure)

print('calling', report, 22.5)
```

:::::::::::::::  solution

## 해결책

```output
calling <function report at 0x7fd128ff1bf8> 22.5
```

함수 호출에는 항상 괄호가 필요하며, 그렇지 않으면 함수 객체의 메모리 주소를 얻게 됩니다. 따라서 report라는 함수를 호출하고 보고할 값 22.5를 제공하려면 함수 호출을 다음과 같이 할 수 있습니다.

```python
print("calling")
report(22.5)
```

```output
calling
pressure is 22.5
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 연산 순서

1. 이 예제에서 무엇이 잘못되었습니까?
  
  ```python
  result = print_time(11, 37, 59)
  
  def print_time(hour, minute, second):
     time_string = str(hour) + ':' + str(minute) + ':' + str(second)
     print(time_string)
  ```

2. 위의 문제를 수정한 후 이 예제 코드를 실행하면
  
  ```python
  result = print_time(11, 37, 59)
  print('result of call is:', result)
  ```
  
  이 출력이 나오는 이유를 설명하십시오.
  
  ```output
  11:37:59
  result of call is: None
  ```

3. 호출 결과가 `None`인 이유는 무엇입니까?

:::::::::::::::  solution

## 해결책

1. 예제의 문제는 `print_time()` 함수가 함수 호출 *이후에* 정의되었다는 것입니다. 파이썬은 `print_time` 이름이 아직 정의되지 않았기 때문에 해결하는 방법을 모르고 `NameError`를 발생시킵니다. 예: `NameError: name 'print_time' is not defined`

2. 출력의 첫 번째 줄 `11:37:59`는 `print_time`을 호출하여 반환된 값을 변수 `result`에 바인딩하는 코드의 첫 번째 줄 `result = print_time(11, 37, 59)`에 의해 인쇄됩니다. 두 번째 줄은 `result` 변수의 내용을 인쇄하기 위한 두 번째 인쇄 호출에서 온 것입니다.

3. `print_time()`은 명시적으로 값을 `return`하지 않으므로 자동으로 `None`을 반환합니다.

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 캡슐화

단일 파일 이름을 인수로 받아 해당 인수로 이름이 지정된 파일의 데이터를 로드하고 해당 데이터의 최소값을 반환하는 함수를 만들도록 빈칸을 채우십시오.

```python
import pandas as pd

def min_in_data(____):
    data = ____
    return ____
```

:::::::::::::::  solution

## 해결책

```python
import pandas as pd

def min_in_data(filename):
    data = pd.read_csv(filename)
    return data.min()
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 첫 번째 찾기

숫자 목록을 인수로 받아 목록의 첫 번째 음수 값을 반환하는 함수를 만들도록 빈칸을 채우십시오.
목록이 비어 있으면 함수는 어떻게 합니까? 목록에 음수가 없으면 어떻게 합니까?

```python
def first_negative(values):
    for v in ____:
        if ____:
            return ____
```

:::::::::::::::  solution

## 해결책

```python
def first_negative(values):
    for v in values:
        if v < 0:
            return v
```

이 함수에 빈 목록이나 모든 양수 값이 있는 목록이 전달되면 `None`을 반환합니다.

```python
my_list = []
print(first_negative(my_list))
```

```output
None
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 이름으로 호출

앞서 이 함수를 보았습니다.

```python
def print_date(year, month, day):
    joined = str(year) + '/' + str(month) + '/' + str(day)
    print(joined)
```

다음과 같이 *명명된 인수*를 사용하여 함수를 호출할 수 있음을 보았습니다.

```python
print_date(day=1, month=2, year=2003)
```

1. `print_date(day=1, month=2, year=2003)`는 무엇을 인쇄합니까?
2. 이와 같은 함수 호출을 이전에 어디에서 보았습니까?
3. 이 방법으로 함수를 호출하는 것이 언제 그리고 왜 유용합니까?

:::::::::::::::  solution

## 해결책

1. `2003/2/1`
2. 판다스 라이브러리로 작업할 때 *명명된 인수*를 사용하는 예를 보았습니다. 예를 들어 `data = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')`를 사용하여 데이터 세트를 읽을 때 마지막 인수 `index_col`은 명명된 인수입니다.
3. 명명된 인수를 사용하면 함수 내에서 다른 인수가 어떤 이름을 갖는지 함수 호출에서 볼 수 있으므로 코드를 더 읽기 쉽게 만들 수 있습니다. 또한 명명된 인수를 사용하면 순서가 중요하지 않으므로 잘못된 순서로 인수를 전달할 가능성을 줄일 수 있습니다.
  
:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## If/Print 블록 캡슐화

아래 코드는 계란 라벨 프린터에서 실행됩니다. 디지털 저울이 컴퓨터에 계란 질량(그램)을 보고하면 컴퓨터가 라벨을 인쇄합니다.

```python
import random
for i in range(10):

    # 계란 질량 시뮬레이션
    # (무작위) 질량은 70 +/- 20그램입니다.
    mass = 70 + 20.0 * (2.0 * random.random() - 1.0)

    print(mass)

    # 계란 크기 조정 기계가 라벨을 인쇄합니다.
    if mass >= 85:
        print("jumbo")
    elif mass >= 70:
        print("large")
    elif mass < 70 and mass >= 55:
        print("medium")
    else:
        print("small")
```

계란을 분류하는 if-block은 다른 상황에서도 유용할 수 있으므로 반복을 피하기 위해 `get_egg_label()` 함수에 포함시킬 수 있습니다.
프로그램을 수정하여 함수를 사용하면 다음과 같이 됩니다.

```python
# 수정된 버전
import random
for i in range(10):

    # 계란 질량 시뮬레이션
    # (무작위) 질량은 70 +/- 20그램입니다.
    mass = 70 + 20.0 * (2.0 * random.random() - 1.0)

    print(mass, get_egg_label(mass))

```

1. 위의 수정된 프로그램과 함께 작동할 `get_egg_label()`에 대한 함수 정의를 만드십시오. `get_egg_label()` 함수의 반환 값이 중요합니다. 위 프로그램의 샘플 출력은 `71.23 large`입니다.
2. 더러운 계란은 90그램 이상일 수 있으며, 상하거나 깨진 계란은 아마도 50그램 미만일 것입니다. 이러한 오류 조건을 고려하도록 `get_egg_label()` 함수를 수정하십시오. 샘플 출력은 `25 too light, probably spoiled`일 수 있습니다.

:::::::::::::::  solution

## 해결책

```python
def get_egg_label(mass):
    # 계란 크기 조정 기계가 라벨을 인쇄합니다.
    egg_label = "Unlabelled"
    if mass >= 90:
        egg_label = "warning: egg might be dirty"
    elif mass >= 85:
        egg_label = "jumbo"
    elif mass >= 70:
        egg_label = "large"
    elif mass < 70 and mass >= 55:
        egg_label = "medium"
    elif mass < 50:
        egg_label = "too light, probably spoiled"
    else:
        egg_label = "small"
    return egg_label
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 데이터 분석 캡슐화

다음 코드가 실행되었다고 가정합니다.

```python
import pandas as pd

data_asia = pd.read_csv('data/gapminder_gdp_asia.csv', index_col=0)
japan = data_asia.loc['Japan']
```

1. 1980년대에 보고된 연도에 대한 일본의 평균 GDP를 얻으려면 아래 문을 완성하십시오.
  
  ```python
  year = 1983
  gdp_decade = 'gdpPercap_' + str(year // ____)
  avg = (japan.loc[gdp_decade + ___] + japan.loc[gdp_decade + ___]) / 2
  ```

2. 위의 코드를 단일 함수로 추상화하십시오.
  
  ```python
  def avg_gdp_in_decade(country, continent, year):
      data_countries = pd.read_csv('data/gapminder_gdp_'+___+'.csv',delimiter=',',index_col=0)
      ____
      ____
      ____
      return avg
  ```

3. 데이터에 어떤 특정 연도가 열로 나타나는지 미리 알지 못했다면 이 함수를 어떻게 일반화하시겠습니까?
  예를 들어, 각 10년 동안 1과 9로 끝나는 연도의 데이터도 있었다면 어떻게 하시겠습니까?
  (힌트: 코드에서 열거하는 대신 열을 사용하여 10년에 해당하는 열을 필터링하십시오.)

:::::::::::::::  solution

## 해결책

1. 1980년대에 보고된 연도에 대한 일본의 평균 GDP는 다음과 같이 계산됩니다.
  
  ```python
  year = 1983
  gdp_decade = 'gdpPercap_' + str(year // 10)
  avg = (japan.loc[gdp_decade + '2'] + japan.loc[gdp_decade + '7']) / 2
  ```

2. 해당 코드를 함수로 만들면 다음과 같습니다.
  
  ```python
  def avg_gdp_in_decade(country, continent, year):
      data_countries = pd.read_csv('data/gapminder_gdp_' + continent + '.csv', index_col=0)
      c = data_countries.loc[country]
      gdp_decade = 'gdpPercap_' + str(year // 10)
      avg = (c.loc[gdp_decade + '2'] + c.loc[gdp_decade + '7'])/2
      return avg
  ```

3. 관련 연도의 평균을 얻으려면 반복해야 합니다.
  
  ```python
  def avg_gdp_in_decade(country, continent, year):
      data_countries = pd.read_csv('data/gapminder_gdp_' + continent + '.csv', index_col=0)
      c = data_countries.loc[country]
      gdp_decade = 'gdpPercap_' + str(year // 10)
      total = 0.0
      num_years = 0
      for yr_header in c.index: # c의 인덱스에는 보고된 연도가 포함됩니다.
          if yr_header.startswith(gdp_decade):
              total = total + c.loc[yr_header]
              num_years = num_years + 1
      return total/num_years
  ```

이제 함수를 다음과 같이 호출할 수 있습니다.

```python
avg_gdp_in_decade('Japan','asia',1983)
```

```output
20880.023800000003
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 동적 시스템 시뮬레이션

수학에서 [동적 시스템](https://en.wikipedia.org/wiki/Dynamical_system)은 함수가 기하학적 공간에서 한 점의 시간 의존성을 설명하는 시스템입니다.
동적 시스템의 정식 예는 현재 밀도를 기반으로 새로운 인구 밀도(0과 1 사이)를 계산하는 성장 모델인 [로지스틱 맵](https://en.wikipedia.org/wiki/Logistic_map)입니다.
모델에서 시간은 0, 1, 2, ...와 같은 이산 값을 가집니다.

1. 현재 인구(시간 `t`에서)를 나타내는 `x`와 매개변수 `r = 1`의 두 입력을 받는 `logistic_map`이라는 함수를 정의하십시오. 이 함수는 매핑 함수를 사용하여 시간 `t + 1`에서 시스템의 상태(인구)를 나타내는 값을 반환해야 합니다.
  
  `f(t+1) = r * f(t) * [1 - f(t)]`

2. `for` 또는 `while` 루프를 사용하여 1부에서 정의한 `logistic_map` 함수를 초기 인구 0.5에서 시작하여 `t_final = 10`의 기간 동안 반복하십시오. 중간 결과를 목록에 저장하여 루프가 종료된 후 `t = [0,1,...,t_final]`(총 11개 값) 시간에 로지스틱 맵의 상태를 나타내는 값 시퀀스를 누적하도록 하십시오.
  인구의 진화를 보려면 이 목록을 인쇄하십시오.

3. 루프의 논리를 초기 인구를 첫 번째 입력으로, 매개변수 `t_final`을 두 번째 입력으로, 매개변수 `r`을 세 번째 입력으로 받는 `iterate`라는 함수로 캡슐화하십시오. 이 함수는 `t = [0,1,...,t_final]` 시간에 로지스틱 맵의 상태를 나타내는 값 목록을 반환해야 합니다.
  이 함수를 `t_final = 100` 및 `1000` 기간 동안 실행하고 일부 값을 인쇄하십시오. 인구가 안정 상태로 향하고 있습니까?

:::::::::::::::  solution

## 해결책

1.
  ```python
  def logistic_map(x, r):
      return r * x * (1 - x)
  ```

2.
  ```python
  initial_population = 0.5
  t_final = 10
  r = 1.0
  population = [initial_population]

  for t in range(t_final):
      population.append( logistic_map(population[t], r) )
  ```

3.
  ```python
  def iterate(initial_population, t_final, r):
      population = [initial_population]
      for t in range(t_final):
          population.append( logistic_map(population[t], r) )
      return population
  
  for period in (10, 100, 1000):
      population = iterate(0.5, period, 1)
      print(population[-1])
  ```

  ```output
  0.06945089389714401
  0.009395779870614648
  0.0009913908614406382
  ```
  
  인구는 0에 가까워지는 것 같습니다.
  
:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::  callout

## 판다스에서 조건문과 함께 함수 사용하기

함수에는 종종 조건문이 포함됩니다. 다음은 사분위수 분할점에 대한 수작업 값에 따라 인수가 어느 사분위수에 있는지 나타내는 간단한 예입니다.

```python
def calculate_life_quartile(exp):
    if exp < 58.41:
        # 이 관측치는 1사분위수에 있습니다.
        return 1
    elif exp >= 58.41 and exp < 67.05:
        # 이 관측치는 2사분위수에 있습니다.
       return 2
    elif exp >= 67.05 and exp < 71.70:
        # 이 관측치는 3사분위수에 있습니다.
       return 3
    elif exp >= 71.70:
        # 이 관측치는 4사분위수에 있습니다.
       return 4
    else:
        # 이 관측치에는 잘못된 데이터가 있습니다.
       return None

calculate_life_quartile(62.5)
```

```output
2
```

해당 함수는 일반적으로 `for` 루프 내에서 사용되지만 판다스는 동일한 작업을 수행하는 더 효율적인 다른 방법을 가지고 있으며, 이는 데이터프레임 또는 데이터프레임의 일부에 함수를 *적용*하는 것입니다. 다음은 위의 정의를 사용한 예입니다.

```python
data = pd.read_csv('data/gapminder_all.csv')
data['life_qrtl'] = data['lifeExp_1952'].apply(calculate_life_quartile)
```

두 번째 줄에는 많은 내용이 있으므로 하나씩 살펴보겠습니다.
`=`의 오른쪽에는 `data['lifeExp']`로 시작하며, 이는 `data`라는 데이터프레임에서 `lifExp`라는 레이블이 붙은 열입니다.
`apply()`를 사용하여 `calculate_life_quartile`을 데이터프레임의 모든 행에 대해 이 열의 값에 적용합니다.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- 프로그램을 함수로 나누어 이해하기 쉽게 만듭니다.
- `def`를 사용하여 이름, 매개변수 및 코드 블록으로 함수를 정의합니다.
- 함수를 정의해도 실행되지는 않습니다.
- 함수 호출의 인수는 정의된 매개변수와 일치합니다.
- 함수는 `return`을 사용하여 호출자에게 결과를 반환할 수 있습니다.

::::::::::::::::::::::::::::::::::::::::::::::::::