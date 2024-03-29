# -*- coding: utf-8 -*-
"""infix to postfix 24/01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Tz2BrSBEO-H7ZSH4Uatml08MZDxe-2_z
"""

def is_operator(char):
    return char in {'+', '-', '*', '/'}

def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    else:
        return 0

def infix_to_postfix(infix_expression):
    stack = []
    postfix_expression = []

    for char in infix_expression:
        if char.isalnum():
            postfix_expression.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix_expression.append(stack.pop())
            stack.pop()
        elif is_operator(char):
            while stack and precedence(stack[-1]) >= precedence(char):
                postfix_expression.append(stack.pop())
            stack.append(char)
    while stack:
        postfix_expression.append(stack.pop())

    return ''.join(postfix_expression)
infix_expression = "(a+b)*c+d"
postfix_expression = infix_to_postfix(infix_expression)
print("Infix Expression:", infix_expression)
print("Postfix Expression:", postfix_expression)

def is_operand(char):
    return char.isalnum()

def evaluate_postfix(postfix_expression):
    stack = []

    for char in postfix_expression:
        if is_operand(char):
            stack.append(float(char))
        else:

            operand2 = stack.pop()
            operand1 = stack.pop()

            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2

            stack.append(result)

    return stack.pop()

postfix_expression = "1020*5+"
result = evaluate_postfix(postfix_expression)
print("Postfix Expression:", postfix_expression)
print("Result:", result)

def precedence(a):
    if a=="+" or a=="-":
        return 1
    if a=="*" or a=="/":
        return 2

a = list(input("Enter the infix notation separated by space: ").split(" "))
postfix = ""
opstack = []
for i in a:
    if i in ["+", "-", "*", "/"]:
        if((len(opstack)==0) or (precedence(i)>precedence(opstack[-1]))):
            opstack.append(i)
        else:
            postfix+=opstack.pop()
            opstack.append(i)
    elif i==" ":
        continue
    else:
        postfix+=i
while(len(opstack)!=0):
    postfix+=opstack.pop()
print(postfix)

a = list(input("Enter the postfix expression: ").split(" "))
stack = []
for i in a:
   # if(len(stack)==1 and i==a[-1]):
    #    stack[0]= -stack[0]
     #   break
    if(i in ["+", "-", "*", "/"]):
        b = stack.pop()
        c = stack.pop()
        if(i=="+"):
            stack.append(c+b)
        elif(i=="-"):
            stack.append(c-b)
        elif(i=="*"):
            stack.append(c*b)
        elif(i=="/"):
            stack.append(c/b)
    elif i==" ":
        continue
    else:
        stack.append(int(i))
print("The result of the expression: ",stack[0])

# recursion
def factorial(n):
  if(n==0 or n==1):
    return 1
  else:
    return n* factorial(n-1)
n=int(input("enter the n value: "))
res=factorial(n)
print(res)

# fibonacci series
def fibonacci(n):
  if n<=0:
    print("invalid input")
  elif n==1:
    return 0
  elif n==2:
    return 1
  else:
    return fibonacci(n-1)+fibonacci(n-2)
for i in range(n_terms):
    print(fibonacci(i))
print(fibonacci(10))

