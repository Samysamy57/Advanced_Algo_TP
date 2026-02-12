#include <stdio.h>
#include <string.h>

#define SIZE 100
int checkBalanced(char str[]) {
    char stack[SIZE];
    int top = -1;
    int i;
    for (i = 0; str[i] != '\0'; i++) {
        if (str[i] == '(' || str[i] == '{' || str[i] == '[') {
            top++;
            stack[top] = str[i];
        }
        else if (str[i] == ')' || str[i] == '}' || str[i] == ']') {
            if (top == -1) {
                return 0;
            }
            if ((str[i] == ')' && stack[top] == '(') ||
                (str[i] == '}' && stack[top] == '{') ||
                (str[i] == ']' && stack[top] == '[')) {

                top--; 
            }
            else {
                return 0;
            }
        }
    }
    if (top == -1)
        return 1;
    else
        return 0;
}
int main() {
    char expression[SIZE];
    printf("Enter expression: ");
    scanf("%s", expression);
    if (checkBalanced(expression))
        printf("Balanced\n");
    else
        printf("Not Balanced\n");
    return 0;
}
