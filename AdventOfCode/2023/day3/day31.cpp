#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

ifstream fin ("data.in");
ofstream fout ("data.out");

int di[] = {-1, -1, -1, 0, 1, 1, 1, 0};
int dj[] = {-1, 0, 1, 1, 1, 0, -1, -1};

char c[1000][1000];
int a[1000][1000], b[1000][1000];
char s[1000];
int l = 1;
int sol = 0;
int k = 1;

bool inside(int x, int y) {
    return x >= 1 && x <= l && y >= 1 && y <= strlen(c[x]+1);
}

void fill(int x, int y, char c[1000][1000], int a[1000][1000]) {
    for (int i = 0; i < 8; i++) {
        if (inside(x+di[i], y+dj[i]) && a[x+di[i]][y+dj[i]] == 0 && strchr("0123456789", c[x+di[i]][y+dj[i]])) {
            a[x+di[i]][y+dj[i]] = k;
            fill(x+di[i], y+dj[i], c, a);
        }
    }
}

void clear(int x, int y, int n, int a[1000][1000]) {
    a[x][y] = 0;
    for (int i = 0; i < 8; i++) {
        if (inside(x+di[i], y+dj[i]) && a[x+di[i]][y+dj[i]] == n) {
            clear(x+di[i], y+dj[i], n, a);
        }
    }
}

int main() {
    while (fin.getline(s, 1000)) {
        strcpy(c[l]+1, s);
        l++;
    }
    l--;

    // fill the numbers
    for (int i = 1; i <= l; i++) {
        for (int j = 1; j <= strlen(c[i]+1); j++) {
            if (strchr("*", c[i][j])) {
                a[i][j] = -1;
                fill(i, j, c, a);
                k++;
            }
        }
    }

    // copy the matrix
    for (int i = 1; i <= l; i++) {
        for (int j = 1; j <= strlen(c[i]+1); j++) {
            b[i][j] = a[i][j];
        }
    }

    // count the numbers that appear in a gear
    int f[10000] = {0};
    for (int i = 1; i <= l; i++) {
        for (int j = 1; j <= strlen(c[i]+1); j++) {
            for (int n = 1; n <= k; n++) {
                if (b[i][j] == n) {
                    f[n]++;
                    clear(i, j, n, b);
                }
            }
        }
    }

    // delete the numbers that appear only once
    for (int i = 1; i <= l; i++) {
        for (int j = 1; j <= strlen(c[i]+1); j++) {
            if (f[a[i][j]] != 2 && a[i][j] != -1) {
                a[i][j] = 0;
            }
        }
    }

    for (int i = 1; i <= l; i++) {
        for (int j = 1; j <= strlen(c[i]+1); j++) {
            if (a[i][j]  == -1)
                fout << "*";
            else
                fout << a[i][j];
        }
        fout << "\n";
    }
    return 0;
}