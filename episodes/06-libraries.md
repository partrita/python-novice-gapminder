---
title: 라이브러리
teaching: 10
exercises: 10
---

::::::::::::::::::::::::::::::::::::::: objectives

- 소프트웨어 라이브러리가 무엇이며 프로그래머가 이를 만들고 사용하는 이유를 설명합니다.
- 파이썬 표준 라이브러리에서 모듈을 가져와 사용하는 프로그램을 작성합니다.
- 표준 라이브러리에 대한 설명서를 대화식(인터프리터에서) 및 온라인으로 찾아 읽습니다.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- 다른 사람이 작성한 소프트웨어를 어떻게 사용할 수 있나요?
- 그 소프트웨어가 무엇을 하는지 어떻게 알 수 있나요?

::::::::::::::::::::::::::::::::::::::::::::::::::

## 프로그래밍 언어의 힘의 대부분은 라이브러리에 있습니다.

- *라이브러리*는 다른 프로그램에서 사용할 함수를 포함하는 파일( *모듈* 이라고 함) 모음입니다.
  - 데이터 값(예: 숫자 상수) 및 기타 항목을 포함할 수도 있습니다.
  - 라이브러리의 내용은 관련이 있어야 하지만 이를 강제할 방법은 없습니다.
- 파이썬 [표준 라이브러리][stdlib]는 파이썬 자체와 함께 제공되는 광범위한 모듈 모음입니다.
- [PyPI][pypi](파이썬 패키지 인덱스)에서 많은 추가 라이브러리를 사용할 수 있습니다.
- 나중에 새 라이브러리를 작성하는 방법을 살펴보겠습니다.

:::::::::::::::::::::::::::::::::::::::::  callout

## 라이브러리 및 모듈

라이브러리는 모듈 모음이지만, 많은 라이브러리가 단일 모듈로만 구성되어 있기 때문에 이 용어는 종종 상호 교환적으로 사용됩니다. 따라서 혼동하더라도 걱정하지 마십시오.

::::::::::::::::::::::::::::::::::::::::::::::::::

## 프로그램은 사용하기 전에 라이브러리 모듈을 가져와야 합니다.

- `import`를 사용하여 라이브러리 모듈을 프로그램의 메모리에 로드합니다.
- 그런 다음 `module_name.thing_name`으로 모듈의 항목을 참조합니다.
  - 파이썬은 `.`을 "의 일부"를 의미하는 데 사용합니다.
- 표준 라이브러리의 모듈 중 하나인 `math` 사용:

```python
import math

print('pi is', math.pi)
print('cos(pi) is', math.cos(math.pi))
```

```output
pi is 3.141592653589793
cos(pi) is -1.0
```

- 각 항목을 모듈 이름으로 참조해야 합니다.
  - `math.cos(pi)`는 작동하지 않습니다. `pi`에 대한 참조는 함수의 `math`에 대한 참조를 어떻게든 "상속"하지 않습니다.

## `help`를 사용하여 라이브러리 모듈의 내용에 대해 알아봅니다.

- 함수에 대한 도움말과 똑같이 작동합니다.

```python
help(math)
```

```output
Help on module math:

NAME
    math

MODULE REFERENCE
    http://docs.python.org/3/library/math

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module is always available.  It provides access to the
    mathematical functions defined by the C standard.

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.
⋮ ⋮ ⋮
```

## 프로그램을 단축하기 위해 라이브러리 모듈에서 특정 항목을 가져옵니다.

- `from ... import ...`를 사용하여 라이브러리 모듈에서 특정 항목만 로드합니다.
- 그런 다음 라이브러리 이름을 접두사로 사용하지 않고 직접 참조합니다.

```python
from math import cos, pi

print('cos(pi) is', cos(pi))
```

```output
cos(pi) is -1.0
```

## 프로그램을 단축하기 위해 가져올 때 라이브러리 모듈에 대한 별칭을 만듭니다.

- `import ... as ...`를 사용하여 가져오는 동안 라이브러리에 짧은 *별칭*을 지정합니다.
- 그런 다음 해당 단축된 이름을 사용하여 라이브러리의 항목을 참조합니다.

```python
import math as m

print('cos(pi) is', m.cos(m.pi))
```

```output
cos(pi) is -1.0
```

- 자주 사용되거나 이름이 긴 라이브러리에 일반적으로 사용됩니다.
  - 예: `matplotlib` 플로팅 라이브러리는 종종 `mpl`로 별칭이 지정됩니다.
- 그러나 독자가 프로그램의 별칭을 배워야 하므로 프로그램을 이해하기 어렵게 만들 수 있습니다.

:::::::::::::::::::::::::::::::::::::::  challenge

## 수학 모듈 탐색

1. `sqrt`를 사용하지 않고 제곱근을 계산하는 데 사용할 수 있는 `math` 모듈의 함수는 무엇입니까?
2. 라이브러리에 이 함수가 포함되어 있는데 `sqrt`가 존재하는 이유는 무엇입니까?

:::::::::::::::  solution

## 해결책

1. `help(math)`를 사용하면 `sqrt(x)` 외에 `pow(x,y)`가 있음을 알 수 있으므로 `pow(x, 0.5)`를 사용하여 제곱근을 찾을 수 있습니다.

2. `sqrt(x)` 함수는 방정식을 구현할 때 `pow(x, 0.5)`보다 틀림없이 더 읽기 쉽습니다. 가독성은 좋은 프로그래밍의 초석이므로 이 특정 공통 사례에 대해 특별한 함수를 제공하는 것이 합리적입니다.
  
  또한 파이썬의 `math` 라이브러리 디자인은 `sqrt(x)`와 `pow(x,y)`를 모두 포함하는 C 표준에 기원을 두고 있으므로 파이썬의 함수 이름에는 프로그래밍의 역사가 약간 나타납니다.
  
:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 올바른 모듈 찾기

문자열에서 임의의 문자를 선택하고 싶습니다.

```python
bases = 'ACTTGCTTGAC'
```

1. 어떤 [표준 라이브러리][stdlib] 모듈이 도움이 될 수 있습니까?
2. 해당 모듈에서 어떤 함수를 선택하시겠습니까? 대안이 있습니까?
3. 함수를 사용하는 프로그램을 작성해 보십시오.

:::::::::::::::  solution

## 해결책

[random 모듈][randommod]이 도움이 될 것 같습니다.

문자열에는 11개의 문자가 있으며 각 문자는 0에서 10까지의 위치 인덱스를 가집니다.
[`random.randrange`](https://docs.python.org/3/library/random.html#random.randrange) 또는 [`random.randint`](https://docs.python.org/3/library/random.html#random.randint) 함수를 사용하여 0에서 10 사이의 임의의 정수를 얻은 다음 해당 인덱스에서 `bases` 문자를 선택할 수 있습니다.

```python
from random import randrange

random_index = randrange(len(bases))
print(bases[random_index])
```

또는 더 간결하게:

```python
from random import randrange

print(bases[randrange(len(bases))])
```

[`random.sample`](https://docs.python.org/3/library/random.html#random.sample) 함수를 찾았을 수도 있습니다.
입력은 약간 덜하지만 읽기만으로는 이해하기가 조금 더 어려울 수 있습니다.

```python
from random import sample

print(sample(bases, 1)[0])
```

이 함수는 값 목록을 반환합니다. [11화](11-lists.md)에서 목록에 대해 배웁니다.

가장 간단하고 짧은 해결책은 우리가 원하는 것을 정확히 수행하는 [`random.choice`](https://docs.python.org/3/library/random.html#random.choice) 함수입니다.

```python
from random import choice

print(choice(bases))
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 직소 퍼즐(파슨스 문제) 프로그래밍 예제

임의의 DNA 염기가 인쇄되고 문자열에서 해당 인덱스가 인쇄되도록 다음 문을 다시 정렬하십시오.
모든 문이 필요하지 않을 수 있습니다. 중간 변수를 자유롭게 사용/추가하십시오.

```python
bases="ACTTGCTTGAC"
import math
import random
___ = random.randrange(n_bases)
___ = len(bases)
print("random base ", bases[___], "base index", ___)
```

:::::::::::::::  solution

## 해결책

```python
import math 
import random
bases = "ACTTGCTTGAC" 
n_bases = len(bases)
idx = random.randrange(n_bases)
print("random base", bases[idx], "base index", idx)
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 도움말은 언제 사용할 수 있나요?

동료가 `help(math)`를 입력하면 파이썬에서 오류가 보고됩니다.

```error
NameError: name 'math' is not defined
```

동료가 무엇을 하는 것을 잊었습니까?

:::::::::::::::  solution

## 해결책

수학 모듈 가져오기(`import math`)

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 별칭으로 가져오기

1. 아래 프로그램이 `90.0`을 인쇄하도록 빈칸을 채우십시오.
2. `as` 없이 `import`를 사용하도록 프로그램을 다시 작성하십시오.
3. 어떤 형식이 더 읽기 쉽습니까?

```python
import math as m
angle = ____.degrees(____.pi / 2)
print(____)
```

:::::::::::::::  solution

## 해결책

```python
import math as m
angle = m.degrees(m.pi / 2)
print(angle)
```

다음과 같이 작성할 수 있습니다.

```python
import math
angle = math.degrees(math.pi / 2)
print(angle)
```

방금 코드를 작성했고 익숙하기 때문에 실제로 첫 번째 버전이 더 읽기 쉽다고 생각할 수 있습니다. 그러나 다른 사람이 작성한 거대한 코드를 읽으려고 할 때나 몇 달 후에 자신의 거대한 코드로 돌아갈 때, 명확한 약어 규칙이 있는 경우를 제외하고는 약어가 아닌 이름이 종종 더 쉽습니다.

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 라이브러리를 가져오는 방법은 여러 가지가 있습니다!

다음 인쇄 문을 적절한 라이브러리 호출과 일치시키십시오.

인쇄 명령:

1. `print("sin(pi/2) =", sin(pi/2))`
2. `print("sin(pi/2) =", m.sin(m.pi/2))`
3. `print("sin(pi/2) =", math.sin(math.pi/2))`

라이브러리 호출:

1. `from math import sin, pi`
2. `import math`
3. `import math as m`
4. `from math import *`

:::::::::::::::  solution

## 해결책

1. 라이브러리 호출 1과 4. 라이브러리 이름을 접두사로 사용하지 않고 `sin`과 `pi`를 직접 참조하려면 `from ... import ...` 문을 사용해야 합니다. 라이브러리 호출 1은 두 함수 `sin`과 `pi`를 구체적으로 가져오는 반면, 라이브러리 호출 4는 `math` 모듈의 모든 함수를 가져옵니다.
2. 라이브러리 호출 3. 여기서 `sin`과 `pi`는 `math` 대신 단축된 라이브러리 이름 `m`으로 참조됩니다. 라이브러리 호출 3은 `import ... as ...` 구문을 사용하여 정확히 그 작업을 수행합니다. 즉, `m`이라는 단축된 이름의 형태로 `math`에 대한 별칭을 만듭니다.
3. 라이브러리 호출 2. 여기서 `sin`과 `pi`는 일반 라이브러리 이름 `math`로 참조되므로 일반 `import ...` 호출로 충분합니다.

**참고:** 라이브러리 호출 4가 작동하지만 와일드카드 가져오기를 사용하여 모듈에서 모든 이름을 가져오는 것은 코드에서 모듈의 어떤 이름이 사용되는지 불분명하게 하므로 [권장되지 않습니다][pep8-imports]. 일반적으로 가져오기를 가능한 한 구체적으로 만들고 코드에서 사용하는 것만 가져오는 것이 가장 좋습니다. 라이브러리 호출 1에서 `import` 문은 `sin` 함수가 `math` 모듈에서 가져온다는 것을 명시적으로 알려주지만 라이브러리 호출 4는 이 정보를 전달하지 않습니다.

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 특정 항목 가져오기

1. 아래 프로그램이 `90.0`을 인쇄하도록 빈칸을 채우십시오.
2. 이 버전이 이전 버전보다 읽기 쉽습니까?
3. 프로그래머가 항상 이 형식의 `import`를 사용하지 *않는* 이유는 무엇입니까?

```python
____ math import ____, ____
angle = degrees(pi / 2)
print(angle)
```

:::::::::::::::  solution

## 해결책

```python
from math import degrees, pi
angle = degrees(pi / 2)
print(angle)
```

덜 빽빽하기 때문에 이 버전이 더 읽기 쉽다고 생각할 가능성이 높습니다.
이 형식의 가져오기를 사용하지 않는 주된 이유는 이름 충돌을 피하기 위해서입니다.
예를 들어, 자신의 변수나 함수에 `degrees`라는 이름을 사용하고 싶거나 다른 라이브러리에서 `degrees`라는 이름의 함수를 가져오려는 경우 이 방법으로 `degrees`를 가져오지 않을 것입니다.

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 오류 메시지 읽기

1. 아래 코드를 읽고 실행하지 않고 오류가 무엇인지 확인해 보십시오.
2. 코드를 실행하고 오류 메시지를 읽으십시오. 어떤 유형의 오류입니까?

```python
from math import log
log(0)
```

:::::::::::::::  solution

## 해결책

```output
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-1-d72e1d780bab> in <module>
      1 from math import log
----> 2 log(0)

ValueError: math domain error
```

1. `x`의 로그는 `x > 0`에 대해서만 정의되므로 0은 함수의 정의역 밖에 있습니다.
2. `ValueError` 유형의 오류가 발생하여 함수가 부적절한 인수 값을 받았음을 나타냅니다. 추가 메시지 "math domain error"는 문제가 무엇인지 더 명확하게 해줍니다.
  
:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

[stdlib]: https://docs.python.org/3/library/
[pypi]: https://pypi.python.org/pypi/
[randommod]: https://docs.python.org/3/library/random.html
[pep8-imports]: https://pep8.org/#imports

:::::::::::::::::::::::::::::::::::::::: keypoints

- 프로그래밍 언어의 힘의 대부분은 라이브러리에 있습니다.
- 프로그램은 사용하기 위해 라이브러리 모듈을 가져와야 합니다.
- `help`를 사용하여 라이브러리 모듈의 내용에 대해 알아봅니다.
- 프로그램을 단축하기 위해 라이브러리에서 특정 항목을 가져옵니다.
- 프로그램을 단축하기 위해 가져올 때 라이브러리에 대한 별칭을 만듭니다.

::::::::::::::::::::::::::::::::::::::::::::::::::