#include <iostream>
#include <fstream>

using namespace std;

ifstream fin ("data.in");
ofstream fout("data.out");

int main() {
    char s[1000];
    char red[] = "red";
    char green[] = "green";
    char blue[] = "blue";

    int id = 1;
    while (fin.getline(s, 1000)) {
        
        id++;
    }
    
    
    return 0;
}