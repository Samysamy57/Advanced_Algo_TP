#include <stdio.h>
int main() {
    int n;
    int reverse = 0;
    int digit;
    printf("Enter a non-negative integer: ");
    scanf("%d", &n);
    // Handle case when number is 0
    if (n == 0) {
        printf("Reversed number: 0\n");
        return 0;
    }
    while (n > 0) {
        digit = n % 10;          
        reverse = reverse * 10 + digit;  
        n = n / 10;              
    }
    printf("Reversed number: %d\n", reverse);
    return 0;
}
