
print('input your string> ', end=' ')
s = input()

t1 = 0
t2 = 0
result = ''
for x in map(ord, s):
    diff = x - t1
    if diff == 0:
        result += '.'
        continue

    absdiff = abs(diff)
    mn = 100
    ans = -1
    for i in range(1, 12):
        v = absdiff % i

        w = v + i + (absdiff // i)
        if w < mn:
            ans = i
            mn = w

    result += '>'
    for i in range(absdiff//ans):
        result += '+'

    if diff < 0:
        char = '-'
    else:
        char = '+'

    result += '[<'
    for i in range(ans):
        result += char

    result += '>-]<'

    for i in range(absdiff % ans):
        result += char

    result += '.'
    t1 = x


print(result)
