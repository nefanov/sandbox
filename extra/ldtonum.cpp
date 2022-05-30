/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/

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
    printf("%Lf\n", ldd);
    unsigned long* u64v;
    int* i32v;
    char* bytes;
    bytes = reinterpret_cast<char*>(&ldd);
    
    for (int i=0;i<16;i++)
    {
        printf("  %02d ",  i );
            cout<<"| ";
        if (i == 7)
            cout<<"-- |";
    }
    cout<<endl;
    for (int i=0;i<16;i++)
    {
        printf("0x%02X ",  (unsigned)bytes[i] & 0xff );
            cout<<"| ";
        if (i == 7)
            cout<<"-- |";
    }
    cout<<endl;
    for (int i=0;i<16;i++)
    {
        printf(" %03u ",  (unsigned)bytes[i] & 0xff );
            cout<<"| ";
        if (i == 7)
            cout<<"-- |";
    }
    cout<<endl;
    return;
}

void __cvt_verbose(long double ldd) {
    unsigned long* u64v;
    int* i32v;
    char* bytes;
    u64v = reinterpret_cast<unsigned long*>(&ldd);
    printf("========uint64=========\n");
    for (int i=0;i<2;i++)
    {
        printf("%d:\t%016lx\n", i,  (unsigned)u64v[i] & 0xffffffffffffffff );
        if (i % 2)
            cout<<"------------------\n";
        if (i == 7)
            cout<<"------------------\n";
    }
    i32v = reinterpret_cast<int*>(&ldd);
    printf("========int=========\n");
    for (int i=0;i<4;i++)
    {
        printf("%d:\t%08x\n", i,  (unsigned)i32v[i] & 0xffffffff );
        if (i % 2)
            cout<<"------------------\n";
        if (i == 7)
            cout<<"------------------\n";
    }
    bytes = reinterpret_cast<char*>(&ldd);
    printf("========bytes=========\n");
    for (int i=0;i<16;i++)
    {
        printf("%d:\t%02x\n", i,  (unsigned)bytes[i] & 0xff );
        if (i % 2)
            cout<<"------------------\n";
        if (i == 7)
            cout<<"------------------\n";
    }
    
    for (int i=0;i<16;i++)
    {
        printf("  %02d ",  i );
            cout<<"| ";
        if (i == 7)
            cout<<"-- |";
    }
    cout<<endl;
    for (int i=0;i<16;i++)
    {
        printf("0x%02x ",  (unsigned)bytes[i] & 0xff );
            cout<<"| ";
        if (i == 7)
            cout<<"-- |";
    }
    cout<<endl;
    return;
}

int main()
{
    cvt(2.0);
    return 0;
}
