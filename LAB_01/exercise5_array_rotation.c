#include <stdio.h>


void Inverser(int Vect[], int debut, int fin) {
    int save;
    while (debut < fin) {
        save = Vect[debut];
        Vect[debut] = Vect[fin];
        Vect[fin] = save;
        debut = debut + 1;
        fin = fin - 1;
    }
}


void Array_Rotation_Optimization(int Vect[], int n, int k) {
    k = k % n; // k mod n
    
    if (k == 0) {
        return;
    }

    // We use the method of three inversions
    Inverser(Vect, 0, n - 1);
    Inverser(Vect, 0, k - 1);
    Inverser(Vect, k, n - 1);
}

int main() {
    int Vect[] = {1, 2, 3, 4, 5, 6, 7};
    int n = 7;
    int k = 10;

    Array_Rotation_Optimization(Vect, n, k);

    for (int i = 0; i < n; i++) {
        printf("%d ", Vect[i]);
    }
    
    return 0;
}