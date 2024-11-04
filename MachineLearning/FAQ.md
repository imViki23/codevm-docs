# FAQ

## What is Multinomial regression or Softmax regression

- Problem of classification involving more than two classes. This is sometimes referred to as multinomial regression or softmax regression when the number of classes is more than two.

## What is mean normalization

Features can have numbers with higher value for e.g. stock price = 1000, housing price = 4500, and if we use this number for calculation it will result in big numbers for computer to calculate so, it is good practise to normalize data within -1 to 1 for efficient calculation.

$$
norm = \frac{x - mean}{standard\_deviation}
$$

```python
X = np.array([100, 150, 200, 225, 275, 300])
mean = np.mean(X) # 208.33333333333334
standard_deviation = np.std(X) # 68.71842709362768
X_norm = (X - mean) / standard_deviation # [-1.57648156 -0.84887469 -0.12126781  0.24253563  0.9701425   1.33394594]
```