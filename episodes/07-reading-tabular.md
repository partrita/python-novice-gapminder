---
title: 표 형식 데이터를 데이터프레임으로 읽기
teaching: 10
exercises: 10
---

::::::::::::::::::::::::::::::::::::::: objectives

- Pandas 라이브러리를 가져옵니다.
- Pandas를 사용하여 간단한 CSV 데이터 세트를 로드합니다.
- Pandas 데이터프레임에 대한 몇 가지 기본 정보를 얻습니다.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- 표 형식 데이터는 어떻게 읽을 수 있나요?

::::::::::::::::::::::::::::::::::::::::::::::::::

## Pandas 라이브러리를 사용하여 표 형식 데이터에 대한 통계를 수행합니다.

- [Pandas](https://pandas.pydata.org/)는 통계, 특히 표 형식 데이터에 널리 사용되는 파이썬 라이브러리입니다.
- R의 데이터프레임에서 많은 기능을 차용했습니다.
  - 열에 이름이 있고 잠재적으로 다른 데이터 유형을 가질 수 있는 2차원 테이블입니다.
- `import pandas as pd`로 Pandas를 로드합니다. 별칭 `pd`는 코드에서 Pandas 라이브러리를 참조하는 데 일반적으로 사용됩니다.
- `pd.read_csv`로 쉼표로 구분된 값(CSV) 데이터 파일을 읽습니다.
  - 인수는 읽을 파일의 이름입니다.
  - 변수에 할당할 수 있는 데이터프레임을 반환합니다.

```python
import pandas as pd

data_oceania = pd.read_csv('data/gapminder_gdp_oceania.csv')
print(data_oceania)
```

```output
       country  gdpPercap_1952  gdpPercap_1957  gdpPercap_1962  \
0    Australia     10039.59564     10949.64959     12217.22686
1  New Zealand     10556.57566     12247.39532     13175.67800

   gdpPercap_1967  gdpPercap_1972  gdpPercap_1977  gdpPercap_1982  \
0     14526.12465     16788.62948     18334.19751     19477.00928
1     14463.91893     16046.03728     16233.71770     17632.41040

   gdpPercap_1987  gdpPercap_1992  gdpPercap_1997  gdpPercap_2002  \
0     21888.88903     23424.76683     26997.93657     30687.75473
1     19007.19129     18363.32494     21050.41377     23189.80135

   gdpPercap_2007
0     34435.36744
1     25185.00911
```

- 데이터프레임의 열은 관찰된 변수이고 행은 관찰입니다.
- Pandas는 출력이 화면에 맞지 않을 때 줄 바꿈된 줄을 표시하기 위해 백슬래시 `\`를 사용합니다.
- 설명적인 데이터프레임 이름을 사용하면 여러 데이터프레임을 구별하는 데 도움이 되므로 실수로 데이터프레임을 덮어쓰거나 잘못된 데이터프레임에서 읽는 것을 방지할 수 있습니다.

:::::::::::::::::::::::::::::::::::::::::  callout

## 파일을 찾을 수 없음

우리 수업은 데이터 파일을 `data` 하위 디렉토리에 저장하므로 파일 경로는 `data/gapminder_gdp_oceania.csv`입니다.
`data/`를 포함하는 것을 잊어버리거나, 포함했지만 파일 복사본이 다른 곳에 있는 경우 다음과 같은 줄로 끝나는 [런타임 오류](04-built-in.md)가 발생합니다.

```error
FileNotFoundError: [Errno 2] No such file or directory: 'data/gapminder_gdp_oceania.csv'
```

::::::::::::::::::::::::::::::::::::::::::::::::::

## `index_col`을 사용하여 열의 값을 행 머리글로 사용해야 함을 지정합니다.

- 행 머리글은 숫자입니다(이 경우 0과 1).
- 실제로 국가별로 인덱싱하고 싶습니다.
- 이를 위해 `read_csv`에 열 이름을 `index_col` 매개변수로 전달합니다.
- 데이터프레임 이름을 `data_oceania_country`로 지정하면 데이터가 포함된 지역(`oceania`)과 인덱싱 방법(`country`)을 알 수 있습니다.

```python
data_oceania_country = pd.read_csv('data/gapminder_gdp_oceania.csv', index_col='country')
print(data_oceania_country)
```

```output
             gdpPercap_1952  gdpPercap_1957  gdpPercap_1962  gdpPercap_1967  \
country
Australia       10039.59564     10949.64959     12217.22686     14526.12465
New Zealand     10556.57566     12247.39532     13175.67800     14463.91893

             gdpPercap_1972  gdpPercap_1977  gdpPercap_1982  gdpPercap_1987  \
country
Australia       16788.62948     18334.19751     19477.00928     21888.88903
New Zealand     16046.03728     16233.71770     17632.41040     19007.19129

             gdpPercap_1992  gdpPercap_1997  gdpPercap_2002  gdpPercap_2007
country
Australia       23424.76683     26997.93657     30687.75473     34435.36744
New Zealand     18363.32494     21050.41377     23189.80135     25185.00911
```

## `DataFrame.info()` 메서드를 사용하여 데이터프레임에 대해 자세히 알아봅니다.

```python
data_oceania_country.info()
```

```output
<class 'pandas.core.frame.DataFrame'>
Index: 2 entries, Australia to New Zealand
Data columns (total 12 columns):
gdpPercap_1952    2 non-null float64
gdpPercap_1957    2 non-null float64
gdpPercap_1962    2 non-null float64
gdpPercap_1967    2 non-null float64
gdpPercap_1972    2 non-null float64
gdpPercap_1977    2 non-null float64
gdpPercap_1982    2 non-null float64
gdpPercap_1987    2 non-null float64
gdpPercap_1992    2 non-null float64
gdpPercap_1997    2 non-null float64
gdpPercap_2002    2 non-null float64
gdpPercap_2007    2 non-null float64
dtypes: float64(12)
memory usage: 208.0+ bytes
```

- 이것은 `DataFrame`입니다.
- `'Australia'`와 `'New Zealand'`라는 이름의 두 행
- 12개의 열, 각각 2개의 실제 64비트 부동 소수점 값을 가짐.
  - 나중에 누락된 관측치를 나타내는 데 사용되는 null 값에 대해 이야기하겠습니다.
- 208바이트의 메모리를 사용합니다.

## `DataFrame.columns` 변수는 데이터프레임의 열에 대한 정보를 저장합니다.

- 이것은 메서드가 아닌 데이터입니다. (괄호가 없습니다.)
  - `math.pi`와 같습니다.
  - 따라서 호출하려고 `()`를 사용하지 마십시오.
- *멤버 변수* 또는 그냥 *멤버*라고 합니다.

```python
print(data_oceania_country.columns)
```

```output
Index(['gdpPercap_1952', 'gdpPercap_1957', 'gdpPercap_1962', 'gdpPercap_1967',
       'gdpPercap_1972', 'gdpPercap_1977', 'gdpPercap_1982', 'gdpPercap_1987',
       'gdpPercap_1992', 'gdpPercap_1997', 'gdpPercap_2002', 'gdpPercap_2007'],
      dtype='object')
```

## `DataFrame.T`를 사용하여 데이터프레임을 전치합니다.

- 때로는 열을 행으로, 행을 열로 처리하고 싶을 때가 있습니다.
- 전치( `.T`로 작성)는 데이터를 복사하지 않고 프로그램의 보기만 변경합니다.
- `columns`와 마찬가지로 멤버 변수입니다.

```python
print(data_oceania_country.T)
```

```output
country           Australia  New Zealand
gdpPercap_1952  10039.59564  10556.57566
gdpPercap_1957  10949.64959  12247.39532
gdpPercap_1962  12217.22686  13175.67800
gdpPercap_1967  14526.12465  14463.91893
gdpPercap_1972  16788.62948  16046.03728
gdpPercap_1977  18334.19751  16233.71770
gdpPercap_1982  19477.00928  17632.41040
gdpPercap_1987  21888.88903  19007.19129
gdpPercap_1992  23424.76683  18363.32494
gdpPercap_1997  26997.93657  21050.41377
gdpPercap_2002  30687.75473  23189.80135
gdpPercap_2007  34435.36744  25185.00911
```

## `DataFrame.describe()`를 사용하여 데이터에 대한 요약 통계를 얻습니다.

`DataFrame.describe()`는 숫자 데이터가 있는 열의 요약 통계만 가져옵니다.
`include='all'` 인수를 사용하지 않는 한 다른 모든 열은 무시됩니다.

```python
print(data_oceania_country.describe())
```

```output
       gdpPercap_1952  gdpPercap_1957  gdpPercap_1962  gdpPercap_1967  \
count        2.000000        2.000000        2.000000        2.000000
mean     10298.085650    11598.522455    12696.452430    14495.021790
std        365.560078      917.644806      677.727301       43.986086
min      10039.595640    10949.649590    12217.226860    14463.918930
25%      10168.840645    11274.086022    12456.839645    14479.470360
50%      10298.085650    11598.522455    12696.452430    14495.021790
75%      10427.330655    11922.958888    12936.065215    14510.573220
max      10556.575660    12247.395320    13175.678000    14526.124650

       gdpPercap_1972  gdpPercap_1977  gdpPercap_1982  gdpPercap_1987  \
count         2.00000        2.000000        2.000000        2.000000
mean      16417.33338    17283.957605    18554.709840    20448.040160
std         525.09198     1485.263517     1304.328377     2037.668013
min       16046.03728    16233.717700    17632.410400    19007.191290
25%       16231.68533    16758.837652    18093.560120    19727.615725
50%       16417.33338    17283.957605    18554.709840    20448.040160
75%       16602.98143    17809.077557    19015.859560    21168.464595
max       16788.62948    18334.197510    19477.009280    21888.889030

       gdpPercap_1992  gdpPercap_1997  gdpPercap_2002  gdpPercap_2007
count        2.000000        2.000000        2.000000        2.000000
mean     20894.045885    24024.175170    26938.778040    29810.188275
std       3578.979883     4205.533703     5301.853680     6540.991104
min      18363.324940    21050.413770    23189.801350    25185.009110
25%      19628.685413    22537.294470    25064.289695    27497.598692
50%      20894.045885    24024.175170    26938.778040    29810.188275
75%      22159.406358    25511.055870    28813.266385    32122.777857
max      23424.766830    26997.936570    30687.754730    34435.367440
```

- 두 개의 레코드만으로는 특별히 유용하지 않지만 수천 개가 있을 때는 매우 유용합니다.

:::::::::::::::::::::::::::::::::::::::  challenge

## 다른 데이터 읽기

`gapminder_gdp_americas.csv`( `gapminder_gdp_oceania.csv`와 동일한 디렉토리에 있어야 함)의 데이터를 `data_americas`라는 변수로 읽고 요약 통계를 표시합니다.

:::::::::::::::  solution

## 해결책

CSV를 읽으려면 `pd.read_csv`를 사용하고 파일 이름 `'data/gapminder_gdp_americas.csv'`를 전달합니다.
또한 국가별로 인덱싱하기 위해 매개변수 `index_col`에 열 이름 `'country'`를 다시 전달합니다.
요약 통계는 `DataFrame.describe()` 메서드로 표시할 수 있습니다.

```python
data_americas = pd.read_csv('data/gapminder_gdp_americas.csv', index_col='country')
data_americas.describe()
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 데이터 검사

아메리카 대륙의 데이터를 읽은 후 `help(data_americas.head)` 및 `help(data_americas.tail)`를 사용하여 `DataFrame.head` 및 `DataFrame.tail`이 무엇을 하는지 알아보십시오.

1. 이 데이터의 처음 세 행을 표시하는 메서드 호출은 무엇입니까?
2. 이 데이터의 마지막 세 열을 표시하는 메서드 호출은 무엇입니까?
  (힌트: 데이터 보기를 변경해야 할 수도 있습니다.)

:::::::::::::::  solution

## 해결책

1. `data_americas.head()`를 실행하여 `data_americas`의 처음 다섯 행을 확인할 수 있습니다.
  이를 통해 데이터프레임의 시작 부분을 볼 수 있습니다. `data_americas.head()` 호출에서 매개변수 `n`을 지정하여 보고 싶은 행 수를 지정할 수 있습니다.
  처음 세 행을 보려면 다음을 실행하십시오.
  
  ```python
  data_americas.head(n=3)
  ```
  
  ```output
            continent  gdpPercap_1952  gdpPercap_1957  gdpPercap_1962  \
  country
  Argentina  Americas     5911.315053     6856.856212     7133.166023
  Bolivia    Americas     2677.326347     2127.686326     2180.972546
  Brazil     Americas     2108.944355     2487.365989     3336.585802
  
            gdpPercap_1967  gdpPercap_1972  gdpPercap_1977  gdpPercap_1982  \
  country
  Argentina     8052.953021     9443.038526    10079.026740     8997.897412
  Bolivia       2586.886053     2980.331339     3548.097832     3156.510452
  Brazil        3429.864357     4985.711467     6660.118654     7030.835878
  
             gdpPercap_1987  gdpPercap_1992  gdpPercap_1997  gdpPercap_2002  \
  country
  Argentina     9139.671389     9308.418710    10967.281950     8797.640716
  Bolivia       2753.691490     2961.699694     3326.143191     3413.262690
  Brazil        7807.095818     6950.283021     7957.980824     8131.212843
  
             gdpPercap_2007
  country
  Argentina    12779.379640
  Bolivia       3822.137084
  Brazil        9065.800825
  ```

2. `data_americas`의 마지막 세 행을 확인하려면 위에서 사용한 `head()`와 유사하게 `americas.tail(n=3)` 명령을 사용합니다. 그러나 여기서는 마지막 세 열을 보려고 하므로 보기를 변경한 다음 `tail()`을 사용해야 합니다. 그렇게 하려면 행과 열이 바뀐 새 데이터프레임을 만듭니다.
  
  ```python
  americas_flipped = data_americas.T
  ```
  
  그런 다음 `americas_flipped`의 마지막 세 행을 봄으로써 `americas`의 마지막 세 열을 볼 수 있습니다.
  
  ```python
  americas_flipped.tail(n=3)
  ```
  
  ```output
  country        Argentina  Bolivia   Brazil   Canada    Chile Colombia  \
  gdpPercap_1997   10967.3  3326.14  7957.98  28954.9  10118.1  6117.36
  gdpPercap_2002   8797.64  3413.26  8131.21    33329  10778.8  5755.26
  gdpPercap_2007   12779.4  3822.14   9065.8  36319.2  13171.6  7006.58
  
  country        Costa Rica     Cuba Dominican Republic  Ecuador    ...     \
  gdpPercap_1997    6677.05  5431.99             3614.1  7429.46    ...
  gdpPercap_2002    7723.45  6340.65            4563.81  5773.04    ...
  gdpPercap_2007    9645.06   8948.1            6025.37  6873.26    ...
  
  country          Mexico Nicaragua   Panama Paraguay     Peru Puerto Rico  \
  gdpPercap_1997   9767.3   2253.02  7113.69   4247.4  5838.35     16999.4
  gdpPercap_2002  10742.4   2474.55  7356.03  3783.67  5909.02     18855.6
  gdpPercap_2007  11977.6   2749.32  9809.19  4172.84  7408.91     19328.7
  
  country        Trinidad and Tobago United States  Uruguay Venezuela
  gdpPercap_1997             8792.57       35767.4  9230.24   10165.5
  gdpPercap_2002             11460.6       39097.1     7727   8605.05
  gdpPercap_2007             18008.5       42951.7  10611.5   11415.8
  ```
  
  이렇게 하면 원하는 데이터가 표시되지만 세 행 대신 세 열을 표시하는 것을 선호할 수 있으므로 다시 뒤집을 수 있습니다.
  
  ```python
  americas_flipped.tail(n=3).T    
  ```
  
  **참고:** 명령을 '연결'하여 한 줄의 코드로 위의 작업을 수행할 수 있습니다.
  
  ```python
  data_americas.T.tail(n=3).T
  ```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 다른 디렉토리의 파일 읽기

현재 프로젝트의 데이터는 `field_data`라는 폴더에 있는 `microbes.csv`라는 파일에 저장되어 있습니다.
`thesis`라는 형제 폴더의 `analysis.ipynb`라는 노트북에서 분석을 수행하고 있습니다.

```output
your_home_directory
+-- field_data/
|   +-- microbes.csv
+-- thesis/
    +-- analysis.ipynb
```

`analysis.ipynb`에서 `microbes.csv`를 읽기 위해 `read_csv`에 어떤 값을 전달해야 합니까?

:::::::::::::::  solution

## 해결책

`pd.read_csv` 호출에서 관심 있는 파일의 경로를 지정해야 합니다. 먼저 `../`를 사용하여 `thesis` 폴더에서 '점프'한 다음 'field_data/'를 사용하여 `field_data` 폴더로 들어가야 합니다. 그런 다음 파일 이름 `microbes.csv`를 지정할 수 있습니다.
결과는 다음과 같습니다.

```python
data_microbes = pd.read_csv('../field_data/microbes.csv')
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## 데이터 쓰기

파일에서 데이터를 읽기 위한 `read_csv` 함수뿐만 아니라 Pandas는 데이터프레임을 파일에 쓰기 위한 `to_csv` 함수를 제공합니다.
파일에서 읽는 것에 대해 배운 내용을 적용하여 데이터프레임 중 하나를 `processed.csv`라는 파일에 쓰십시오.
`help`를 사용하여 `to_csv` 사용 방법에 대한 정보를 얻을 수 있습니다.

:::::::::::::::  solution

## 해결책

`data_americas` 데이터프레임을 `processed.csv`라는 파일에 쓰려면 다음 명령을 실행하십시오.

```python
data_americas.to_csv('processed.csv')
```

`read_csv` 또는 `to_csv`에 대한 도움말을 보려면 예를 들어 다음을 실행할 수 있습니다.

```python
help(data_americas.to_csv)
help(pd.read_csv)
```

`help(to_csv)` 또는 `help(pd.to_csv)`는 오류를 발생시킵니다! 이는 `to_csv`가 전역 Pandas 함수가 아니라 데이터프레임의 멤버 함수라는 사실 때문입니다. 즉, 데이터프레임의 인스턴스에서만 호출할 수 있습니다.
예: `data_americas.to_csv` 또는 `data_oceania.to_csv`

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- Pandas 라이브러리를 사용하여 표 형식 데이터에서 기본 통계를 얻습니다.
- `index_col`을 사용하여 열의 값을 행 머리글로 사용해야 함을 지정합니다.
- `DataFrame.info`를 사용하여 데이터프레임에 대해 자세히 알아봅니다.
- `DataFrame.columns` 변수는 데이터프레임의 열에 대한 정보를 저장합니다.
- `DataFrame.T`를 사용하여 데이터프레임을 전치합니다.
- `DataFrame.describe`를 사용하여 데이터에 대한 요약 통계를 얻습니다.

::::::::::::::::::::::::::::::::::::::::::::::::::