#include <iostream>
using namespace std;

typedef unsigned char       uint8;
typedef unsigned short int  uint16;
typedef unsigned long int   uint32;

uint32  // OR uint16 OR uint8
isqrt32 (uint32 n) // OR isqrt16 ( uint16 n ) OR  isqrt8 ( uint8 n ) - respectively [ OR overloaded as isqrt (uint?? n) in C++ ]
{
    register uint32 // OR register uint16 OR register uint8 - respectively
        root, remainder, place;

    root = 0;
    remainder = n;
    place = 0x40000000; // OR place = 0x4000; OR place = 0x40; - respectively

    while (place > remainder)
        place = place >> 2;
    while (place)
    {
        if (remainder >= root + place)
        {
            remainder = remainder - root - place;
            root = root + (place << 1);
        }
        root = root >> 1;
        place = place >> 2;
    }
    return root;
}
int is_prime(int n) {
    for (int i = 2; i < isqrt32(n); i++) {
        if (n % i == 0)
            return 0;
    }
    return 1;
}

int main()
{
    long l = 600851475143;
    for (int i = 2; i < l / 2; i++) {
        if (is_prime(i) == 0) {
            continue;
        }
        if (l % i == 0) {
            cout << i << "\n";
        }
    }
    return 0;
}
