#include <iostream>
using namespace std;

bool isDiv(int n) {
    for (int i = 1; i < 21; i++) {
        if (n % i != 0)
            return 0;
    }
    return 1;
}
int main() {
    int a = 0;
    for (int x = 2520; x < 10000000000; x++) {
        if (isDiv(x) == 1) {
            a = x;
            break;
        }
    }
    cout << a << "\n";
    return 0;
}
