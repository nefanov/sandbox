import numpy as np
import sys
import os


def generate_code(indexes, array_len):
    prefix = "#include <stdio.h>\n" \
             "\nint arr[" + str(array_len) + "];\n"\
             "int main() {\n"
    text = [prefix]
    text.append("\tint left;\n")
    for idx in indexes:
        text.append("\tleft = arr["+str(idx)+"];\n")
    text.append("\treturn 0;\n}\n")
    return "".join(text)

  
if __name__ == '__main__':
    lim = 128
    if len(sys.argv) > 1:
        lim = int(sys.argv[1])

    iterations = 64
    if len(sys.argv) > 2:
        iterations = int(sys.argv[2])

    src_dir = None
    if len(sys.argv) > 3:
        src_dir = sys.argv[3]

    for idx in range(iterations):
        permutation = np.random.permutation([i for i in range(lim)])
        generated = generate_code(permutation, array_len=lim)
        print(generated)
        if src_dir:
            with open(src_dir + os.sep + str(idx) + "_perm.c", "w+") as f:
                f.write(generated)