---
title: 판다스 데이터프레임
teaching: 15
exercises: 15
---

::::::::::::::::::::::::::::::::::::::: objectives

- 판다스 데이터프레임에서 개별 값을 선택합니다.
- 데이터프레임에서 전체 행 또는 전체 열을 선택합니다.
- 단일 작업으로 데이터프레임에서 행과 열의 하위 집합을 선택합니다.
- 단일 부울 기준으로 데이터프레임의 하위 집합을 선택합니다.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- 표 형식 데이터의 통계 분석은 어떻게 할 수 있나요?

::::::::::::::::::::::::::::::::::::::::::::::::::

## 판다스 데이터프레임/시리즈에 대한 참고 사항

[데이터프레임][pandas-dataframe]은 [시리즈][pandas-series]의 모음입니다.
데이터프레임은 판다스가 테이블을 나타내는 방식이며, 시리즈는 판다스가 열을 나타내는 데 사용하는 데이터 구조입니다.

판다스는 [Numpy][numpy] 라이브러리 위에 구축되었으며, 실제로 이는 Numpy 배열에 대해 정의된 대부분의 메서드가 판다스 시리즈/데이터프레임에 적용된다는 것을 의미합니다.

판다스를 매우 매력적으로 만드는 것은 테이블의 개별 레코드에 액세스하는 강력한 인터페이스, 누락된 값의 적절한 처리, 데이터프레임 간의 관계형 데이터베이스 작업입니다.

## 값 선택

데이터프레임의 `[i,j]` 위치에 있는 값에 액세스하려면 사용 중인 `i`의 의미에 따라 두 가지 옵션이 있습니다.
데이터프레임은 테이블의 행을 식별하는 방법으로 *인덱스*를 제공한다는 것을 기억하십시오.
그런 다음 행은 테이블 내의 *위치*와 *레이블*을 가지며, 이는 데이터프레임의 *항목*을 고유하게 식별합니다.

## `DataFrame.iloc[..., ...]`를 사용하여 (항목) 위치별로 값을 선택합니다.

- 문자열에서 문자 선택의 2D 버전과 유사하게 숫자 인덱스로 위치를 지정할 수 있습니다.

```python
import pandas as pd
data = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
print(data.iloc[0, 0])
```

```output
1601.056136
```

## `DataFrame.loc[..., ...]`를 사용하여 (항목) 레이블별로 값을 선택합니다.

- 행 및/또는 열 이름으로 위치를 지정할 수 있습니다.

```python
print(data.loc["Albania", "gdpPercap_1952"])
```

```output
1601.056136
```

## 모든 열 또는 모든 행을 의미하려면 `:`를 단독으로 사용합니다.

- 파이썬의 일반적인 슬라이싱 표기법과 같습니다.

```python
print(data.loc["Albania", :])
```

```output
gdpPercap_1952    1601.056136
gdpPercap_1957    1942.284244
gdpPercap_1962    2312.888958
gdpPercap_1967    2760.196931
gdpPercap_1972    3313.422188
gdpPercap_1977    3533.003910
gdpPercap_1982    3630.880722
gdpPercap_1987    3738.932735
gdpPercap_1992    2497.437901
gdpPercap_1997    3193.054604
gdpPercap_2002    4604.211737
gdpPercap_2007    5937.029526
Name: Albania, dtype: float64
```

- `data.loc["Albania"]`를 인쇄하면 동일한 결과를 얻을 수 있습니다(두 번째 인덱스 없이).

```python
print(data.loc[:, "gdpPercap_1952"])
```

```output
country
Albania                    1601.056136
Austria                    6137.076492
Belgium                    8343.105127
⋮ ⋮ ⋮
Switzerland               14734.232750
Turkey                     1969.100980
United Kingdom             9979.508487
Name: gdpPercap_1952, dtype: float64
```

- `data["gdpPercap_1952"]`를 인쇄하면 동일한 결과를 얻을 수 있습니다.
- `data.gdpPercap_1952`를 인쇄해도 동일한 결과를 얻을 수 있습니다(메서드에 대한 `.` 표기법과 쉽게 혼동될 수 있으므로 권장하지 않음).

## `DataFrame.loc` 및 명명된 슬라이스를 사용하여 여러 열 또는 행을 선택합니다.

```python
print(data.loc['Italy':'Poland', 'gdpPercap_1962':'gdpPercap_1972'])
```

```output
             gdpPercap_1962  gdpPercap_1967  gdpPercap_1972
country
Italy           8243.582340    10022.401310    12269.273780
Montenegro      4649.593785     5907.850937     7778.414017
Netherlands    12790.849560    15363.251360    18794.745670
Norway         13450.401510    16361.876470    18965.055510
Poland          5338.752143     6557.152776     8006.506993
```

위의 코드에서 **`loc`를 사용한 슬라이싱은 양쪽 끝을 포함**한다는 것을 발견했으며, 이는 **`iloc`를 사용한 슬라이싱**과 다릅니다. `iloc`를 사용한 슬라이싱은 최종 인덱스를 포함하지 않고 그 이전까지 모든 것을 나타냅니다.

## 슬라이싱 결과는 추가 작업에 사용할 수 있습니다.

- 일반적으로 슬라이스를 인쇄만 하지는 않습니다.
- 전체 데이터프레임에서 작동하는 모든 통계 연산자는 슬라이스에서도 동일하게 작동합니다.
- 예: 슬라이스의 최대값 계산.

```python
print(data.loc['Italy':'Poland', 'gdpPercap_1962':'gdpPercap_1972'].max())
```

```output
gdpPercap_1962    13450.40151
gdpPercap_1967    16361.87647
gdpPercap_1972    18965.05551
dtype: float64
```

```python
print(data.loc['Italy':'Poland', 'gdpPercap_1962':'gdpPercap_1972'].min())
```

```output
gdpPercap_1962    4649.593785
gdpPercap_1967    5907.850937
gdpPercap_1972    7778.414017
dtype: float64
```

## 값을 기준으로 데이터를 선택하려면 비교를 사용합니다.

- 비교는 요소별로 적용됩니다.
- `True`와 `False`로 구성된 유사한 모양의 데이터프레임을 반환합니다.

```python
# 출력을 읽기 쉽게 유지하기 위해 데이터의 하위 집합을 사용합니다.
subset = data.loc['Italy':'Poland', 'gdpPercap_1962':'gdpPercap_1972']
print('데이터의 하위 집합:\n', subset)

# 어떤 값이 10000보다 컸습니까?
print('\n값이 큰 곳은 어디입니까?\n', subset > 10000)
```

```output
데이터의 하위 집합:
             gdpPercap_1962  gdpPercap_1967  gdpPercap_1972
country
Italy           8243.582340    10022.401310    12269.273780
Montenegro      4649.593785     5907.850937     7778.414017
Netherlands    12790.849560    15363.251360    18794.745670
Norway         13450.401510    16361.876470    18965.055510
Poland          5338.752143     6557.152776     8006.506993

값이 큰 곳은 어디입니까?
            gdpPercap_1962 gdpPercap_1967 gdpPercap_1972
country
Italy                False           True           True
Montenegro           False          False          False
Netherlands           True           True           True
Norway                True           True           True
Poland               False          False          False
```

## 부울 마스크를 사용하여 값 또는 NaN을 선택합니다.

- 부울로 가득 찬 프레임은 사용할 수 있는 방식 때문에 때때로 *마스크*라고 합니다.

```python
mask = subset > 10000
print(subset[mask])
```

```output
             gdpPercap_1962  gdpPercap_1967  gdpPercap_1972
country
Italy                   NaN     10022.40131     12269.27378
Montenegro              NaN             NaN             NaN
Netherlands     12790.84956     15363.25136     18794.74567
Norway          13450.40151     16361.87647     18965.05551
Poland                  NaN             NaN             NaN
```

- 마스크가 참인 곳에서는 값을 가져오고 거짓인 곳에서는 NaN(숫자 아님)을 가져옵니다.
- NaN은 max, min, average 등과 같은 작업에서 무시되기 때문에 유용합니다.

```python
print(subset[subset > 10000].describe())
```

```output
       gdpPercap_1962  gdpPercap_1967  gdpPercap_1972
count        2.000000        3.000000        3.000000
mean     13120.625535    13915.843047    16676.358320
std        466.373656     3408.589070     3817.597015
min      12790.849560    10022.401310    12269.273780
25%      12955.737547    12692.826335    15532.009725
50%      13120.625535    15363.251360    18794.745670
75%      13285.513523    15862.563915    18879.900590
max      13450.401510    16361.876470    18965.055510
```

## 그룹화: 분할-적용-결합

::::::::::::::::::::::::::::::::::::: 강사
학습자들은 종종 여기서 어려움을 겪으며, 많은 사람들이 금융 데이터 및 개념에 익숙하지 않아 예제 개념을 이해하기 어려워합니다. 하지만 가장 큰 문제는 부유 점수를 생성하는 줄입니다. 이 단계는 철저하게 설명해야 합니다.
* 이 과정에서 지금까지 다루지 않은 부울 값과 부동 소수점 값 간의 암시적 변환을 사용합니다.
* axis=1 인수는 명확하게 설명해야 합니다.
:::::::::::::::::::::::::::::::::::::::::::::::::

판다스 벡터화 메서드 및 그룹화 작업은 사용자에게 데이터를 분석할 수 있는 많은 유연성을 제공하는 기능입니다.

예를 들어, 유럽 국가들이 GDP에 따라 어떻게 나뉘는지 더 명확하게 보고 싶다고 가정해 보겠습니다.

1. 조사 기간 동안 국가를 두 그룹으로 나누어 개략적으로 볼 수 있습니다. 유럽 평균보다 *높은* GDP를 보인 국가와 *낮은* GDP를 보인 국가입니다.
2. 그런 다음 1962년부터 2007년까지의 과거 값을 기반으로 *부유 점수*를 추정합니다. 여기서 국가가 *낮은* 또는 *높은* GDP 그룹에 몇 번이나 참여했는지 설명합니다.

```python
mask_higher = data > data.mean()
wealth_score = mask_higher.aggregate('sum', axis=1) / len(data.columns)
print(wealth_score)
```

```output
country
Albania                   0.000000
Austria                   1.000000
Belgium                   1.000000
Bosnia and Herzegovina    0.000000
Bulgaria                  0.000000
Croatia                   0.000000
Czech Republic            0.500000
Denmark                   1.000000
Finland                   1.000000
France                    1.000000
Germany                   1.000000
Greece                    0.333333
Hungary                   0.000000
Iceland                   1.000000
Ireland                   0.333333
Italy                     0.500000
Montenegro                0.000000
Netherlands               1.000000
Norway                    1.000000
Poland                    0.000000
Portugal                  0.000000
Romania                   0.000000
Serbia                    0.000000
Slovak Republic           0.000000
Slovenia                  0.333333
Spain                     0.333333
Sweden                    1.000000
Switzerland               1.000000
Turkey                    0.000000
United Kingdom            1.000000
dtype: float64
```

마지막으로 `wealth_score` 테이블의 각 그룹에 대해 체인 메서드를 사용하여 조사 기간 동안의 (재정적) 기여도를 합산합니다.

```python
print(data.groupby(wealth_score).sum())
```

```output
          gdpPercap_1952  gdpPercap_1957  gdpPercap_1962  gdpPercap_1967  \
0.000000    36916.854200    46110.918793    56850.065437    71324.848786   
0.333333    16790.046878    20942.456800    25744.935321    33567.667670   
0.500000    11807.544405    14505.000150    18380.449470    21421.846200   
1.000000   104317.277560   127332.008735   149989.154201   178000.350040   

          gdpPercap_1972  gdpPercap_1977  gdpPercap_1982  gdpPercap_1987  \
0.000000    88569.346898   104459.358438   113553.768507   119649.599409   
0.333333    45277.839976    53860.456750    59679.634020    64436.912960   
0.500000    25377.727380    29056.145370    31914.712050    35517.678220   
1.000000   215162.343140   241143.412730   263388.781960   296825.131210   

          gdpPercap_1992  gdpPercap_1997  gdpPercap_2002  gdpPercap_2007  
0.000000    92380.047256   103772.937598   118590.929863   149577.357928  
0.333333    67918.093220    80876.051580   102086.795210   122803.729520  
0.500000    36310.666080    40723.538700    45564.308390    51403.028210  
1.000000   315238.235970   346930.926170   385109.939210   427850.333420
```

:::::::::::::::::::::::::::::::::::::::  challenge

## 개별 값 선택

판다스가 노트북으로 가져와졌고 유럽에 대한 갭마인더 GDP 데이터가 로드되었다고 가정합니다.

```python
import pandas as pd

data_europe = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
```

2007년 세르비아의 1인당 GDP를 찾는 표현식을 작성하십시오.

:::::::::::::::  solution

## 해결책

행("Serbia")과 열("gdpPercap_2007") 모두에 대한 레이블을 사용하여 선택을 수행할 수 있습니다.

```python
print(data_europe.loc['Serbia', 'gdpPercap_2007'])
```

출력은 다음과 같습니다.

```output
9786.534714
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 슬라이싱 범위

1. 아래 두 문은 동일한 출력을 생성합니까?
2. 이를 바탕으로 판다스에서 숫자 슬라이스 및 명명된 슬라이스에 포함되는(또는 포함되지 않는) 것을 지배하는 규칙은 무엇입니까?

```python
print(data_europe.iloc[0:2, 0:2])
print(data_europe.loc['Albania':'Belgium', 'gdpPercap_1952':'gdpPercap_1962'])
```

:::::::::::::::  solution

## 해결책

아니요, 동일한 출력을 생성하지 않습니다! 첫 번째 문의 출력은 다음과 같습니다.

```output
        gdpPercap_1952  gdpPercap_1957
country                                
Albania     1601.056136     1942.284244
Austria     6137.076492     8842.598030
```

두 번째 문은 다음과 같습니다.

```output
        gdpPercap_1952  gdpPercap_1957  gdpPercap_1962
country                                                
Albania     1601.056136     1942.284244     2312.888958
Austria     6137.076492     8842.598030    10750.721110
Belgium     8343.105127     9714.960623    10991.206760
```

분명히 두 번째 문은 첫 번째 문에 비해 추가 열과 추가 행을 생성합니다.
어떤 결론을 내릴 수 있습니까? 숫자 슬라이스 0:2는 제공된 범위의 최종 인덱스(즉, 인덱스 2)를 *생략*하는 반면, 명명된 슬라이스 'gdpPercap_1952':'gdpPercap_1962'는 최종 요소를 *포함*한다는 것을 알 수 있습니다.

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 데이터 재구성

다음 짧은 프로그램의 각 줄이 무엇을 하는지 설명하십시오.
`first`, `second` 등에는 무엇이 있습니까?

```python
first = pd.read_csv('data/gapminder_all.csv', index_col='country')
second = first[first['continent'] == 'Americas']
third = second.drop('Puerto Rico')
fourth = third.drop('continent', axis = 1)
fourth.to_csv('result.csv')
```

:::::::::::::::  solution

## 해결책

이 코드를 한 줄씩 살펴보겠습니다.

```python
first = pd.read_csv('data/gapminder_all.csv', index_col='country')
```

이 줄은 모든 국가의 GDP 데이터를 포함하는 데이터 세트를 `first`라는 데이터프레임으로 로드합니다. `index_col='country'` 매개변수는 데이터프레임의 행 레이블로 사용할 열을 선택합니다.

```python
second = first[first['continent'] == 'Americas']
```

이 줄은 선택을 합니다. 'continent' 열이 'Americas'와 일치하는 `first`의 행만 추출됩니다. 괄호 안의 부울 표현식 `first['continent'] == 'Americas'`가 표현식이 참인 행만 선택하는 데 어떻게 사용되는지 확인하십시오.
이 표현식을 인쇄해 보십시오! 개별 True/False 요소도 인쇄할 수 있습니까?
(힌트: 먼저 표현식을 변수에 할당하십시오)

```python
third = second.drop('Puerto Rico')
```

구문에서 알 수 있듯이 이 줄은 레이블이 'Puerto Rico'인 `second`에서 행을 삭제합니다. 결과 데이터프레임 `third`는 원래 데이터프레임 `second`보다 한 행이 적습니다.

```python
fourth = third.drop('continent', axis = 1)
```

다시 drop 함수를 적용하지만 이 경우 행이 아닌 전체 열을 삭제합니다.
이를 수행하려면 `axis` 매개변수도 지정해야 합니다(인덱스 1을 가진 두 번째 열을 삭제하려고 함).

```python
fourth.to_csv('result.csv')
```

마지막 단계는 작업 중인 데이터를 csv 파일에 쓰는 것입니다. 판다스는 `to_csv()` 함수를 사용하여 이를 쉽게 만듭니다. 함수에 필요한 유일한 인수는 파일 이름입니다. 파일은 주피터 또는 파이썬 세션을 시작한 디렉토리에 기록됩니다.

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 인덱스 선택

아래 짧은 프로그램에서 `idxmin`과 `idxmax`가 무엇을 하는지 간단한 용어로 설명하십시오.
이러한 메서드는 언제 사용하시겠습니까?

```python
data = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
print(data.idxmin())
print(data.idxmax())
```

:::::::::::::::  solution

## 해결책

`data`의 각 열에 대해 `idxmin`은 각 열의 최소값에 해당하는 인덱스 값을 반환합니다.
`idxmax`는 각 열의 최대값에 대해 동일한 작업을 수행합니다.

실제 최소/최대값이 아닌 최소/최대값의 행 인덱스를 얻고 싶을 때마다 이러한 함수를 사용할 수 있습니다.

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 선택 연습

판다스가 가져와졌고 유럽에 대한 갭마인더 GDP 데이터가 로드되었다고 가정합니다.
다음을 각각 선택하는 표현식을 작성하십시오.

1. 1982년 모든 국가의 1인당 GDP.
2. 모든 연도의 덴마크 1인당 GDP.
3. 1985년 *이후* 모든 국가의 1인당 GDP.
4. 2007년 각 국가의 1인당 GDP를 해당 국가의 1952년 1인당 GDP의 배수로 표시.

:::::::::::::::  solution

## 해결책

1:

```python
data['gdpPercap_1982']
```

2:

```python
data.loc['Denmark',:]
```

3:

```python
data.loc[:,'gdpPercap_1985':]
```

판다스는 `gdpPercap_1985`라는 열이 실제로 존재하지 않더라도 열 레이블 끝에 있는 숫자를 인식할 만큼 똑똑하며 오류를 발생시키지 않습니다. 이는 나중에 CSV 파일에 새 열이 추가될 경우 유용합니다.

4:

```python
data['gdpPercap_2007']/data['gdpPercap_1952']
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 다양한 액세스 방법

데이터프레임의 값이나 슬라이스에 액세스하는 방법에는 이름 또는 인덱스별로 최소 두 가지 방법이 있습니다.
그러나 다른 많은 방법이 있습니다. 예를 들어 단일 열 또는 행은 `DataFrame` 또는 `Series` 객체로 액세스할 수 있습니다.

데이터프레임에서 다음 작업을 수행하는 다양한 방법을 제안하십시오.

1. 단일 열에 액세스
2. 단일 행에 액세스
3. 개별 데이터프레임 요소에 액세스
4. 여러 열에 액세스
5. 여러 행에 액세스
6. 특정 행과 열의 하위 집합에 액세스
7. 행 및 열 범위의 하위 집합에 액세스

:::::::::::::::  solution

## 해결책

1. 단일 열에 액세스:

```python
# 이름으로
data["col_name"]   # 시리즈로
data[["col_name"]] # 데이터프레임으로

# .loc를 사용하여 이름으로
data.T.loc["col_name"]  # 시리즈로
data.T.loc[["col_name"]].T  # 데이터프레임으로

# 점 표기법(시리즈)
data.col_name

# 인덱스별(iloc)
data.iloc[:, col_index]   # 시리즈로
data.iloc[:, [col_index]] # 데이터프레임으로

# 마스크 사용
data.T[data.T.index == "col_name"].T
```

2. 단일 행에 액세스:

```python
# .loc를 사용하여 이름으로
data.loc["row_name"] # 시리즈로
data.loc[["row_name"]] # 데이터프레임으로

# 이름으로
data.T["row_name"] # 시리즈로
data.T[["row_name"]].T # 데이터프레임으로

# 인덱스별
data.iloc[row_index]   # 시리즈로
data.iloc[[row_index]]   # 데이터프레임으로

# 마스크 사용
data[data.index == "row_name"]
```

3. 개별 데이터프레임 요소에 액세스:

```python
# 열/행 이름으로
data["column_name"]["row_name"]         # 시리즈로

data[["col_name"]].loc["row_name"]  # 시리즈로
data[["col_name"]].loc[["row_name"]]  # 데이터프레임으로

data.loc["row_name"]["col_name"]  # 값으로
data.loc[["row_name"]]["col_name"]  # 시리즈로
data.loc[["row_name"]][["col_name"]]  # 데이터프레임으로

data.loc["row_name", "col_name"]  # 값으로
data.loc[["row_name"], "col_name"]  # 시리즈로. 인덱스 유지. 열 이름이 `.name`으로 이동.
data.loc["row_name", ["col_name"]]  # 시리즈로. 인덱스가 `.name`으로 이동. 인덱스를 열 이름으로 설정.
data.loc[["row_name"], ["col_name"]]  # 데이터프레임으로 (원래 인덱스 및 열 이름 유지)

# 열/행 이름으로: 점 표기법
data.col_name.row_name

# 열/행 인덱스별
data.iloc[row_index, col_index] # 값으로
data.iloc[[row_index], col_index] # 시리즈로. 인덱스 유지. 열 이름이 `.name`으로 이동
data.iloc[row_index, [col_index]] # 시리즈로. 인덱스가 `.name`으로 이동. 인덱스를 열 이름으로 설정.
data.iloc[[row_index], [col_index]] # 데이터프레임으로 (원래 인덱스 및 열 이름 유지)

# 열 이름 + 행 인덱스
data["col_name"][row_index]
data.col_name[row_index]
data["col_name"].iloc[row_index]

# 열 인덱스 + 행 이름
data.iloc[:, [col_index]].loc["row_name"]  # 시리즈로
data.iloc[:, [col_index]].loc[["row_name"]]  # 데이터프레임으로

# 마스크 사용
data[data.index == "row_name"].T[data.T.index == "col_name"].T
```

4. 여러 열에 액세스:

```python
# 이름으로
data[["col1", "col2", "col3"]]
data.loc[:, ["col1", "col2", "col3"]]

# 인덱스별
data.iloc[:, [col1_index, col2_index, col3_index]]
```

5. 여러 행에 액세스

```python
# 이름으로
data.loc[["row1", "row2", "row3"]]

# 인덱스별
data.iloc[[row1_index, row2_index, row3_index]]
```

6. 특정 행과 열의 하위 집합에 액세스

```python
# 이름으로
data.loc[["row1", "row2", "row3"], ["col1", "col2", "col3"]]

# 인덱스별
data.iloc[[row1_index, row2_index, row3_index], [col1_index, col2_index, col3_index]]

# 열 이름 + 행 인덱스
data[["col1", "col2", "col3"]].iloc[[row1_index, row2_index, row3_index]]

# 열 인덱스 + 행 이름
data.iloc[:, [col1_index, col2_index, col3_index]].loc[["row1", "row2", "row3"]]
```

7. 행 및 열 범위의 하위 집합에 액세스

```python
# 이름으로
data.loc["row1":"row2", "col1":"col2"]

# 인덱스별
data.iloc[row1_index:row2_index, col1_index:col2_index]

# 열 이름 + 행 인덱스
data.loc[:, "col1_name":"col2_name"].iloc[row1_index:row2_index]

# 열 인덱스 + 행 이름
data.iloc[:, col1_index:col2_index].loc["row1":"row2"]
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## `dir()` 함수를 사용하여 사용 가능한 메서드 탐색

파이썬에는 데이터 객체에 내장된 사용 가능한 모든 메서드(함수)를 표시하는 데 사용할 수 있는 `dir()` 함수가 포함되어 있습니다. 4장에서는 문자열과 함께 일부 메서드를 사용했습니다. 그러나 `dir()`을 사용하여 더 많은 메서드를 볼 수 있습니다.

```python
my_string = 'Hello world!'   # 문자열 객체 생성
dir(my_string)
```

이 명령은 다음을 반환합니다.

```python
['__add__',
...
'__subclasshook__',
'capitalize',
'casefold',
'center',
...
'upper',
'zfill']
```

`help()` 또는 <kbd>Shift</kbd>+<kbd>Tab</kbd>을 사용하여 이러한 메서드가 무엇을 하는지에 대한 자세한 정보를 얻을 수 있습니다.

판다스가 가져와졌고 유럽에 대한 갭마인더 GDP 데이터가 `data`로 로드되었다고 가정합니다. 그런 다음 `dir()`을 사용하여 정보가 있는 각 연도에 대해 모든 유럽 국가의 1인당 GDP 중앙값을 인쇄하는 함수를 찾으십시오.

:::::::::::::::  solution

## 해결책

많은 선택 사항 중에서 `dir()`은 `median()` 함수를 가능성으로 나열합니다. 따라서,

```python
data.median()
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 해석

폴란드의 국경은 1945년 이후 안정되었지만 그 이전 몇 년 동안 여러 번 변경되었습니다.
20세기 전체에 대한 폴란드의 1인당 GDP 표를 만들고 있다면 이것을 어떻게 처리하시겠습니까?

::::::::::::::::::::::::::::::::::::::::::::::::::

[pandas-dataframe]: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html
[pandas-series]: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.html
[numpy]: https://www.numpy.org/


:::::::::::::::::::::::::::::::::::::::: keypoints

- `DataFrame.iloc[..., ...]`를 사용하여 정수 위치별로 값을 선택합니다.
- 모든 열 또는 모든 행을 의미하려면 `:`를 단독으로 사용합니다.
- `DataFrame.loc` 및 명명된 슬라이스를 사용하여 여러 열 또는 행을 선택합니다.
- 슬라이싱 결과는 추가 작업에 사용할 수 있습니다.
- 값을 기준으로 데이터를 선택하려면 비교를 사용합니다.
- 부울 마스크를 사용하여 값 또는 NaN을 선택합니다.

::::::::::::::::::::::::::::::::::::::::::::::::::