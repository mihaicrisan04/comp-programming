#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("data.in");
ofstream fout("data.out");

int main() {
    int sol = 0;
    char s[1000];
    while (fin.getline(s, 1000)) {
        char first_chr, last_chr;

        for (int i = 0; s[i]; i++) {
            if (strchr("0123456789", s[i])) {
                first_chr = s[i];
                break;
            }
        }

        for (int i = 0; s[i]; i++) {
            if (strchr("0123456789", s[i])) {
                last_chr = s[i];
            }
        }

        int first = first_chr - '0';
        int last = last_chr - '0';  
        int num = first * 10 + last;
        sol += num;
    }
    fout << sol;
    
    return 0;
}