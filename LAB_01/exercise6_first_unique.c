#include <stdio.h>
#include <string.h>

// Function to find the first unique character
int Character_Finder(char s[]) {
    // A table of 256 is used to simulate the dictionary
    int dico[256] = {0};
    int n, i;

    n = strlen(s);
    if (n == 0) {
        return -1;
    }

    // First loop: count the letters
    for (i = 0; i < n; i++) {
        dico[(unsigned char)s[i]] = dico[(unsigned char)s[i]] + 1;
    }

    // Second loop: we look for the first one that has 1
    for (i = 0; i < n; i++) {
        if (dico[(unsigned char)s[i]] == 1) {
            return i;
        }
    }

    return -1;
}

int main() {
    char s[] = "loveleetcode";
    int index = Character_Finder(s);

    if (index != -1) {
        printf("Index : %d (lettre '%c')\n", index, s[index]);
    } else {
        printf("-1\n");
    }

    return 0;
}