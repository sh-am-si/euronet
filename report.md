# Data

The data consists of three columns

|   column	    |   count	|   unique	|   nan	|   range	|
|---	        |---	    |---	    |---	|---	|
|  Atm       	|   8942	|   9    |  0 	|  ATM1 - ATM9 	|
|  ProcessDate 	|   8942	|   1034	|   0	|  2017-01-01 - 2019-10-31 	|
|  Withdrawal 	|   8942	|   	|   0	|   20 - 191210	|

The minimal withdrawal ammount is 20 PLN.

## Withdrawal

|       | Withdrawal |
| :---- | ---------: |
| count |       8942 |
| mean  |    25271.2 |
| std   |    19715.9 |
| min   |         20 |
| 25%   |       9960 |
| 50%   |      21325 |
| 75%   |      36935 |
| max   |     191210 |

## Values by ATM

```python3
df.groupby('Atm').agg(['min', 'max', 'count'])
```

| Atm  | ProcessDate, min | ProcessDate, max | Withdrawal, min | Withdrawal, max | count |
| :--- | :--------------- | :--------------- | --------------: | --------------: | ----: |
| ATM1 | 2017-01-02       | 2019-10-31       |              20 |           93060 |   883 |
| ATM2 | 2017-01-01       | 2019-10-31       |             570 |           97120 |  1034 |
| ATM3 | 2017-01-01       | 2019-10-31       |              50 |           72940 |  1029 |
| ATM4 | 2017-01-01       | 2019-10-31       |             200 |           85530 |  1028 |
| ATM5 | 2017-01-01       | 2019-10-31       |              80 |           73080 |  1030 |
| ATM6 | 2017-01-01       | 2019-10-31       |             300 |           84450 |  1031 |
| ATM7 | 2017-01-02       | 2019-10-31       |             150 |           50790 |   941 |
| ATM8 | 2017-01-01       | 2019-10-31       |              20 |          191210 |  1018 |
| ATM9 | 2017-01-02       | 2019-10-31       |            2590 |           83700 |   948 |


## Index continiuty

|      | missing days |
| :--- | -----------: |
| ATM1 |          150 |
| ATM2 |            0 |
| ATM3 |            5 |
| ATM4 |            6 |
| ATM5 |            4 |
| ATM6 |            3 |
| ATM7 |           92 |
| ATM8 |           16 |
| ATM9 |           85 |

### Discontiniuty by week day

|      | ATM1 | ATM2 | ATM3 | ATM4 | ATM5 | ATM6 | ATM7 | ATM8 | ATM9 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
|    0 |    7 |  nan |  nan |  nan |  nan |    1 |    9 |    7 |    7 |
|    1 |    5 |  nan |    1 |    2 |  nan |  nan |    7 |    5 |    5 |
|    2 |    5 |  nan |  nan |    2 |  nan |  nan |    5 |    1 |    5 |
|    3 |    6 |  nan |  nan |    2 |    2 |  nan |    6 |    2 |    6 |
|    4 |    2 |  nan |  nan |  nan |    1 |  nan |    2 |  nan |    2 |
|    5 |    2 |  nan |    1 |  nan |    1 |  nan |    3 |  nan |    3 |
|    6 |  123 |  nan |    3 |  nan |  nan |    2 |   60 |    1 |   57 |

It is evident that missing days mostly coincide with Sundays. It seems those dates indicate zero withdrawals.
Therefore missing dates were replaced by zero values.


## Histograms by ATM

### All ATMs

![All ATMS](.pics/../pics/by_atm/hist.png)

### ATM1 

![ATM1](.pics/../pics/by_atm/hist_ATM1.png)

### ATM2 

![ATM2](.pics/../pics/by_atm/hist_ATM2.png)


### ATM3 

![ATM3](.pics/../pics/by_atm/hist_ATM3.png)

### ATM4

![ATM4](.pics/../pics/by_atm/hist_ATM4.png)

### ATM5 

![ATM5](.pics/../pics/by_atm/hist_ATM5.png)

### ATM6 

![ATM6](.pics/../pics/by_atm/hist_ATM6.png)

### ATM7

![ATM7](.pics/../pics/by_atm/hist_ATM7.png)

### ATM8 

![ATM8](.pics/../pics/by_atm/hist_ATM8.png)

### ATM9 

![ATM9](.pics/../pics/by_atm/hist_ATM9.png)

## Withdrawal by Weekday

![Distribution by weekday](./pics/ts_by_weekday.png)

## Withdrawal by Month 

![Distribution by months](./pics/ts_by_month.png)

## Withdrawal by Year 

![Distribution by years](./pics/ts_by_year.png)

## Withdrawal all times 

![Withdrawal all times](./pics/ts_all_times.png)

## Boxplot

![Boxplot](./pics/boxplot.png)

|      |   count |    mean |      std |   min |     25% |   50% |     75% |    max |
|:-----|--------:|--------:|---------:|------:|--------:|------:|--------:|-------:|
| ATM1 |    1034 | 30293.3 | 18679.7  |     0 | 14157.5 | 35100 | 43535   |  93060 |
| ATM2 |    1034 | 21134.5 | 18756.4  |   570 |  7165   | 14495 | 29485   |  97120 |
| ATM3 |    1034 | 25271.4 | 12840.9  |     0 | 15640   | 24410 | 33087.5 |  72940 |
| ATM4 |    1034 | 25797.2 | 16771.7  |     0 | 11462.5 | 22485 | 38290   |  85530 |
| ATM5 |    1034 | 14954.9 | 12569.3  |     0 |  6212.5 | 10755 | 19732.5 |  73080 |
| ATM6 |    1034 | 34208.1 | 15086.3  |     0 | 26010   | 35530 | 43690   |  84450 |
| ATM7 |    1034 | 12958.8 |  8267.86 |     0 |  7342.5 | 12280 | 17665   |  50790 |
| ATM8 |    1034 | 24331   | 36563    |     0 |  1800   |  7005 | 25685   | 191210 |
| ATM9 |    1034 | 29595.2 | 15854.3  |     0 | 19437.5 | 29955 | 39727.5 |  83700 |

## Autocorrelation

### ATM1 

![autocorrelation ATM1](./pics/autocorr/ATM1.png)

### ATM2 

![autocorrelation ATM2](./pics/autocorr/ATM2.png)

### One day lag

![One day lag](./pics/lags/ATM2_lag_1.png)

### ATM3 

![autocorrelation ATM3](./pics/autocorr/ATM3.png)

### ATM4

![autocorrelation ATM4](./pics/autocorr/ATM4.png)

### One day lag

![One day lag](./pics/lags/ATM4_lag_1.png)

### ATM5 

![autocorrelation ATM5](./pics/autocorr/ATM5.png)

### One day lag

![One day lag](./pics/lags/ATM5_lag_1.png)

### ATM6 

![autocorrelation ATM6](./pics/autocorr/ATM6.png)

### ATM7 

![autocorrelation ATM7](./pics/autocorr/ATM7.png)

### ATM8 

![autocorrelation ATM8](./pics/autocorr/ATM8.png)

### One day lag

![One day lag](./pics/lags/ATM8_lag_1.png)

### ATM9 

![autocorrelation ATM9](./pics/autocorr/ATM9.png)

# Summary

|      |   Season |    Week |     Comment |   
|:-----|--------:|--------:|---------:|
| ATM1 |    None | Yes | Essential withdrawal decay at Sundays  |  
| ATM2 |    Summer | Yes |  | 
| ATM3 |    None | Yes |  | 
| ATM4 |    Winter, Summer | Yes | Withdrawal increase in Saturdays |  
| ATM5 |    Summer | Yes |  | 
| ATM6 |    None | Yes |   |  
| ATM7 |    None| Yes|  |  
| ATM8 |    Winter, Summer| Yes   |   |   
| ATM9 |    None | Yes |  | 
