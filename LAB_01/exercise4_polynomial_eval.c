#include <stdio.h>

double Eval_Poly(double coeffs[], int n, double x) {
    double valeur;
    int i;

    // We take the last number from the table
    valeur = coeffs[n];

    // Horner's loop
    for (i = n - 1; i >= 0; i--) {
        valeur = (valeur * x) + coeffs[i];
    }

    return valeur;
}

int main() {
    // Exemple du TP : P(x) = 5x^3 + 0x^2 - 2x + 3
    double coeffs[] = {3, -2, 0, 5};
    int n = 3; // degre 3
    double x = 2.0;

    double resultat = Eval_Poly(coeffs, n, x);
    printf("Resultat : %.2f\n", resultat); // Affiche 39.00

    return 0;
}