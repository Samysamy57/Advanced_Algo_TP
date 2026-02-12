#include <stdio.h>
#include <stdlib.h>

struct Interval {
    int start;
    int end;
};
int compare(const void *a, const void *b) {
    struct Interval *x = (struct Interval *)a;
    struct Interval *y = (struct Interval *)b;
    return x->start - y->start;
}
void merge(struct Interval arr[], int n) {
    if (n <= 0)
        return;
    qsort(arr, n, sizeof(struct Interval), compare);
    struct Interval merged[n];
    int index = 0;
    merged[0] = arr[0];
    int i;
    for (i = 1; i < n; i++) {
        if (arr[i].start <= merged[index].end) {

            if (arr[i].end > merged[index].end)
                merged[index].end = arr[i].end;
        }
        else {
            index++;
            merged[index] = arr[i];
        }
    }
    printf("Merged Intervals:\n");
    for (i = 0; i <= index; i++) {
        printf("[%d, %d] ", merged[i].start, merged[i].end);
    }
}
int main() {
    int n, i;
    printf("Enter number of intervals: ");
    scanf("%d", &n);
    struct Interval arr[n];
    for (i = 0; i < n; i++) {
        printf("Enter start and end: ");
        scanf("%d %d", &arr[i].start, &arr[i].end);
    }
    merge(arr, n);
    return 0;
}
