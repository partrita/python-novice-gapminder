---
title: 플로팅
teaching: 15
exercises: 15
---

::::::::::::::::::::::::::::::::::::::: objectives

- 단일 데이터 세트를 보여주는 시계열 플롯을 생성합니다.
- 두 데이터 세트 간의 관계를 보여주는 산점도를 생성합니다.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- 내 데이터는 어떻게 플로팅할 수 있나요?
- 게시를 위해 플롯을 어떻게 저장할 수 있나요?

::::::::::::::::::::::::::::::::::::::::::::::::::

## [`matplotlib`](https://matplotlib.org/)는 파이썬에서 가장 널리 사용되는 과학 플로팅 라이브러리입니다.

- 일반적으로 [`matplotlib.pyplot`](https://matplotlib.org/stable/tutorials/introductory/pyplot.html)이라는 하위 라이브러리를 사용합니다.
- 주피터 노트북은 기본적으로 플롯을 인라인으로 렌더링합니다.

```python
import matplotlib.pyplot as plt
```

- 그러면 간단한 플롯을 (꽤) 간단하게 만들 수 있습니다.

```python
time = [0, 1, 2, 3]
position = [0, 100, 200, 300]

plt.plot(time, position)
plt.xlabel('Time (hr)')
plt.ylabel('Position (km)')
```

![](fig/9_simple_position_time_plot.svg){alt='위 코드 블록에 제공된 값을 사용하여 시간에 따른 위치(km)를 보여주는 선형 차트입니다. 기본적으로 그려진 선은 흰색 배경에 파란색이며 축은 입력 데이터 범위에 맞게 자동으로 조정되었습니다.'}

:::::::::::::::::::::::::::::::::::::::::  callout

## 모든 열린 그림 표시

주피터 노트북 예제에서 셀을 실행하면 코드 바로 아래에 그림이 생성됩니다.
그림은 나중에 볼 수 있도록 노트북 문서에도 포함됩니다.
그러나 터미널에서 시작된 대화형 파이썬 세션이나 명령줄을 통해 실행된 파이썬 스크립트와 같은 다른 파이썬 환경에서는 그림을 표시하기 위해 추가 명령이 필요합니다.

`matplotlib`에 그림을 표시하도록 지시합니다.

```python
plt.show()
```

이 명령은 노트북 내에서도 사용할 수 있습니다. 예를 들어 단일 셀에서 여러 그림이 생성된 경우 여러 그림을 표시하는 데 사용할 수 있습니다.

::::::::::::::::::::::::::::::::::::::::::::::::::

## [`Pandas 데이터프레임`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)에서 직접 데이터 플로팅.

- [Pandas 데이터프레임](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html)도 플로팅할 수 있습니다.
- 플로팅하기 전에 열 머리글을 숫자 값을 나타내므로 `string`에서 `integer` 데이터 유형으로 변환합니다. `gpdPercap_` 접두사를 제거하기 위해 [str.replace()](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.replace.html)를 사용한 다음 문자열 값 시리즈(`['1952', '1957', ..., '2007']`)를 정수 시리즈(`[1925, 1957, ..., 2007]`)로 변환하기 위해 [astype(int)](https://pandas.pydata.org/docs/reference/api/pandas.Series.astype.html)를 사용합니다.

```python
import pandas as pd

data = pd.read_csv('data/gapminder_gdp_oceania.csv', index_col='country')

# 각 열 이름의 마지막 4자에서 연도 추출
# 현재 열 이름은 'gdpPercap_(year)'로 구성되어 있으므로 GDP 대 연도를 플로팅할 때 명확성을 위해 (year) 부분만 유지하려고 합니다.
# 이렇게 하려면 인수에 명시된 문자를 문자열에서 제거하는 replace()를 사용합니다.
# 이 메서드는 문자열에서 작동하므로 Pandas Series.str 벡터화된 문자열 함수에서 replace()를 사용합니다.

years = data.columns.str.replace('gdpPercap_', '')

# 연도 값을 정수로 변환하여 결과를 데이터프레임에 다시 저장

data.columns = years.astype(int)

data.loc['Australia'].plot()
```

![](fig/9_gdp_australia.svg){alt='호주 GDP 플롯'}

## 데이터를 선택하고 변환한 다음 플로팅합니다.

- 기본적으로 [`DataFrame.plot`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.html#pandas.DataFrame.plot)은 행을 X축으로 플로팅합니다.
- 여러 시리즈를 플로팅하기 위해 데이터를 전치할 수 있습니다.

```python
data.T.plot()
plt.ylabel('GDP per capita')
```

![](fig/9_gdp_australia_nz.svg){alt='호주 및 뉴질랜드 GDP 플롯'}

## 다양한 스타일의 플롯을 사용할 수 있습니다.

- 예를 들어 더 멋진 스타일을 사용하여 막대 플롯을 만듭니다.

```python
plt.style.use('ggplot')
data.T.plot(kind='bar')
plt.ylabel('GDP per capita')
```

![](fig/gdp_bar.svg){alt='호주 GDP 막대 플롯'}

## `matplotlib` `plot` 함수를 직접 호출하여 데이터를 플로팅할 수도 있습니다.

- 명령은 `plt.plot(x, y)`입니다.
- 마커의 색상과 형식은 추가 선택적 인수로 지정할 수도 있습니다. 예: `b-`는 파란색 선, `g--`는 녹색 점선입니다.

## 데이터프레임에서 호주 데이터 가져오기

```python
years = data.columns
gdp_australia = data.loc['Australia']

plt.plot(years, gdp_australia, 'g--')
```

![](fig/9_gdp_australia_formatted.svg){alt='호주 GDP 형식화된 플롯'}

## 많은 데이터 세트를 함께 플로팅할 수 있습니다.

```python
# 두 국가의 데이터를 선택합니다.
gdp_australia = data.loc['Australia']
gdp_nz = data.loc['New Zealand']

# 다른 색상의 마커로 플로팅합니다.
plt.plot(years, gdp_australia, 'b-', label='Australia')
plt.plot(years, gdp_nz, 'g-', label='New Zealand')

# 범례를 만듭니다.
plt.legend(loc='upper left')
plt.xlabel('Year')
plt.ylabel('GDP per capita ($)')
```

:::::::::::::::::::::::::::::::::::::::::  callout

## 범례 추가

동일한 그림에 여러 데이터 세트를 플로팅할 때 데이터를 설명하는 범례가 있는 것이 바람직한 경우가 많습니다.

이것은 `matplotlib`에서 두 단계로 수행할 수 있습니다.

- 그림의 각 데이터 세트에 대한 레이블을 제공합니다.

```python
plt.plot(years, gdp_australia, label='Australia')
plt.plot(years, gdp_nz, label='New Zealand')
```

- `matplotlib`에 범례를 만들도록 지시합니다.

```python
plt.legend()
```

기본적으로 matplotlib은 적절한 위치에 범례를 배치하려고 시도합니다. 위치를 지정하려면 `loc=` 인수를 사용하여 수행할 수 있습니다. 예를 들어 플롯의 왼쪽 상단 모서리에 범례를 배치하려면 `loc='upper left'`를 지정합니다.

::::::::::::::::::::::::::::::::::::::::::::::::::

![](fig/9_gdp_australia_nz_formatted.svg){alt='호주 및 뉴질랜드 GDP 형식화된 플롯'}

- 호주와 뉴질랜드의 GDP를 상관시키는 산점도를 플로팅합니다.
- `plt.scatter` 또는 `DataFrame.plot.scatter`를 사용합니다.

```python
plt.scatter(gdp_australia, gdp_nz)
```

![](fig/9_gdp_correlation_plt.svg){alt='plt.scatter를 사용한 GDP 상관 관계'}

```python
data.T.plot.scatter(x = 'Australia', y = 'New Zealand')
```

![](fig/9_gdp_correlation_data.svg){alt='data.T.plot.scatter를 사용한 GDP 상관 관계'}

:::::::::::::::::::::::::::::::::::::::  challenge

## 최소값 및 최대값

아래 빈칸을 채워 유럽의 모든 국가에 대한 시간 경과에 따른 최소 1인당 GDP를 플로팅하십시오.
유럽에 대한 시간 경과에 따른 최대 1인당 GDP를 플로팅하도록 다시 수정하십시오.

```python
data_europe = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
data_europe.____.plot(label='min')
data_europe.____
plt.legend(loc='best')
plt.xticks(rotation=90)
```

:::::::::::::::  solution

## 해결책

```python
data_europe = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
data_europe.min().plot(label='min')
data_europe.max().plot(label='max')
plt.legend(loc='best')
plt.xticks(rotation=90)
```

![](fig/9_minima_maxima_solution.png){alt='최소 최대 솔루션'}

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 상관 관계

노트의 예제를 수정하여 데이터 세트의 각 연도에 대해 아시아 국가 간의 최소 및 최대 1인당 GDP 간의 관계를 보여주는 산점도를 만듭니다.
어떤 관계가 보이나요(있다면)?

:::::::::::::::  solution

## 해결책

```python
data_asia = pd.read_csv('data/gapminder_gdp_asia.csv', index_col='country')
data_asia.describe().T.plot(kind='scatter', x='min', y='max')
```

![](fig/9_correlations_solution1.svg){alt='상관 관계 솔루션 1'}

연간 최소 및 최대 GDP 값 사이에는 특별한 상관 관계가 보이지 않습니다. 아시아 국가의 운명은 함께 상승하고 하락하지 않는 것 같습니다.

:::::::::::::::::::::::::

최대값의 변동성이 최소값의 변동성보다 훨씬 높다는 것을 알 수 있습니다.
최대값과 최대 인덱스를 살펴보십시오.

```python
data_asia = pd.read_csv('data/gapminder_gdp_asia.csv', index_col='country')
data_asia.max().plot()
print(data_asia.idxmax())
print(data_asia.idxmin())
```

:::::::::::::::  solution

## 해결책

![](fig/9_correlations_solution2.png){alt='상관 관계 솔루션 2'}

이 값의 변동성은 1972년 이후 급격한 하락 때문인 것 같습니다.
아마도 지정학적 요인이 작용했을까요? 석유 생산국의 지배력을 감안할 때 브렌트유 지수가 흥미로운 비교가 될 수 있습니다.
미얀마는 지속적으로 GDP가 가장 낮지만 가장 높은 GDP 국가는 더 눈에 띄게 다양했습니다.

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 더 많은 상관 관계

이 짧은 프로그램은 2007년 GDP와 기대 수명 간의 상관 관계를 보여주는 플롯을 생성하며, 인구별로 마커 크기를 정규화합니다.

```python
data_all = pd.read_csv('data/gapminder_all.csv', index_col='country')
data_all.plot(kind='scatter', x='gdpPercap_2007', y='lifeExp_2007',
              s=data_all['pop_2007']/1e6)
```

온라인 도움말 및 기타 리소스를 사용하여 `plot`의 각 인수가 무엇을 하는지 설명하십시오.

:::::::::::::::  solution

## 해결책

![](fig/9_more_correlations_solution.svg){alt='더 많은 상관 관계 솔루션'}

살펴보기 좋은 곳은 플롯 함수의 설명서입니다 -
help(data_all.plot).

kind - 이미 본 것처럼 플롯할 종류를 결정합니다.

x 및 y - 플롯의 x축과 y축에 어떤 데이터를 배치할지 결정하는 열 이름 또는 인덱스입니다.

s - 이에 대한 자세한 내용은 plt.scatter 설명서에서 찾을 수 있습니다.
단일 숫자 또는 각 데이터 포인트에 대한 하나의 값입니다. 그려진 점의 크기를 결정합니다.

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::  callout

## 플롯을 파일에 저장

표시되는 플롯에 만족하면 파일에 저장하여 출판물에 포함할 수 있습니다.
matplotlib.pyplot 모듈에는 이를 수행하는 함수가 있습니다.
[savefig](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html).
이 함수를 호출하면, 예를 들어

```python
plt.savefig('my_figure.png')
```

현재 그림을 `my_figure.png` 파일에 저장합니다. 파일 형식은 파일 이름 확장자에서 자동으로 추론됩니다(다른 형식은 pdf, ps, eps 및 svg).

`plt`의 함수는 전역 그림 변수를 참조하며 그림이 화면에 표시된 후(예: `plt.show` 사용) matplotlib은 이 변수가 새 빈 그림을 참조하도록 만듭니다.
따라서 플롯이 화면에 표시되기 전에 `plt.savefig`를 호출해야 합니다. 그렇지 않으면 빈 플롯이 있는 파일을 찾을 수 있습니다.

데이터프레임을 사용할 때 데이터는 종종 한 줄로 생성되고 화면에 플로팅됩니다.
`plt.savefig`를 사용하는 것 외에도 `plt.gcf`를 사용하여 현재 그림에 대한 참조를 지역 변수에 저장하고 해당 변수에서 `savefig` 클래스 메서드를 호출하여 그림을 파일에 저장할 수 있습니다.

```python
data.plot(kind='bar')
fig = plt.gcf() # 현재 그림 가져오기
fig.savefig('my_figure.png')
```

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::  callout

## 플롯에 액세스할 수 있도록 만들기

논문이나 프레젠테이션에 들어갈 플롯을 생성할 때마다 모든 사람이 플롯을 이해할 수 있도록 몇 가지 작업을 수행할 수 있습니다.

- 항상 텍스트가 읽을 수 있을 만큼 큰지 확인하십시오. `xlabel`, `ylabel`, `title`, `legend`에서 `fontsize` 매개변수를 사용하고 축의 숫자 텍스트 크기를 늘리려면 [`tick_params`와 `labelsize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html)를 사용하십시오.
- 마찬가지로 그래프 요소를 쉽게 볼 수 있도록 해야 합니다. `s`를 사용하여 산점도 마커의 크기를 늘리고 `linewidth`를 사용하여 플롯 선의 크기를 늘립니다.
- 다른 플롯 요소를 구별하기 위해 색상(및 다른 것은 없음)을 사용하면 색맹이거나 흑백 사무실 프린터가 있는 사람에게는 플롯을 읽을 수 없게 됩니다. 선의 경우 `linestyle` 매개변수를 사용하여 다른 유형의 선을 사용할 수 있습니다. 산점도의 경우 `marker`를 사용하여 점의 모양을 변경할 수 있습니다. 색상이 확실하지 않은 경우 [Coblis](https://www.color-blindness.com/coblis-color-blindness-simulator/) 또는 [Color Oracle](https://colororacle.org/)을 사용하여 색맹인 사람에게 플롯이 어떻게 보일지 시뮬레이션할 수 있습니다.
  
::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- [`matplotlib`](https://matplotlib.org/)는 파이썬에서 가장 널리 사용되는 과학 플로팅 라이브러리입니다.
- Pandas 데이터프레임에서 직접 데이터를 플로팅합니다.
- 데이터를 선택하고 변환한 다음 플로팅합니다.
- 다양한 스타일의 플롯을 사용할 수 있습니다. 자세한 옵션은 [파이썬 그래프 갤러리](https://python-graph-gallery.com/matplotlib/)를 참조하십시오.
- 많은 데이터 세트를 함께 플로팅할 수 있습니다.

::::::::::::::::::::::::::::::::::::::::::::::::::