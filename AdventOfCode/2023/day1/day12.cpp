#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

ifstream fin("data.in");
ofstream fout("data.out");

int find_num(char s[], char nums[][10]) {
    int min = 1e9;
    int max = -1e9;
    int first = -1, last = -1;

    // for numbers that are represented by words
    for (int i = 0; i < 10; i++) {
        char * first_pos = strstr(s, nums[i]);
        if (first_pos != NULL) {
            int fp = first_pos - s;
            if (fp < min) {
                min = fp;
                first = i;
            }
        }

        char * last_pos = NULL;
        char * curr = strstr(s, nums[i]);
        while (curr != NULL) {
            last_pos = curr;
            curr = strstr(curr + 1, nums[i]);
        }
        if (last_pos != NULL) {
            int lp = last_pos - s;
            if (lp > max) {
                max = lp;
                last = i;
            }
        }
    }

    // for numbers that are represented by digits
    char first_chr, last_chr;
    int first_pos = -1, last_pos = -1;
    for (int i = 0; s[i]; i++) {
            if (strchr("0123456789", s[i])) {
                first_chr = s[i];
                first_pos = i;
                break;
            }
        }

    for (int i = 0; s[i]; i++) {
        if (strchr("0123456789", s[i])) {
            last_chr = s[i];
            last_pos = i;
        }
    }

    int first_digit = first_chr - '0';
    int last_digit = last_chr - '0';

    if (first_pos == -1) {
        first_pos = min+1;
    }
    if (min == 1e9) {
        first = first_digit;
    }
    if (first_pos < min) {
        first = first_digit;
    }

    if (last_pos == -1) {
        last_pos = max-1;
    }
    if (max == -1e9) {
        last = last_digit;
    }
    else if (last_pos > max) {
        last = last_digit;
    }

    return first * 10 + last;
}

int main() {
    int sol = 0;
    char s[1000];
    char nums[10][10] = {
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
    };
    while (fin.getline(s, 1000)) {
        sol += find_num(s, nums);
    }
    fout << sol;
    
    return 0;
}