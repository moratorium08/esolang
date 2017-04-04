def dup():
    return "👥"

def string(x):
    return  "💬" + x +  "💬"

def string2(x):
    return "⛽" + x + "🚘 "

def num(x):
    return string(str(x)) + "🔢"

def puts():
    return "➡"

def loop_exp(condition, code):
    return string2(condition) + string2(code) + "🔃"

def div():
    return "🍴"
def divx(x):
    return num(x) + div()
def add():
    return "👫"
def addx(x):
    return num(x) + add()

def mul():
    return "👪"

def mulx(x):
    return num(x) + mul()

def sub():
    return "🌊"

def subx(x):
    return num(x) + sub()

def eq():
    return "👬"

def greater():
    return "🐔"

def less():
    return "🐣"

def if_exp(x):
    return "🔚" + x + "🐧"

def else_exp():
    return "🔙"

def objatindex():
    return "🔑"

def assign(name):
    return string(name) + "📲"

def reference(name):
    return string(name) + "📱"

def swap():
    return "🔀"

def true():
    return "🚲"

def append(array, obj):
    return array + obj + "📌"

def tochar():
    return "🔍"

def mod():
    return "💸"

def modx(x):
    return num(x) + mod()

input_val = ""
tmp_val = "c"


cond = ""
cond += addx(1)
cond += dup()
cond += num(5800)
cond += less()

loop = ""
loop += dup()
loop += dup()
loop += divx(100)
loop += tochar()
loop += dup()
loop += assign(tmp_val)
loop += swap()
loop += modx(100)
loop += reference(input_val)
loop += swap()
loop += objatindex()
loop += eq()
loop += if_exp(swap()+reference(tmp_val)+add()+swap())


code = ""
code += assign(input_val)
code += string("")

code += num(0)
code += loop_exp(cond, loop)
code += swap()
code += puts()

print(code)
