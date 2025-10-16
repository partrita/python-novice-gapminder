---
title: For 루프
teaching: 10
exercises: 15
---

::::::::::::::::::::::::::::::::::::::: objectives

- for 루프가 일반적으로 무엇에 사용되는지 설명합니다.
- 간단한 (중첩되지 않은) 루프의 실행을 추적하고 각 반복에서 변수의 값을 올바르게 명시합니다.
- 누산기 패턴을 사용하여 값을 집계하는 for 루프를 작성합니다.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- 프로그램이 많은 일을 하도록 하려면 어떻게 해야 하나요?

::::::::::::::::::::::::::::::::::::::::::::::::::

## *for 루프*는 컬렉션의 각 값에 대해 한 번씩 명령을 실행합니다.

- 리스트의 값에 대해 하나씩 계산을 수행하는 것은 `pressure_001`, `pressure_002` 등으로 작업하는 것만큼 고통스럽습니다.
- *for 루프*는 파이썬에게 리스트, 문자열 또는 다른 컬렉션의 각 값에 대해 일부 문을 한 번씩 실행하도록 지시합니다.
- "이 그룹의 각 항목에 대해 이러한 작업을 수행하십시오."

```python
for number in [2, 3, 5]:
    print(number)
```

- 이 `for` 루프는 다음과 같습니다.

```python
print(2)
print(3)
print(5)
```

- 그리고 `for` 루프의 출력은 다음과 같습니다.

```output
2
3
5
```

## `for` 루프는 컬렉션, 루프 변수 및 본문으로 구성됩니다.

```python
for number in [2, 3, 5]:
    print(number)
```

- 컬렉션 `[2, 3, 5]`는 루프가 실행되는 대상입니다.
- 본문 `print(number)`는 컬렉션의 각 값에 대해 수행할 작업을 지정합니다.
- 루프 변수 `number`는 루프의 각 *반복*에 대해 변경되는 것입니다.
  - "현재 항목".

## `for` 루프의 첫 번째 줄은 콜론으로 끝나야 하며 본문은 들여쓰기해야 합니다.

- 첫 번째 줄 끝에 있는 콜론은 문 *블록*의 시작을 알립니다.
- 파이썬은 *중첩*을 표시하기 위해 `{}` 또는 `begin`/`end` 대신 들여쓰기를 사용합니다.
  - 일관된 들여쓰기는 합법적이지만 거의 모든 사람이 4개의 공백을 사용합니다.

```python
for number in [2, 3, 5]:
print(number)
```

```error
IndentationError: expected an indented block
```

- 파이썬에서 들여쓰기는 항상 의미가 있습니다.

```python
firstName = "Jon"
  lastName = "Smith"
```

```error
  File "<ipython-input-7-f65f2962bf9c>", line 2
    lastName = "Smith"
    ^
IndentationError: unexpected indent
```

- 이 오류는 두 번째 줄 시작 부분의 추가 공백을 제거하여 해결할 수 있습니다.

## 루프 변수는 무엇이든 호출할 수 있습니다.

- 모든 변수와 마찬가지로 루프 변수는 다음과 같습니다.
  - 필요에 따라 생성됩니다.
  - 의미 없음: 이름은 무엇이든 될 수 있습니다.

```python
for kitten in [2, 3, 5]:
    print(kitten)
```

## 루프의 본문에는 많은 문이 포함될 수 있습니다.

- 그러나 어떤 루프도 몇 줄보다 길어서는 안 됩니다.
- 인간이 더 큰 코드 덩어리를 염두에 두기는 어렵습니다.

```python
primes = [2, 3, 5]
for p in primes:
    squared = p ** 2
    cubed = p ** 3
    print(p, squared, cubed)
```

```output
2 4 8
3 9 27
5 25 125
```

## `range`를 사용하여 숫자 시퀀스를 반복합니다.

- 내장 함수 [`range`](https://docs.python.org/3/library/stdtypes.html#range)는 숫자 시퀀스를 생성합니다.
  - 리스트가 *아님*: 숫자는 필요에 따라 생성되어 큰 범위에 대한 루프를 더 효율적으로 만듭니다.
- `range(N)`은 0..N-1까지의 숫자입니다.
  - 길이 N의 리스트 또는 문자열의 정확한 법적 인덱스입니다.

```python
print('a range is not a list: range(0, 3)')
for number in range(0, 3):
    print(number)
```

```output
a range is not a list: range(0, 3)
0
1
2
```

## 누산기 패턴은 많은 값을 하나로 바꿉니다.

- 프로그램에서 일반적인 패턴은 다음과 같습니다.
  1. *누산기* 변수를 0, 빈 문자열 또는 빈 리스트로 초기화합니다.
  2. 컬렉션의 값으로 변수를 업데이트합니다.

```python
# 처음 10개 정수의 합을 구합니다.
total = 0
for number in range(10):
   total = total + (number + 1)
print(total)
```

```output
55
```

- `total = total + (number + 1)`을 다음과 같이 읽습니다.
  - 루프 변수 `number`의 현재 값에 1을 더합니다.
  - 그것을 누산기 변수 `total`의 현재 값에 더합니다.
  - 그것을 `total`에 할당하여 현재 값을 바꿉니다.
- `range`가 1..10이 아닌 0..9를 생성하기 때문에 `number + 1`을 더해야 합니다.

:::::::::::::::::::::::::::::::::::::::  challenge

## 오류 분류

들여쓰기 오류는 구문 오류입니까, 아니면 런타임 오류입니까?

:::::::::::::::  solution

## 해결책

IndentationError는 구문 오류입니다. 구문 오류가 있는 프로그램은 시작할 수 없습니다.
런타임 오류가 있는 프로그램은 시작되지만 특정 조건에서 오류가 발생합니다.

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 실행 추적

이 프로그램이 실행될 때 실행되는 줄의 번호와 각 줄이 실행된 후 변수의 값을 보여주는 표를 만듭니다.

```python
total = 0
for char in "tin":
    total = total + 1
```

:::::::::::::::  solution

## 해결책

| 줄 번호 | 변수                 |
| ------- | -------------------- |
| 1       | total = 0            | 
| 2       | total = 0 char = 't' | 
| 3       | total = 1 char = 't' | 
| 2       | total = 1 char = 'i' | 
| 3       | total = 2 char = 'i' | 
| 2       | total = 2 char = 'n' | 
| 3       | total = 3 char = 'n' | 

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 문자열 뒤집기

아래 프로그램의 빈칸을 채워 "nit"("tin"의 역순)를 인쇄하도록 합니다.

```python
original = "tin"
result = ____
for char in original:
    result = ____
print(result)
```

:::::::::::::::  solution

## 해결책

```python
original = "tin"
result = ""
for char in original:
    result = char + result
print(result)
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 누적 연습

아래 각 프로그램의 빈칸을 채워 표시된 결과를 생성하십시오.

```python
# 리스트에 있는 문자열의 총 길이: ["red", "green", "blue"] => 12
total = 0
for word in ["red", "green", "blue"]:
    ____ = ____ + len(word)
print(total)
```

:::::::::::::::  solution

## 해결책

```python
total = 0
for word in ["red", "green", "blue"]:
    total = total + len(word)
print(total)
```

:::::::::::::::::::::::::

```python
# 단어 길이 리스트: ["red", "green", "blue"] => [3, 5, 4]
lengths = ____
for word in ["red", "green", "blue"]:
    lengths.____(____)
print(lengths)
```

:::::::::::::::  solution

## 해결책

```python
lengths = []
for word in ["red", "green", "blue"]:
    lengths.append(len(word))
print(lengths)
```

:::::::::::::::::::::::::

```python
# 모든 단어 연결: ["red", "green", "blue"] => "redgreenblue"
words = ["red", "green", "blue"]
result = ____
for ____ in ____:
    ____
print(result)
```

:::::::::::::::  solution

## 해결책

```python
words = ["red", "green", "blue"]
result = ""
for word in words:
    result = result + word
print(result)
```

:::::::::::::::::::::::::

**약어 만들기:** `["red", "green", "blue"]` 리스트에서 시작하여 for 루프를 사용하여 약어 `"RGB"`를 만듭니다.

**힌트:** 약어를 올바르게 포맷하려면 문자열 메서드를 사용해야 할 수 있습니다.

:::::::::::::::  solution

## 해결책

```python
acronym = ""
for word in ["red", "green", "blue"]:
    acronym = acronym + word[0].upper()
print(acronym)
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 누적 합계

아래 코드 줄을 재정렬하고 올바르게 들여쓰기하여 데이터의 누적 합계가 있는 리스트를 인쇄하도록 합니다.
결과는 `[1, 3, 5, 10]`이어야 합니다.

```python
cumulative.append(total)
for number in data:
cumulative = []
total = total + number
total = 0
print(cumulative)
data = [1,2,2,5]
```

:::::::::::::::  solution

## 해결책

```python
total = 0
data = [1,2,2,5]
cumulative = []
for number in data:
    total = total + number
    cumulative.append(total)
print(cumulative)
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 변수 이름 오류 식별

1. 아래 코드를 읽고 실행하지 않고 오류가 무엇인지 확인해 보십시오.
2. 코드를 실행하고 오류 메시지를 읽으십시오.
  어떤 유형의 `NameError`라고 생각하십니까?
  따옴표가 없는 문자열, 잘못된 변수 또는 정의되었어야 했지만 정의되지 않은 변수입니까?
3. 오류를 수정하십시오.
4. 모든 오류를 수정할 때까지 2단계와 3단계를 반복하십시오.

```python
for number in range(10):
    # 숫자가 3의 배수이면 a를 사용하고 그렇지 않으면 b를 사용합니다.
    if (Number % 3) == 0:
        message = message + a
    else:
        message = message + "b"
print(message)
```

:::::::::::::::  solution

## 해결책

- 파이썬 변수 이름은 대소문자를 구분합니다. `number`와 `Number`는 다른 변수를 참조합니다.
- `message` 변수는 빈 문자열로 초기화해야 합니다.
- `message`에 정의되지 않은 변수 `a`가 아닌 문자열 `"a"`를 추가하려고 합니다.

```python
message = ""
for number in range(10):
    # 숫자가 3의 배수이면 a를 사용하고 그렇지 않으면 b를 사용합니다.
    if (number % 3) == 0:
        message = message + "a"
    else:
        message = message + "b"
print(message)
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 항목 오류 식별

1. 아래 코드를 읽고 실행하지 않고 오류가 무엇인지 확인해 보십시오.
2. 코드를 실행하고 오류 메시지를 읽으십시오. 어떤 유형의 오류입니까?
3. 오류를 수정하십시오.

```python
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print('My favorite season is ', seasons[4])
```

:::::::::::::::  solution

## 해결책

이 리스트에는 4개의 요소가 있으며 리스트의 마지막 요소에 액세스하는 인덱스는 `3`입니다.

```python
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print('My favorite season is ', seasons[3])
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- *for 루프*는 컬렉션의 각 값에 대해 한 번씩 명령을 실행합니다.
- `for` 루프는 컬렉션, 루프 변수 및 본문으로 구성됩니다.
- `for` 루프의 첫 번째 줄은 콜론으로 끝나야 하며 본문은 들여쓰기해야 합니다.
- 파이썬에서 들여쓰기는 항상 의미가 있습니다.
- 루프 변수는 무엇이든 호출할 수 있습니다(그러나 루핑 변수에 의미 있는 이름을 지정하는 것이 좋습니다).
- 루프의 본문에는 많은 문이 포함될 수 있습니다.
- `range`를 사용하여 숫자 시퀀스를 반복합니다.
- 누산기 패턴은 많은 값을 하나로 바꿉니다.

::::::::::::::::::::::::::::::::::::::::::::::::::