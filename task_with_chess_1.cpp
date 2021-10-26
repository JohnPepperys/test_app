
#include <iostream>
#include <vector>
using namespace std;

int main() {
    // put your code here
    int n = 8, i, countx = 0, county = 0, j, count;

    // loading input data
    vector <int> x(n), y(n);
    for (i = 0; i < n; i++) {
        cin >> x[i] >> y[i];
    }

    // calculating x - array - на одной горизонтали
    for (i = 0; i < n; i++) {
        for (count = 0, j = 0; j < n; j++) {
            if (i != j && x[i] == x[j]) {
                count++;
            }
        }
        if (count == 0) {
            countx++;
        }
    }

    // calculating y - array - на одной вертикали
    for (i = 0; i < n; i++) {
        for (count = 0, j = 0; j < n; j++) {
            if (i != j && y[i] == y[j]) {
                count++;
            }
        }
        if (count == 0) {
            county++;
        }
    }

    // cout << "x: " << countx << ",   y: " << county;
    if (countx != 8 || county != 8) {
        cout << "YES";
        return 0;
    }

    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            if (i != j) {
                if (abs(x[i] - x[j]) == abs(y[i] - y[j])) {
                    cout << "YES";
                    return 0;
                }
            }
        }
    }
//
    cout << "NO";
    return 0;
}
