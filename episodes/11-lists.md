---
title: 리스트
teaching: 10
exercises: 10
---

::::::::::::::::::::::::::::::::::::::: objectives

- 프로그램에 값 모음이 필요한 이유를 설명합니다.
- 플랫 리스트를 만들고, 인덱싱하고, 슬라이싱하고, 할당 및 메서드 호출을 통해 수정하는 프로그램을 작성합니다.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- 여러 값을 어떻게 저장할 수 있나요?

::::::::::::::::::::::::::::::::::::::::::::::::::

## 리스트는 단일 구조에 많은 값을 저장합니다.

- `pressure_001`, `pressure_002` 등 백 개의 변수로 계산을 수행하는 것은 손으로 하는 것만큼이나 느릴 것입니다.
- *리스트*를 사용하여 많은 값을 함께 저장합니다.
  - 대괄호 `[...]` 안에 포함됩니다.
  - 쉼표 `,`로 구분된 값.
- `len`을 사용하여 리스트에 얼마나 많은 값이 있는지 확인합니다.

```python
pressures = [0.273, 0.275, 0.277, 0.275, 0.276]
print('pressures:', pressures)
print('length:', len(pressures))
```

```output
pressures: [0.273, 0.275, 0.277, 0.275, 0.276]
length: 5
```

## 항목의 인덱스를 사용하여 리스트에서 가져옵니다.

- 문자열과 같습니다.

```python
print('zeroth item of pressures:', pressures[0])
print('fourth item of pressures:', pressures[4])
```

```output
zeroth item of pressures: 0.273
fourth item of pressures: 0.276
```

## 리스트의 값은 할당을 통해 바꿀 수 있습니다.

- 할당 왼쪽에 인덱스 표현식을 사용하여 값을 바꿉니다.

```python
pressures[0] = 0.265
print('pressures is now:', pressures)
```

```output
pressures is now: [0.265, 0.275, 0.277, 0.275, 0.276]
```

## 리스트에 항목을 추가하면 길이가 늘어납니다.

- `list_name.append`를 사용하여 리스트 끝에 항목을 추가합니다.

```python
primes = [2, 3, 5]
print('primes is initially:', primes)
primes.append(7)
print('primes has become:', primes)
```

```output
primes is initially: [2, 3, 5]
primes has become: [2, 3, 5, 7]
```

- `append`는 리스트의 *메서드*입니다.
  - 함수와 같지만 특정 객체에 연결되어 있습니다.
- 메서드를 호출하려면 `object_name.method_name`을 사용합니다.
  - 의도적으로 라이브러리의 항목을 참조하는 방식과 유사합니다.
- 진행하면서 다른 리스트 메서드를 만나게 될 것입니다.
  - 미리 보려면 `help(list)`를 사용하십시오.
- `extend`는 `append`와 유사하지만 두 리스트를 결합할 수 있습니다. 예를 들어:

```python
teen_primes = [11, 13, 17, 19]
middle_aged_primes = [37, 41, 43, 47]
print('primes is currently:', primes)
primes.extend(teen_primes)
print('primes has now become:', primes)
primes.append(middle_aged_primes)
print('primes has finally become:', primes)
```

```output
primes is currently: [2, 3, 5, 7]
primes has now become: [2, 3, 5, 7, 11, 13, 17, 19]
primes has finally become: [2, 3, 5, 7, 11, 13, 17, 19, [37, 41, 43, 47]]
```

`extend`는 리스트의 "플랫" 구조를 유지하지만 리스트에 리스트를 추가하면 `primes`의 마지막 요소 자체가 정수가 아닌 리스트가 됩니다. 리스트는 모든 유형의 값을 포함할 수 있으므로 리스트의 리스트가 가능합니다.

## `del`을 사용하여 리스트에서 항목을 완전히 제거합니다.

- `del list_name[index]`를 사용하여 리스트에서 요소를 제거하고(예제에서는 9가 소수가 아님) 길이를 줄입니다.
- `del`은 함수나 메서드가 아니라 언어의 문입니다.

```python
primes = [2, 3, 5, 7, 9]
print('primes before removing last item:', primes)
del primes[4]
print('primes after removing last item:', primes)
```

```output
primes before removing last item: [2, 3, 5, 7, 9]
primes after removing last item: [2, 3, 5, 7]
```

## 빈 리스트에는 값이 없습니다.

- `[]`를 단독으로 사용하여 값이 없는 리스트를 나타냅니다.
  - "리스트의 0."
- 값을 수집하기 위한 시작점으로 유용합니다(다음 에피소드에서 볼 수 있음).

## 리스트에는 다른 유형의 값이 포함될 수 있습니다.

- 단일 리스트에는 숫자, 문자열 및 기타 모든 것이 포함될 수 있습니다.

```python
goals = [1, 'Create lists.', 2, 'Extract items from lists.', 3, 'Modify lists.']
```

## 문자열은 리스트처럼 인덱싱할 수 있습니다.

- 대괄호 안의 인덱스를 사용하여 문자열에서 단일 문자를 가져옵니다.

```python
element = 'carbon'
print('zeroth character:', element[0])
print('third character:', element[3])
```

```output
zeroth character: c
third character: b
```

## 문자열은 불변입니다.

- 문자열이 생성된 후에는 문자를 변경할 수 없습니다.
  - *불변*: 생성 후 변경할 수 없습니다.
  - 반면에 리스트는 *가변*입니다. 제자리에서 수정할 수 있습니다.
- 파이썬은 문자열을 값 모음이 아닌 부분이 있는 단일 값으로 간주합니다.

```python
element[0] = 'C'
```

```error
TypeError: 'str' object does not support item assignment
```

- 리스트와 문자열은 모두 *컬렉션*입니다.

## 컬렉션의 끝을 넘어서 인덱싱하면 오류가 발생합니다.

- 존재하지 않는 값에 액세스하려고 하면 파이썬에서 `IndexError`를 보고합니다.
  - 이것은 일종의 [런타임 오류](04-built-in.md)입니다.
  - 인덱스가 데이터를 기반으로 계산될 수 있으므로 코드가 구문 분석될 때 감지할 수 없습니다.

```python
print('99th element of element is:', element[99])
```

```output
IndexError: string index out of range
```

:::::::::::::::::::::::::::::::::::::::  challenge

## 빈칸 채우기

아래 프로그램이 표시된 출력을 생성하도록 빈칸을 채우십시오.

```python
values = ____
values.____(1)
values.____(3)
values.____(5)
print('first time:', values)
values = values[____]
print('second time:', values)
```

```output
first time: [1, 3, 5]
second time: [3, 5]
```

:::::::::::::::  solution

## 해결책

```python
values = []
values.append(1)
values.append(3)
values.append(5)
print('first time:', values)
values = values[1:]
print('second time:', values)
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 슬라이스는 얼마나 큰가요?

`start`와 `stop`이 모두 음이 아닌 정수인 경우 리스트 `values[start:stop]`의 길이는 얼마입니까?

:::::::::::::::  solution

## 해결책

리스트 `values[start:stop]`에는 최대 `stop - start`개의 요소가 있습니다. 예를 들어, `values[1:4]`에는 3개의 요소 `values[1]`, `values[2]`, `values[3]`이 있습니다.
왜 '최대'일까요? [2화](02-variables.md)에서 보았듯이 `stop`이 리스트 `values`의 총 길이보다 크면 여전히 리스트를 반환하지만 예상보다 짧을 것입니다.

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 문자열에서 리스트로, 그리고 다시

다음이 주어졌을 때:

```python
print('string to list:', list('tin'))
print('list to string:', ''.join(['g', 'o', 'l', 'd']))
```

```output
string to list: ['t', 'i', 'n']
list to string: gold
```

1. `list('some string')`은 무엇을 합니까?
2. `'-'.join(['x', 'y', 'z'])`는 무엇을 생성합니까?

:::::::::::::::  solution

## 해결책

1. [`list('some string')`](https://docs.python.org/3/library/stdtypes.html#list)은 문자열을 모든 문자를 포함하는 리스트로 변환합니다.
2. [`join`](https://docs.python.org/3/library/stdtypes.html#str.join)은 리스트의 각 문자열 요소를 *연결*한 문자열을 반환하고 리스트의 각 요소 사이에 구분 기호를 추가합니다. 결과는 `x-y-z`입니다. 요소 사이의 구분 기호는 이 메서드를 제공하는 문자열입니다.
  
:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 끝으로 작업하기

다음 프로그램은 무엇을 인쇄합니까?

```python
element = 'helium'
print(element[-1])
```

1. 파이썬은 음수 인덱스를 어떻게 해석합니까?
2. 리스트나 문자열에 N개의 요소가 있는 경우 안전하게 사용할 수 있는 가장 음수 인덱스는 무엇이며 해당 인덱스는 어떤 위치를 나타냅니까?
3. `values`가 리스트인 경우 `del values[-1]`은 무엇을 합니까?
4. `values`를 변경하지 않고 마지막 요소를 제외한 모든 요소를 어떻게 표시할 수 있습니까?
  (힌트: 슬라이싱과 음수 인덱싱을 결합해야 합니다.)

:::::::::::::::  solution

## 해결책

프로그램은 `m`을 인쇄합니다.

1. 파이썬은 음수 인덱스를 (처음부터 시작하는 것과 반대로) 끝에서부터 시작하는 것으로 해석합니다. 마지막 요소는 `-1`입니다.
2. N개 요소의 리스트와 함께 안전하게 사용할 수 있는 마지막 인덱스는 `-N` 요소이며, 이는 첫 번째 요소를 나타냅니다.
3. `del values[-1]`은 리스트에서 마지막 요소를 제거합니다.
4. `values[:-1]`
  
:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 리스트를 단계별로 살펴보기

다음 프로그램은 무엇을 인쇄합니까?

```python
element = 'fluorine'
print(element[::2])
print(element[::-1])
```

1. 슬라이스를 `low:high:stride`로 작성하면 `stride`는 무엇을 합니까?
2. 컬렉션에서 모든 짝수 번째 항목을 선택하는 표현식은 무엇입니까?

:::::::::::::::  solution

## 해결책

프로그램이 인쇄합니다.

```python
furn
eniroulf
```

1. `stride`는 슬라이스의 단계 크기입니다.
2. 슬라이스 `1::2`는 컬렉션에서 모든 짝수 번째 항목을 선택합니다. 요소 `1`(인덱싱이 `0`에서 시작하므로 두 번째 요소임)부터 시작하여 끝까지 계속되고(`end`가 지정되지 않았으므로) 단계 크기 `2`를 사용합니다(즉, 두 번째 요소마다 선택).
  
:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 슬라이스 경계

다음 프로그램은 무엇을 인쇄합니까?

```python
element = 'lithium'
print(element[0:20])
print(element[-1:3])
```

:::::::::::::::  solution

## 해결책

```output
lithium

```

첫 번째 문은 슬라이스가 문자열의 총 길이를 초과하므로 전체 문자열을 인쇄합니다.
두 번째 문은 슬라이스가 문자열의 "범위를 벗어나기" 때문에 빈 문자열을 반환합니다.

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 정렬 및 정렬됨

이 두 프로그램은 무엇을 인쇄합니까?
간단한 용어로 `sorted(letters)`와 `letters.sort()`의 차이점을 설명하십시오.

```python
# 프로그램 A
letters = list('gold')
result = sorted(letters)
print('letters is', letters, 'and result is', result)
```

```python
# 프로그램 B
letters = list('gold')
result = letters.sort()
print('letters is', letters, 'and result is', result)
```

:::::::::::::::  solution

## 해결책

프로그램 A가 인쇄합니다.

```output
letters is ['g', 'o', 'l', 'd'] and result is ['d', 'g', 'l', 'o']
```

프로그램 B가 인쇄합니다.

```output
letters is ['d', 'g', 'l', 'o'] and result is None
```

`sorted(letters)`는 `letters` 리스트의 정렬된 복사본을 반환하고(원래 리스트 `letters`는 변경되지 않음), `letters.sort()`는 `letters` 리스트를 제자리에서 정렬하고 아무것도 반환하지 않습니다.

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 복사(또는 안 함)

이 두 프로그램은 무엇을 인쇄합니까?
간단한 용어로 `new = old`와 `new = old[:]`의 차이점을 설명하십시오.

```python
# 프로그램 A
old = list('gold')
new = old      # 간단한 할당
new[0] = 'D'
print('new is', new, 'and old is', old)
```

```python
# 프로그램 B
old = list('gold')
new = old[:]   # 슬라이스 할당
new[0] = 'D'
print('new is', new, 'and old is', old)
```

:::::::::::::::  solution

## 해결책

프로그램 A가 인쇄합니다.

```output
new is ['D', 'o', 'l', 'd'] and old is ['D', 'o', 'l', 'd']
```

프로그램 B가 인쇄합니다.

```output
new is ['D', 'o', 'l', 'd'] and old is ['g', 'o', 'l', 'd']
```

`new = old`는 `new`를 `old` 리스트에 대한 참조로 만듭니다. `new`와 `old`는 동일한 객체를 가리킵니다.

`new = old[:]`는 그러나 `old` 리스트의 모든 요소를 포함하는 새 리스트 객체 `new`를 만듭니다. `new`와 `old`는 다른 객체입니다.

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- 리스트는 단일 구조에 많은 값을 저장합니다.
- 항목의 인덱스를 사용하여 리스트에서 가져옵니다.
- 리스트의 값은 할당을 통해 바꿀 수 있습니다.
- 리스트에 항목을 추가하면 길이가 늘어납니다.
- `del`을 사용하여 리스트에서 항목을 완전히 제거합니다.
- 빈 리스트에는 값이 없습니다.
- 리스트에는 다른 유형의 값이 포함될 수 있습니다.
- 문자열은 리스트처럼 인덱싱할 수 있습니다.
- 문자열은 불변입니다.
- 컬렉션의 끝을 넘어서 인덱싱하면 오류가 발생합니다.

::::::::::::::::::::::::::::::::::::::::::::::::::