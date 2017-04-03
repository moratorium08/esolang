# coding:utf-8
import math
import sys

def pushx(x):
    return " " * (x + 5) + "+"


def pushx_sq(x):
    """
    push sq
    dup
    mul
    push r
    add
    """
    if x < 11:
        return pushx(x)
    ret = ""
    sq = math.floor(math.sqrt(x))
    r = x - sq * sq

    # push sq
    ret += " " * (sq + 5)
    ret += "+"
    # dup
    ret += " +"
    # mul
    ret += "  *"
    # push r
    ret += " " * (r + 5)
    ret += "+"
    # add
    ret += "*"
    return ret

def add():
    return "*"
def sub():
    return " *"
def mul():
    return "  *"
def div():
    return "   *"
def mod():
    return "    *"

def mulx(x):
    ret = ""
    ret += pushx_sq(x)
    ret += mul()
    return ret

def subx(x):
    """
    push x (push_sq)
    sub
    """

    ret = ""

    ret += pushx_sq(x)
    ret += sub()

    return ret

def addx(x):
    """
    push x (push_sq)
    add
    """
    ret = ""
    ret += pushx_sq(x)
    ret += add()
    return ret

def divx(x):
    ret = ""
    ret += pushx_sq(x)
    ret += div()
    return ret

def modx(x):
    ret = ""
    ret += pushx_sq(x)
    ret += mod()
    return ret

def read_ascii():
    return " ,"

def label(mark):
    return " "*mark + "`"

def iszerojump(mark):
    return " "*mark + "'"

def print_num():
    return "."

def print_ascii():
    return " ."

def dup():
    return " +"
def swap():
    return "  +"
def rot():
    return "   +"
def pop():
    return "    +"
def push_val(val):
    n = val + 5
    return " " * n + "+"



"""
# test
source += pushx_sq(15)
source += addx(5)
source += print_num() # this should be print 20
source += pushx_sq(15)
source += addx(5)
source += print_num() # this should be print 10
source += pushx_sq(10)
source += dup()
source +=  " " * 5 + "*"
source += print_num()
"""

max_val = 20

code = ""
code += pushx(0) # memory
code += pushx_sq(100) # loopcounter

code += label(1)
code += swap()
code += read_ascii()
code += subx(48)
code += pushx(1)
code += swap()

code += pushx(1)
code += iszerojump(0)
code += label(3)
code += swap()
code += mulx(max_val)
code += swap()
code += subx(1)
code += label(0)
code += dup()
code += iszerojump(3)
code += pop()

code += add()
code += swap()
code += subx(1)
code += dup()
code += iszerojump(1)
code += pop()

# ---- make memory ----
code += pushx(0)

code += label(2)
code += swap()
code += dup()
code += modx(max_val) # counter

code += pushx(1)
code += iszerojump(5)
code += label(4)
code += rot()
code += rot()
code += dup()
code += print_num()
code += rot()
code += subx(1)
code += label(5)
code += dup()
code += iszerojump(4)

code += pop()

code += divx(max_val)
code += swap()
code += addx(1)
code += dup()
code += subx(10)
code += iszerojump(2)

print(code+"\n\n")

