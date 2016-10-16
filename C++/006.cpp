#include <stdio.h>
#include <iostream>     /* printf */
#include <math.h>
using namespace std;

int sumOfSquares() {
    int s = 0;
    for (int x = 1; x < 101; x++) {
        s += pow(x, 2);
    }
    return s;
}
int squareOfSum() {
    int s = 0;
    for (int x = 1; x < 101; x++) {
        s += x;
    }
    return pow(s, 2);
}
int main() {
    cout << squareOfSum() - sumOfSquares() << "\n";
    return 0;
}
