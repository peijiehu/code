---
layout: post
title: Evaluate a math expression represented by a String
excerpt: ''
categories: [code]
date:   2017-07-31 21:00:00
comments: true
---

## Evaluate a math expression represented by a String

### 1. only +, -, *, / and 0 - 9 are allowed, presented as Infix Notation

s = '9+3-2*2+1'  res = 9

first iteration calculate * and / pairs and store other nums and operators in a list

stack = [9, '+', 3, '-', 4, '+', 1]

second iteration on stack to calculate result

~~~ python
def eval_math(s):
    stack = [int(s[0])]
    i = 1
    while i < len(s):
        if s[i] == '*':
            stack[-1] *= int(s[i+1])
            i += 2
        elif s[i] == '/':
            stack[-1] /= int(s[i+1])
            i += 2
        elif s[i] == '+' or s[i] == '-':
            stack.append(s[i])
            i += 1
        else:
            stack.append(int(s[i]))
            i += 1
    res = stack[0]
    i = 1
    while i < len(stack) - 1:
        if stack[i] == '+':
            res += stack[i+1]
        elif stack[i] == '-':
            res -= stack[i+1]
        i += 2
    return res
~~~

### 2. LeetCode 150. Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:

  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9

  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

Solution

Use stack to store previous two numbers or latest result:
```
stack = [2]
stack = [2, 1]
stack = [3]
stack = [3, 3]
stack = [9]
```
~~~ python
def evalRPN(tokens):
    stack = []
    for t in tokens:
        if t not in {'+', '-', '*', '/'}:
            stack.append(int(t))
        else:
            r, l = stack.pop(), stack.pop()
            if t == '+':
                stack.append(l + r)
            elif t == '-':
                stack.append(l - r)
            elif t == '*':
                stack.append(l * r)
            elif t == '/':
                if l * r < 0 and l % r != 0:
                    stack.append(l / r+1)
                else:
                    stack.append(l / r)
            else: raise ValueError("Unsupported operation '{}'".format(t))
    return stack[0]
~~~

Another similar solution is to use python lambda
~~~ python
def __init__(self):
    self.operators = {
        '+': lambda y, x: x + y,
        '-': lambda y, x: x - y,
        '*': lambda y, x: x * y,
        '/': lambda y, x: int(operator.truediv(x, y))
    }

def evalRPN(self, tokens):
    if not tokens:
        return 0

    stack = []

    for token in tokens:
        if token in self.operators:
            stack.append(self.operators[token](stack.pop(), stack.pop()))
        else:
            stack.append(int(token))

    return stack[0]
~~~
