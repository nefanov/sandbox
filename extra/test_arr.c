#include <stdio.h>

int main() {
        long double arr[2];
        arr[0]=__builtin_nanl("");
        arr[1]=__builtin_infl();
        int i;
        for (i=0;i<2;i++) {
                printf("Number :\n");
                printf("%Lf\n", arr[i]);
        }
        return 0;
}

/*
The correct values from arm64-gcc:
.LC2:
        .word   0
        .word   0
        .word   0
        .word   2147450880
.LC3:
        .word   0
        .word   0
        .word   0
        .word   2147418112

======== Already fixed =========

*/
