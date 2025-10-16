---
title: 데이터 세트 반복하기
teaching: 5
exercises: 10
---

::::::::::::::::::::::::::::::::::::::: objectives

- 파일 집합과 일치하는 glob 표현식을 읽고 쓸 수 있습니다.
- glob을 사용하여 파일 목록을 만듭니다.
- for 루프를 작성하여 목록에 이름이 지정된 파일에 대한 작업을 수행합니다.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- 단일 명령으로 많은 데이터 세트를 어떻게 처리할 수 있나요?

::::::::::::::::::::::::::::::::::::::::::::::::::

## `for` 루프를 사용하여 이름 목록이 지정된 파일을 처리합니다.

- 파일 이름은 문자열입니다.
- 그리고 목록에는 문자열이 포함될 수 있습니다.

```python
import pandas as pd
for filename in ['data/gapminder_gdp_africa.csv', 'data/gapminder_gdp_asia.csv']:
    data = pd.read_csv(filename, index_col='country')
    print(filename, data.min())
```

```output
data/gapminder_gdp_africa.csv gdpPercap_1952    298.846212
gdpPercap_1957    335.997115
gdpPercap_1962    355.203227
gdpPercap_1967    412.977514
⋮ ⋮ ⋮
gdpPercap_1997    312.188423
gdpPercap_2002    241.165877
gdpPercap_2007    277.551859
dtype: float64
data/gapminder_gdp_asia.csv gdpPercap_1952    331
gdpPercap_1957    350
gdpPercap_1962    388
gdpPercap_1967    349
⋮ ⋮ ⋮
gdpPercap_1997    415
gdpPercap_2002    611
gdpPercap_2007    944
dtype: float64
```

## [`glob.glob`](https://docs.python.org/3/library/glob.html#glob.glob)을 사용하여 이름이 패턴과 일치하는 파일 집합을 찾습니다.

- 유닉스에서 "globbing"이라는 용어는 "패턴으로 파일 집합 일치"를 의미합니다.
- 가장 일반적인 패턴은 다음과 같습니다.
  - `*`는 "0개 이상의 문자 일치"를 의미합니다.
  - `?`는 "정확히 한 문자 일치"를 의미합니다.
- 파이썬의 표준 라이브러리에는 패턴 일치 기능을 제공하는 [`glob`](https://docs.python.org/3/library/glob.html) 모듈이 포함되어 있습니다.
- [`glob`](https://docs.python.org/3/library/glob.html) 모듈에는 파일 패턴을 일치시키는 `glob`이라는 함수도 포함되어 있습니다.
- 예: `glob.glob('*.txt')`는 현재 디렉토리에서 이름이 `.txt`로 끝나는 모든 파일을 일치시킵니다.
- 결과는 (비어 있을 수 있는) 문자열 목록입니다.

```python
import glob
print('all csv files in data directory:', glob.glob('data/*.csv'))
```

```output
all csv files in data directory: ['data/gapminder_all.csv', 'data/gapminder_gdp_africa.csv', \
'data/gapminder_gdp_americas.csv', 'data/gapminder_gdp_asia.csv', 'data/gapminder_gdp_europe.csv', \
'data/gapminder_gdp_oceania.csv']
```

```python
print('all PDB files:', glob.glob('*.pdb'))
```

```output
all PDB files: []
```

## `glob`과 `for`를 사용하여 파일 배치를 처리합니다.

- 파일이 체계적이고 일관되게 이름이 지정되고 저장되어 간단한 패턴으로 올바른 데이터를 찾을 수 있으면 많은 도움이 됩니다.

```python
for filename in glob.glob('data/gapminder_*.csv'):
    data = pd.read_csv(filename)
    print(filename, data['gdpPercap_1952'].min())
```

```output
data/gapminder_all.csv 298.8462121
data/gapminder_gdp_africa.csv 298.8462121
data/gapminder_gdp_americas.csv 1397.717137
data/gapminder_gdp_asia.csv 331.0
data/gapminder_gdp_europe.csv 973.5331948
data/gapminder_gdp_oceania.csv 10039.59564
```

- 여기에는 모든 데이터와 지역별 데이터가 포함됩니다.
- 전체 데이터 세트를 제외하려면 연습에서 더 구체적인 패턴을 사용하십시오.
- 그러나 전체 데이터 세트의 최소값은 데이터 세트 중 하나의 최소값이기도 하므로 정확성에 대한 좋은 확인이 됩니다.

:::::::::::::::::::::::::::::::::::::::  challenge

## 일치 항목 결정

`glob.glob('data/*as*.csv')` 표현식과 일치하지 *않는* 파일은 무엇입니까?

1. `data/gapminder_gdp_africa.csv`
2. `data/gapminder_gdp_americas.csv`
3. `data/gapminder_gdp_asia.csv`

:::::::::::::::  solution

## 해결책

1은 glob과 일치하지 않습니다.

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 최소 파일 크기

이 프로그램을 수정하여 가장 적은 레코드가 있는 파일의 레코드 수를 인쇄하도록 하십시오.

```python
import glob
import pandas as pd
fewest = ____
for filename in glob.glob('data/*.csv'):
    dataframe = pd.____(filename)
    fewest = min(____, dataframe.shape[0])
print('smallest file has', fewest, 'records')
```

[`DataFrame.shape()` 메서드][shape-method]는 데이터 프레임의 행과 열 수가 있는 튜플을 반환합니다.

:::::::::::::::  solution

## 해결책

```python
import glob
import pandas as pd
fewest = float('Inf')
for filename in glob.glob('data/*.csv'):
    dataframe = pd.read_csv(filename)
    fewest = min(fewest, dataframe.shape[0])
print('smallest file has', fewest, 'records')
```

`fewest` 변수를 다루는 숫자보다 큰 숫자로 초기화하도록 선택했을 수 있지만 더 큰 숫자로 코드를 재사용하면 문제가 발생할 수 있습니다.
파이썬에서는 양의 무한대를 사용할 수 있으며 숫자가 아무리 크더라도 작동합니다.
[`float` 함수][float-function]가 인식하는 다른 특수 문자열은 무엇입니까?

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 데이터 비교

지역 데이터 세트를 읽고 각 지역의 시간 경과에 따른 평균 1인당 GDP를 단일 차트로 그리는 프로그램을 작성하십시오. Pandas는 데이터 프레임 계산에서 숫자가 아닌 열을 만나면 오류를 발생시키므로 해당 열을 필터링하거나 pandas에 무시하도록 알려야 합니다.

:::::::::::::::  solution

## 해결책

이 솔루션은 [문자열 `split` 메서드][split-method]를 사용하여 경로 'data/gapminder_gdp_a_specific_region.csv'에서 `region`을 추출하여 유용한 범례를 만듭니다.

```python
import glob
import pandas as pd
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1,1)
for filename in glob.glob('data/gapminder_gdp*.csv'):
    dataframe = pd.read_csv(filename)
    # 파일 이름에서 <region>을 추출합니다. 'data/gapminder_gdp_<region>.csv' 형식으로 예상됩니다.
    # split 메서드와 구분 기호로 `_`를 사용하여 문자열을 분할하고,
    # split이 반환하는 목록의 마지막 문자열(`<region>.csv`)을 검색한 다음
    # 해당 문자열에서 `.csv` 확장자를 제거합니다.
    # 참고: 다음 설명에서 다루는 pathlib 모듈도
    # 파일 시스템 경로 작업에 대한 편리한 추상화를 제공하며 이 문제를 해결할 수도 있습니다.
    # from pathlib import Path
    # region = Path(filename).stem.split('_')[-1]
    region = filename.split('_')[-1][:-4]
    # 데이터 프레임의 열에서 연도를 추출합니다.
    headings = dataframe.columns[1:]
    years = headings.str.split('_').str.get(1)
    # pandas는 데이터 프레임 계산에서 숫자가 아닌 열을 만나면 오류를 발생시킵니다.
    # 하지만 `numeric_only` 매개변수를 사용하여 pandas에 무시하도록 지시할 수 있습니다.
    dataframe.mean(numeric_only=True).plot(ax=ax, label=region)
    # 참고: 이 작업을 수행하는 또 다른 방법은 filter 메서드를 사용하여 이름에 gdp가 있는 열만 선택하는 것입니다.
    # dataframe.filter(like="gdp").mean().plot(ax=ax, label=region)
# 제목 및 레이블 설정
ax.set_title('시간 경과에 따른 지역별 1인당 GDP')
ax.set_xticks(range(len(years)))
ax.set_xticklabels(years)
ax.set_xlabel('연도')
plt.tight_layout()
plt.legend()
plt.show()
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::  callout

## 파일 경로 처리

[`pathlib` 모듈][pathlib-module]은 파일 확장자 없이 파일 이름을 반환하는 것과 같은 파일 및 경로 조작을 위한 유용한 추상화를 제공합니다. 이는 파일 및 디렉토리를 반복할 때 매우 유용합니다. 아래 예에서는 `Path` 객체를 만들고 해당 속성을 검사합니다.

```python
from pathlib import Path

p = Path("data/gapminder_gdp_africa.csv")
print(p.parent)
print(p.stem)
print(p.suffix)
```

```output
data
gapminder_gdp_africa
.csv
```

**힌트:** `dir()` 함수를 사용하여 `Path` 객체의 모든 사용 가능한 속성 및 메서드를 확인하십시오.

::::::::::::::::::::::::::::::::::::::::::::::::::

[shape-method]: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.shape.html
[float-function]: https://docs.python.org/3/library/functions.html#float
[split-method]: https://docs.python.org/3/library/stdtypes.html#str.split
[pathlib-module]: https://docs.python.org/3/library/pathlib.html


:::::::::::::::::::::::::::::::::::::::: keypoints

- `for` 루프를 사용하여 이름 목록이 지정된 파일을 처리합니다.
- `glob.glob`을 사용하여 이름이 패턴과 일치하는 파일 집합을 찾습니다.
- `glob`과 `for`를 사용하여 파일 배치를 처리합니다.

::::::::::::::::::::::::::::::::::::::::::::::::::