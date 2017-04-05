# coding:utf-8
import sys
import re


def translate(filename):
    with open(filename, "r") as f:
        data = f.read()

    while True:
        m = re.search(r"'\(.+\)", data)
        if m is not None:
            p = m.start()
            pe = m.end()
            chars = data[p+2:pe-1]
            o_c = "#"+"#".join([str(ord(x)) for x in chars])
            data = data[:p] + o_c + data[pe:]
            continue

        m = re.search(r"''+[^']", data)
        if m is None:
            m = re.search(r"'[^']", data)
            if m is None:
                break
            p = m.start()
            char = data[p+1]
            o_c = str(ord(char))
            data = data[:p] + '#' + o_c + data[p+2:]
            continue
        p = m.start()
        pe = m.end()
        s = "'" * (pe-p -2)

        char = data[pe-1]
        o_c = s+s.join([x for x in str(ord(char))])
        data = data[:p] + s+"#" + o_c + data[pe:]

    l = data.split("\n")
    l = [x for x in l if x[0:2] != "//"]
    return ''.join(l).replace(" ","")

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("python %s [filename]" % sys.argv[0])
    else:
        print(translate(sys.argv[1]))
