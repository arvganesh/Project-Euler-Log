#include <iostream>

using namespace std;


int reverse_number(int num, int base = 10)
{
    int new_num = 0;

    while (num != 0)
    {
        int digit = num % base;
        new_num = new_num*base + digit;
        num /= base;
    }
    return new_num;
}
bool is_pal(int num)
{
    return num == reverse_number(num);
}
int main()
{
    int big = 0;
    for (int a = 999; a > 99; a--) {
        for (int b = 999; b > 99; b--) {
            int x = a*b;
            if (is_pal(x) == 0) {
                continue;
            }
            if (a*b > big)
                big = a*b;
        }
    }
    cout << big << "\n";
    return 0;
}
