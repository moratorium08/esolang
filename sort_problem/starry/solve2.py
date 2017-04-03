
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
    if x == 48:
        ret = ""
        ret += pushx(7)
        ret += dup()
        ret += mul()
        ret += subx(1)
        return ret
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

def read_num():
    return ","
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


max_val = 16
code = ""
code += read_num()
code += dup()
code += pushx(0)

code += label(2)
code += swap()
code += label(0)
code += dup()
code += modx(10)
code += rot()
code += rot()
code += dup()
code += rot()
code += sub()
code += iszerojump(1)

code += dup()
code += print_num()

code += label(1)
code += swap()
code += divx(10)
code += dup()

code += iszerojump(0)
code += add()

code += addx(1)
code += swap()
code += dup()
code += rot()
code += rot()
code += dup()
code += subx(10)
code += iszerojump(2)
print(code)
