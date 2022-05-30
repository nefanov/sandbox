/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>
#include <cstdio>

using namespace std;

void cvt(long double ldd) {
    unsigned long* u64v;
    int* i32v;
    char* bytes;
    u64v = reinterpret_cast<unsigned long*>(&ldd);
    printf("========uint64=========\n");
    for (int i=0;i<2;i++)
    {
        printf("%d:\t%lx\n", i,  (unsigned)u64v[i] & 0xffffffffffffffff );
        if (i % 2)
            cout<<"------------------\n";
        if (i == 7)
            cout<<"------------------\n";
    }
    i32v = reinterpret_cast<int*>(&ldd);
    printf("========int=========\n");
    for (int i=0;i<4;i++)
    {
        printf("%d:\t%x\n", i,  (unsigned)i32v[i] & 0xffffffff );
        if (i % 2)
            cout<<"------------------\n";
        if (i == 7)
            cout<<"------------------\n";
    }
    bytes = reinterpret_cast<char*>(&ldd);
    printf("========bytes=========\n");
    for (int i=0;i<16;i++)
    {
        printf("%d:\t%x\n", i,  (unsigned)bytes[i] & 0xff );
        if (i % 2)
            cout<<"------------------\n";
        if (i == 7)
            cout<<"------------------\n";
    }
    return;
}

int main()
{
    cvt(2.0L);
    return 0;
}
