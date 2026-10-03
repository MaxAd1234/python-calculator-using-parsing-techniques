# Calculator using scanning and parsing techniques

This is a basic calculator using scanning and parsing techniques used in compilers to evaluate and calculate basic arithmetic expressions.

## Implemented with 
Python
Tkinter

## How it works
1. **Tokenizing**
    The input expression is tokenized to check whether allowed chars are entered or not. For tokenizing DFAs are used. Available tokens: "+", "*", "/", "-", "(", ")", "number" (positive and negative numbers)
2. **Infix to prefix**
    After tokenizing, the expression is converted from infix to prefix notation, so that a simpler context-free grammar can be used. For this part an algorithm from [Geeksforgeeks](https://www.geeksforgeeks.org/dsa/convert-infix-prefix-notation/) is used.
3. **Parsing**
    The arithmetic expression is parsed using a context-free grammar, its parsing table and a bottom-up parsing algorithm to check whether the expression is valid.
4. **Calculating**
    After parsing, the result will be calculated.

## How to use
Clone the repo:
```bash
git clone https://github.com/MaxAd1234/python-calculator-using-parsing-techniques.git
```

Run with Tkinter UI:
```bash
python main.py
```

Run with console output (for own expressions, change them in the `main` method):
```bash
python calculator.py
```
