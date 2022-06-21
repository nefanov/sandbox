import numpy as np
import sys
import os

def print_hi(name):
    print(f'Hi, {name}')

def generate_code(indexes, array_len, mult):
    prefix = "#include <stdio.h>\n" \
             "\nint arr1[" + str(array_len*mult) + "];\n"\
             "int main() {\n"
    text = [prefix]
    text.append("\tint left;\n");
    for i in range(len(indexes)):
        text.append("\tleft = arr1["+str(indexes[i]*mult)+"];\n")
    text.append("\treturn 0;\n}\n")
    return "".join(text)

if __name__ == '__main__':
    lim = 256
    if len(sys.argv) > 1:
        lim = int(sys.argv[1])

    second_lim = 128
    if len(sys.argv) > 2:
        second_lim = int(sys.argv[2])

    iterations = 64
    if len(sys.argv) > 3:
        iterations = int(sys.argv[3])

    src_dir = None
    if len(sys.argv) > 4:
        src_dir = sys.argv[4]
     
    mult = 1
    for idx in range(iterations):
        if idx == 0:
                p = np.array([1] + [0 for i in range(lim-1)])
                mult = 1
        elif idx == 1:
                p = np.array([0 for i in range(lim)])
                p[32 * 1024] = 1
                mult = 512
        elif idx < iterations//2:
                p = np.array([0.99**i for i in range(lim)])
                mult = 1
        else:
                p = np.array([1.000001**i for i in range(lim)])
                mult = 512
        p = p/p.sum()
        permutation = []
        elems = [i for i in range(lim)]
        ds = np.random.choice(elems, second_lim, p=p)
        for j in range(second_lim):
                if len(permutation) == 0:
                        permutation.append(0)
                else:
                        permutation.append((permutation[-1] + ds[j])%lim)
        generated = generate_code(permutation, array_len=lim, mult=mult)
        print(generated)
        if src_dir:
            with open(src_dir + os.sep + str(idx) + "_perm" + str(lim) + ".c", "w+") as f:
                f.write(generated)
                
