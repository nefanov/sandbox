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
    u64v = reinterpret_cast<unsigned long*>(bytes);
    for (int i=0;i<2;i++)
        printf("%016lx ", u64v[i]);
    printf("\n");
    
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



#define ALPHA   0x1.405f49063806f6e0ca86fd58fe82p1

#define EXPAND_SUFFIX_L(what) what##L
#define SUFFIX_L(       what) EXPAND_SUFFIX_L(what)

int main()
{
    cvt(SUFFIX_L(ALPHA));
    std::cout<< sizeof(SUFFIX_L(ALPHA)) <<std::endl;
    return 0;
}
