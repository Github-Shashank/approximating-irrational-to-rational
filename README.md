# Approximating Irrational to Rational

A simple yet powerful Python tool to find the best rational approximation (as a reduced fraction) for a given irrational number.

## 🚀 Features

- Approximates irrational numbers like π, √2, e, etc.
- Returns the closest rational fraction within a given denominator limit.
- Skips unreduced (non-coprime) fractions for optimal results.
- Extremely fast — handles large denominators efficiently.

## 🤔 How to use

- This program takes three inputs.
- First input will be your irrational number which you want to approximate.
- Second input will be maximum denominator can be.
- Third input will be minimum denominator can be.
- Then what about numerator, well program efficiency takes place and set on its own
- It returns set(list) of numbers like [p,q,p/q,error] so your fraction closest to your value is p/q

## 🧠 How It Works

- For each possible denominator `j`, calculates `i` such that `i/j ≈ input number`.
- Only considers fractions where `gcd(i, j) == 1` (i.e., reduced).
- Selects the fraction with the smallest absolute error.

## 📦 Example

```bash
Enter any irrational number :- 3.141592653589793
Enter max number to be used in denominator :- 2000000
Enter min number to be used in denominator :- 1
```

Output: [p,q,p/q,error] 
```
[5419351, 1725033, 3.1415926535898153, 2.220446049250313e-14]
```

## 🛠 Requirements

- Python 3.6+

## 📁 Usage

Run the script:
```bash
python irrational_fraction_finder.py
```

## 📄 License

MIT License
