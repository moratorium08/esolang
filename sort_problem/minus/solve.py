# coding:utf-8


code = ""

def add(c):
    global code
    code += c + "\n"

def make_for(code, count, place):
    inst_c = len(code.strip("\n").split("\n"))
    bef = for_bef % (count, place, (inst_c + 3))
    aft = for_aft % (inst_c + 10)
    return bef + code + aft

def make_print(val):
    return print_val

def test():
    print(make_for(test, 10, 900) + test2)

def solve():
    # add("b-=1")
    add(make_for(getc, 100, 900))
    add(make_for(print_val, 10, 600))
    print(code.replace("\n\n", "\n").replace("\n\n", "\n"))


# l: loop counter
for_bef = """
p-=p
k-=k
l-=l
k-=%d
l-=k
p-=%d
A-=A
k-=k
k-=l
A-=%d
p-=k
c-=A
p-=p
"""

for_aft = """
l-=1
c-=%d
p-=p
"""


getc = """
A-=i
p-=A
K-=1
A-=K
p-=p
A-=A
"""

print_val = """
A-=A
A-=58
m-=m
n-=n
m-=10
n-=m
n-=l
A-=n
p-=A
u-=u
u-=A
A-=A
p-=p
p-=300
A-=A
v-=v
v-=u
A-=7
p-=v
c-=A
p-=p
A-=A
A-=48
A-=n
o-=A
u-=1
c-=15
p-=p
"""

test = """
A-=A
A-=66
o-=A
"""
test2 = """
A-=A
A-=67
o-=A
"""
print_val = print_val.replace("\n\n", "\n")



if __name__ == '__main__':
    solve()

