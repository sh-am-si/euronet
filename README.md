# TASK

# DATA

## shape

- x_train:  (8437, 114)
- x_test:  (1428, 114)
- y_train:  (8437, 3)
- y_test:  (1428, 3)

## dtypes

### x_train, x_test
| name      | type   |
| --------- | ------ |
| key       | int64  |
| date      | object |
| x1 - x112 | object |

### y_test
| name | type   |
| ---- | ------ |
| key  | int64  |
| date | object |
| y    | object |

### y_train 
| name | type                                     |
| ---- | ---------------------------------------- |
| key  | int64                                    |
| date | object                                   |
| y    | float64 (EMPTY template for predictions) |

## Suspicious data

### Zero, NaN, repeating values *x_train*

The dataset consists of continious data in the all columns x1-x112. Therefore repeating values seem to be dubious.

|      | zero |  nan | repeating |
| :--- | ---: | ---: | --------: |
| x1   | 6104 |  637 |      6741 |
| x2   | 6082 |  644 |      6726 |
| x3   | 6114 |  640 |      6754 |
| x4   | 6118 |  642 |      6760 |
| x5   |  271 | 5561 |      5832 |
| x6   |  262 | 5531 |      5793 |
| x7   |   28 |  657 |       685 |
| x8   |   27 |  657 |       684 |
| x9   |   48 |  637 |       685 |
| x10  |   23 |  650 |       971 |
| x11  |  266 | 5569 |      5835 |
| x12  | 1465 |  635 |      2100 |
| x13  |   72 |  637 |       709 |
| x14  | 2413 |  635 |      3048 |
| x15  |   27 |  660 |       687 |
| x16  |   44 |  642 |       686 |
| x17  |  198 | 6392 |      6686 |
| x18  |  278 | 5554 |      5832 |
| x19  | 1482 |  640 |      2122 |
| x20  |   68 |  642 |       710 |
| x21  | 2451 |  641 |      3092 |
| x22  | 2457 |  633 |      3340 |
| x23  |   51 |  637 |       688 |
| x24  | 6121 |  637 |      6758 |
| x25  |  269 | 5519 |      5788 |
| x26  | 1479 |  635 |      2114 |
| x27  |   71 |  637 |       708 |
| x28  | 2427 |  635 |      3062 |
| x29  |   27 |  652 |       679 |
| x30  |   47 |  633 |       680 |
| x31  | 6124 |  633 |      6757 |
| x32  |  272 | 5553 |      5825 |
| x33  | 1482 |  632 |      2114 |
| x34  |   77 |  633 |       710 |
| x35  | 2457 |  633 |      3090 |
| x36  |   27 |  659 |       686 |
| x37  |   47 |  640 |       687 |
| x38  | 6102 |  640 |      6742 |
| x39  |  268 | 5541 |      5809 |
| x40  | 1489 |  638 |      2127 |
| x41  |   73 |  640 |       713 |
| x42  | 2450 |  638 |      3088 |
| x43  |   24 |  657 |       681 |
| x44  |   43 |  640 |       683 |
| x45  | 6137 |  634 |      6771 |
| x46  |  270 | 5553 |      5823 |
| x47  | 1471 |  636 |      2107 |
| x48  |   70 |  640 |       710 |
| x49  | 2428 |  638 |      3066 |
| x50  |   27 |  648 |       675 |
| x51  |   45 |  631 |       676 |
| x52  | 6118 |  631 |      6749 |
| x53  |  262 | 5568 |      5830 |
| x54  | 1455 |  633 |      2088 |
| x55  |   72 |  631 |       703 |
| x56  | 2420 |  633 |      3053 |
| x57  |   24 |  653 |       677 |
| x58  |   47 |  633 |       680 |
| x59  | 6113 |  633 |      6746 |
| x60  |  271 | 5550 |      5821 |
| x61  | 1447 |  629 |      2076 |
| x62  |   69 |  633 |       702 |
| x63  | 2456 |  632 |      3088 |
| x64  |   25 |  645 |       670 |
| x65  |   47 |  627 |       674 |
| x66  | 6084 |  627 |      6711 |
| x67  |  267 | 5569 |      5836 |
| x68  | 1450 |  628 |      2078 |
| x69  |   73 |  627 |       700 |
| x70  | 2434 |  627 |      3061 |
| x71  |   23 |  645 |       668 |
| x72  |   46 |  626 |       672 |
| x73  | 6108 |  626 |      6734 |
| x74  |  261 | 5568 |      5829 |
| x75  | 1454 |  624 |      2078 |
| x76  |   72 |  626 |       698 |
| x77  | 2435 |  625 |      3060 |
| x78  |   26 |  638 |       664 |
| x79  |   42 |  623 |       665 |
| x80  | 6131 |  623 |      6754 |
| x81  |  255 | 5575 |      5830 |
| x82  | 1480 |  622 |      2102 |
| x83  |   68 |  623 |       691 |
| x84  | 2427 |  623 |      3050 |
| x85  |   24 |  661 |       685 |
| x86  |   44 |  642 |       686 |
| x87  | 6105 |  642 |      6747 |
| x88  |   66 |  634 |      1028 |
| x89  | 1449 |  640 |      2089 |
| x90  |   70 |  642 |       712 |
| x91  | 2406 |  641 |      3047 |
| x92  |   24 |  654 |       678 |
| x93  |   45 |  637 |       682 |
| x94  | 6113 |  637 |      6750 |
| x95  |  264 | 5566 |      5830 |
| x96  | 1453 |  635 |      2088 |
| x97  |   68 |  637 |       705 |
| x98  | 2430 |  636 |      3066 |
| x99  |   27 |  664 |       691 |
| x100 |   49 |  644 |       693 |
| x101 |   42 |  634 |       961 |
| x102 |  267 | 5599 |      5866 |
| x103 | 1450 |  640 |      2090 |
| x104 |   70 |  644 |       714 |
| x105 | 2453 |  641 |      3094 |
| x106 |   23 |  641 |       664 |
| x107 |   46 |  620 |       666 |
| x108 | 6137 |  620 |      6757 |
| x109 | 1463 |  632 |      2712 |
| x110 | 1469 |  617 |      2086 |
| x111 |   73 |  620 |       693 |
| x112 | 2454 |  619 |      3073 |

Every single row and column contain NaN value.

```python
wo_nan0 = x_train_df.dropna(axis=0)
wo_nan0.shape == (0, 114)
```

```python
wo_nan1 = x_train_df.dropna(axis=1)
wo_nan1.shape == (8437, 2) # only 'key' and 'date' columns
```

### Repeating values *y_train*

```python
yrv = y_train_df["y"].value_counts()
yrv[yrv > 1].index
```

|      value |    y |
| ---------: | ---: |
|     0.0000 |  130 |
| 10000.0000 |   71 |
|  2444.4444 |    9 |
|  2666.6667 |    6 |
|  3111.1111 |    6 |
|  2222.2222 |    6 |
|  1777.7778 |    5 |
|  3777.7778 |    5 |
|  2888.8889 |    4 |
|   586.9793 |    4 |
|  4000.0000 |    4 |
|  1555.5556 |    4 |
|  3555.5556 |    4 |
|  1383.9462 |    3 |
|  3021.6735 |    3 |
|  2000.0000 |    3 |
|  1333.3333 |    3 |
|  3333.3333 |    3 |
|  5000.0000 |    2 |
|  1107.1570 |    2 |
|   444.4444 |    2 |
|   460.4279 |    2 |
|  1146.6983 |    2 |
|   593.1198 |    2 |
|  1344.4049 |    2 |
|  2807.4338 |    2 |
|  1700.2768 |    2 |
|  2570.1858 |    2 |
|  1067.6157 |    2 |
|  2685.8536 |    2 |
|  2214.3140 |    2 |
|   222.2222 |    2 |
|  3084.2230 |    2 |
|  1426.5290 |    2 |
|  1739.8181 |    2 |
|  2259.8222 |    2 |
|  1660.7355 |    2 |
|  1726.2846 |    2 |
|   303.7405 |    2 |
|  4448.9080 |    2 |
|  3433.7827 |    2 |
|  4726.4841 |    2 |
|  5322.1656 |    2 |
|   888.8889 |    2 |
|  3451.1435 |    2 |
|  2635.9911 |    2 |
|  2308.0562 |    2 |
|  4666.6667 |    2 |
|   666.5863 |    2 |
|  2098.1688 |    2 |
|  1916.4038 |    2 |
|  1720.3714 |    2 |
|   355.8719 |    2 |
|  1463.0289 |    2 |
|   237.2479 |    2 |
|  1557.2125 |    2 |
|   790.8264 |    2 |
|   672.2025 |    2 |
|  4557.5097 |    2 |
|   293.1369 |    2 |
|  2727.8311 |    2 |
|  5266.6638 |    1 |
|        ... |    1 |

y_train dubious values: [
    10000.0,
    2444.444444,
    2666.666667,
    3111.111111,
    2222.222222,
    1777.777778,
    3777.777778,
    2888.888889,
    4000.0,
    1555.555556,
    3555.555556,
    2000.0,
    1333.333333,
    3333.333333,
    5000.0,
    444.4444444,
]

![y_train distribution](./pics/y_train_dist.png)

The above picture of *y_train* distribution demonstrates an anomality appearing with values *0* and *10000*, meanwhile these values are borders of the interval containing all the *y_train* values. This makes me think that values outside of the interval were somehow aggregated to its borders. 



### Distribution analysis

![y_train distribution](./pics/y_train_clean_dist_analysis.png)


|           | sumsquare_error |         aic |            bic |   kl_div |
| --------- | --------------: | ----------: | -------------: | -------: |
| beta      |    1.370405e-08 | 1909.951166 | -220331.161274 | 0.007121 |
| nakagami  |    1.448949e-08 | 1912.762703 | -219887.114378 | 0.007551 |
| johnsonsb |    1.590840e-08 | 1909.449062 | -219118.668745 | 0.008402 |
| burr12    |    1.798824e-08 | 1916.217251 | -218119.852460 | 0.009306 |
| rayleigh  |    2.699707e-08 | 1918.448148 | -214837.403326 | 0.013449 |

## x_train data

### Correlation matrix

![correlation matrix](./pics/corr_matrix_unfiltred.jpg)
the correlation matrix showed presence of 16 blocks of narrowly correlated columns. 

### PCA

Initially I used several Imputer strategies (SimpleImputer with strategies *mean*, *median*, *most_frequent*) and KNNImputer (*n_neighbors=3,5,7*). The *mean* strategy followed by unconverging the PCA algorithm. Nevertheless all others convergated therefore I choose the SimpleImputer with the strategy *median*. 

The PCA algorithm suggested I should choose *n_components=41*.

```python
imputer.fit(xs)
x_train_filled = imputer.transform(xs)

pca.fit(x_train_filled)
cumsum = np.cumsum(pca.explained_variance_ratio_)

d = np.argmax(cumsum > 0.95) + 1
d

```

```python
>>> d=41
```

![correlation matrix](./pics/pac_variance.png)



# MATERIALS

- [A Straightforward Guide to Cleaning and Preparing Data in Python](https://towardsdatascience.com/a-straightforward-guide-to-cleaning-and-preparing-data-in-python-8c82f209ae33)

- [Distribution Analysis 1](https://www.kdnuggets.com/2021/09/determine-best-fitting-data-distribution-python.html)

- [Distribution Analysis 2](https://medium.com/the-researchers-guide/finding-the-best-distribution-that-fits-your-data-using-pythons-fitter-library-319a5a0972e9)

- [Kaggle: Time series with Linear Regression](https://www.kaggle.com/ryanholbrook/linear-regression-with-time-series)