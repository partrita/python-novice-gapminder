---
title: 프로그래밍 스타일
teaching: 15
exercises: 15
---

::::::::::::::::::::::::::::::::::::::: objectives

- 코딩 스타일의 기본 규칙에 대한 건전한 정당성을 제공합니다.
- 한 페이지 분량의 프로그램을 더 읽기 쉽게 리팩토링하고 변경 사항을 정당화합니다.
- 파이썬 커뮤니티 코딩 표준(PEP-8)을 사용합니다.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- 프로그램을 더 읽기 쉽게 만들려면 어떻게 해야 하나요?
- 대부분의 프로그래머는 코드를 어떻게 형식화합니까?
- 프로그램이 자체 작동을 어떻게 확인할 수 있습니까?

::::::::::::::::::::::::::::::::::::::::::::::::::

## 코딩 스타일

일관된 코딩 스타일은 다른 사람(미래의 자신 포함)이 코드를 더 쉽게 읽고 이해하는 데 도움이 됩니다. 코드는 작성되는 것보다 훨씬 더 자주 읽히며, [파이썬의 선(Zen of Python)](https://www.python.org/dev/peps/pep-0020)에서 말했듯이 "가독성은 중요합니다".
파이썬은 첫 번째 파이썬 개선 제안(PEP) 중 하나인 [PEP8](https://www.python.org/dev/peps/pep-0008)을 통해 표준 스타일을 제안했습니다.

강조할 만한 몇 가지 사항:

- 코드를 문서화하고 가정, 내부 알고리즘, 예상 입력, 예상 출력 등이 명확한지 확인하십시오.
- 명확하고 의미적으로 의미 있는 변수 이름을 사용하십시오.
- 줄을 들여쓰기할 때 탭이 아닌 공백을 사용하십시오(탭은 다른 텍스트 편집기, 운영 체제 및 버전 제어 시스템에서 문제를 일으킬 수 있음).

## 코드에서 표준 파이썬 스타일을 따르십시오.

- [PEP8](https://www.python.org/dev/peps/pep-0008):
  변수 이름 지정 방법, 코드 들여쓰기 방법, `import` 문 구성 방법 등과 같은 주제를 다루는 파이썬 스타일 가이드입니다.
  PEP8을 준수하면 다른 파이썬 개발자가 코드를 더 쉽게 읽고 이해하고 기여가 어떻게 보여야 하는지 이해하는 데 도움이 됩니다.
- PEP8 준수 여부를 확인하려면 [pycodestyle 애플리케이션](https://pypi.org/project/pycodestyle/)을 사용할 수 있으며 [black 코드 포맷터](https://github.com/psf/black)와 같은 도구는 코드를 PEP8 및 pycodestyle에 맞게 자동으로 포맷할 수 있습니다(주피터 노트북 포맷터도 존재함 [nb_black](https://github.com/dnanhkhoa/nb_black)).
- 일부 그룹 및 조직은 PEP8 외에 다른 스타일 지침을 따릅니다. 예를 들어 [파이썬에 대한 구글 스타일 가이드](https://google.github.io/styleguide/pyguide.html)는 약간 다른 권장 사항을 제시합니다. 구글은 [yapf](https://github.com/google/yapf/)라는 자신의 스타일이나 PEP8로 코드를 포맷하는 데 도움이 되는 애플리케이션을 작성했습니다.
- 코딩 스타일과 관련하여 핵심은 *일관성*입니다. PEP8, 구글 스타일 또는 다른 스타일이든 프로젝트에 대한 스타일을 선택하고 자신과 협력하는 다른 모든 사람이 이를 준수하도록 최선을 다하십시오. 프로젝트 내의 일관성은 종종 사용되는 특정 스타일보다 더 영향력이 있습니다. 일관된 스타일은 다른 사람과 미래의 자신을 위해 소프트웨어를 더 쉽게 읽고 이해할 수 있도록 합니다.

## 내부 오류를 확인하려면 어설션을 사용하십시오.

어설션은 코드가 실행되는 컨텍스트가 예상대로인지 확인하는 간단하지만 강력한 방법입니다.

```python
def calc_bulk_density(mass, volume):
    '''건조 벌크 밀도 = 분말 질량 / 분말 부피를 반환합니다.'''
    assert volume > 0
    return mass / volume
```

어설션이 `False`이면 파이썬 인터프리터는 `AssertionError` 런타임 예외를 발생시킵니다. 실패한 표현식의 소스 코드가 오류 메시지의 일부로 표시됩니다. 코드에서 어설션을 무시하려면 '-O'(최적화) 스위치로 인터프리터를 실행하십시오. 어설션에는 간단한 검사만 포함되어야 하며 프로그램의 상태를 변경해서는 안 됩니다. 예를 들어 어설션에는 할당이 포함되어서는 안 됩니다.

## 내장 도움말을 제공하려면 독스트링을 사용하십시오.

함수의 첫 번째 항목이 변수에 직접 할당되지 않은 문자열인 경우 파이썬은 이를 함수에 연결하여 내장 도움말 함수를 통해 액세스할 수 있도록 합니다. 문서를 제공하는 이 문자열을 *독스트링*이라고도 합니다.

```python
def average(values):
    "값의 평균을 반환하거나 값이 제공되지 않으면 None을 반환합니다."

    if len(values) == 0:
        return None
    return sum(values) / len(values)

help(average)
```

```output
Help on function average in module __main__:

average(values)
    값의 평균을 반환하거나 값이 제공되지 않으면 None을 반환합니다.
```

:::::::::::::::::::::::::::::::::::::::::  callout

## 여러 줄 문자열

문서에는 종종 *여러 줄 문자열*을 사용합니다.
이들은 세 개의 따옴표 문자(작은따옴표 또는 큰따옴표)로 시작하고 끝나며 세 개의 일치하는 문자로 끝납니다.

```python
"""이 문자열은 여러 줄에 걸쳐 있습니다.

빈 줄이 허용됩니다."""
```

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 무엇이 표시될까요?

아래 코드에서 온라인 도움말로 사용할 수 있는 줄을 강조 표시하십시오.
사용할 수 있어야 하지만 사용할 수 없는 줄이 있습니까?
구문 오류나 런타임 오류를 생성하는 줄이 있습니까?

```python
"Find maximum edit distance between multiple sequences."
# This finds the maximum distance between all sequences.

def overall_max(sequences):
    '''Determine overall maximum edit distance.'''

    highest = 0
    for left in sequences:
        for right in sequences:
            '''Avoid checking sequence against itself.'''
            if left != right:
                this = edit_distance(left, right)
                highest = max(highest, this)

    # Report.
    return highest
```

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 이것을 문서화하십시오

주석을 사용하여 잠재적으로 직관적이지 않은 섹션이나 개별 코드 줄을 설명하고 다른 사람들이 이해하는 데 도움을 주십시오. 특히 나중에 코드를 이해하고 편집해야 할 수 있는 사람(자신 포함)에게 유용합니다.

독스트링을 사용하여 메서드나 클래스의 허용 가능한 입력 및 예상 출력, 목적, 가정 및 의도된 동작을 문서화하십시오. 독스트링은 사용자가 메서드나 클래스에서 내장된 `help` 메서드를 호출할 때 표시됩니다.

다음 함수의 주석을 독스트링으로 바꾸고 `help`가 제대로 표시되는지 확인하십시오.

```python
def middle(a, b, c):
    # 세 값의 중간 값을 반환합니다.
    # 값이 실제로 비교될 수 있다고 가정합니다.
    values = [a, b, c]
    values.sort()
    return values[1]
```

:::::::::::::::  solution

## 해결책

```python
def middle(a, b, c):
    '''세 값의 중간 값을 반환합니다.
    값이 실제로 비교될 수 있다고 가정합니다.'''
    values = [a, b, c]
    values.sort()
    return values[1]
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 이 코드 정리하기

1. 이 짧은 프로그램을 읽고 무엇을 하는지 예측해 보십시오.
2. 실행해 보십시오. 예측이 얼마나 정확했습니까?
3. 프로그램을 더 읽기 쉽게 리팩토링하십시오.
  동작이 변경되지 않았는지 확인하기 위해 각 변경 후에 실행하는 것을 잊지 마십시오.
4. 이웃의 재작성과 비교하십시오.
  무엇을 똑같이 했습니까?
  무엇을 다르게 했고 그 이유는 무엇입니까?

```python
n = 10
s = 'et cetera'
print(s)
i = 0
while i < n:
    # print('at', j)
    new = ''
    for j in range(len(s)):
        left = j-1
        right = (j+1)%len(s)
        if s[left]==s[right]: new = new + '-'
        else: new = new + '*'
    s=''.join(new)
    print(s)
    i += 1
```

:::::::::::::::  solution

## 해결책

다음은 한 가지 해결책입니다.

```python
def string_machine(input_string, iterations):
    """
    input_string을 가져와서 인접한 문자가 동일한지 여부에 따라
    -'s와 *'s로 새 문자열을 생성합니다.
    제공된 반복 횟수만큼 결과 문자열로 이 절차를 반복합니다.
    """
    print(input_string)
    input_string_length = len(input_string)
    old = input_string
    for i in range(iterations):
        new = ''
        # 이전 문자열의 문자를 반복합니다.
        for j in range(input_string_length):
            left = j-1
            right = (j+1) % input_string_length  # 오른쪽 인덱스가 순환되도록 합니다.
            if old[left] == old[right]:
                new = new + '-'
            else:
                new = new + '*'
        print(new)
        # 새 문자열을 이전 문자열로 저장합니다.
        old = new     

string_machine('et cetera', 10)
```

```output
et cetera
*****-***
----*-*--
---*---*-
--*-*-*-*
**-------
***-----*
--**---**
*****-***
----*-*--
---*---*-
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- 코드에서 표준 파이썬 스타일을 따르십시오.
- 내장 도움말을 제공하려면 독스트링을 사용하십시오.

::::::::::::::::::::::::::::::::::::::::::::::::::