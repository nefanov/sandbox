#include <stdio.h>

void multiply_mantissas( uint64_t mantissa1[], uint64_t mantissa2[], int result []);

typedef union _container {
  __float128 float_val;
  unsigned long bits[2];
} ContainerF128;

typedef ContainerF128 float_128;

int main()
{
    // init
    // check_mul
    // output:
    // raw
    // float128
    // implement:
    // another operations
    // try to minimize overhead

    return 0;
}

float_128 mul(const float_128 op1, const float_128 float_to_multiply)
{
    float_128 result;
    
    uint64_t mantissa1[2];
    uint64_t mantissa2[2];
    
    mantissa1[0] = op1.bits[0]; mantissa1[1] = op1.bits[1];
    mantissa2[0] = float_to_multiply.bits[0]; mantissa2[1] = float_to_multiply.bits[1];
    
    int result_mantissa[230];
    
    multiply_mantissas( mantissa1, mantissa2, result_mantissa );
    
    int exp = 0;
    
    int start = 2;
    if( result_mantissa[0]){
        start = 1;
        exp += 1;
    }   
    
    exp += get_exponent(op1) + get_exponent(float_to_multiply);
    
    for( int i=0; i < 114; i++ )  {
        if(result_mantissa[i + start])
            set_bit(result, 113 - i);
    }
    
    set_exponent(result, exp );
    
    if((is_negative(op1) && !is_negative(float_to_multiply) ) || ( !is_negative(op1) && is_negative(float_to_multiply)))
        result.set_bit( 127 );
    
    return result;
}

void multiply_mantissas(uint64_t mantissa1[], uint64_t mantissa2[], int result[])
{
    mantissa1[0] = ( mantissa1[0] << 14 ) >> 14;
    mantissa2[0] = ( mantissa2[0] << 14 ) >> 14;
    
    mantissa1[0] |= 1ULL << 50;
    mantissa2[0] |= 1ULL << 50;
    
    
    for( int i=0; i< 230; i++)
        result[i] = 0;
    
    for( int i=0; i < 115; i++ ){
        for( int j=0; j < 115; j++){
            
            int bit1 = get_bit( mantissa1, i );
            int bit2 = get_bit( mantissa2, j);
            
            result[ 229 - j - i ] += bit1 * bit2;
        }
    }
    
    
    for( int i=229; i>0; i--){
        int val = result[i];
        result[i] = val % 2;
        result[i-1] += val / 2;
    }
}
