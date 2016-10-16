#include <iostream>
using namespace std;

int main()
{
    int s = 2;
    int a = 1;
    int b = 2;
    while (a + b < 4000000) {
        int c = a + b;
        if (c % 2 == 0)
            s += a + b;
        a = b;
        b = c;
    }
    cout << "The sum of even fibonnaci numbers under Four million is " << s << "\n";
    return 0;
}
