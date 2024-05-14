#include <stdio.h>
#include <math.h>
#include <complex.h>

#define N 4
#define EPSILON 0.5
#define OMEGA_LP 1
#define PI 3.14159265358979323846

int main() {
    // Calculate B_k coefficient
    double B_k = asinh(1 / EPSILON) / N;

    // Initialize an array to store the poles
    double complex poles[2*N];

    // Calculate and store the poles for the left-half of the complex plane
    for (int i = 0; i < N; ++i) {
        double angle = PI * (2 * i + 1) / (2 * N);
        poles[i] = -sinh(B_k) * sin(angle) + I * cosh(B_k) * cos(angle);
        poles[2*N - 1 - i] = conj(poles[i]);
    }

    // Calculate and store the poles for the right-half of the complex plane
    for (int i = 0; i < N; ++i) {
        poles[N + i] = -poles[i];
    }

    // Save poles to a .dat file
    FILE *file = fopen("poles.txt", "w");
    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }
    fprintf(file, "Real Part, Imaginary Part\n");
    for (int i = 0; i < 2*N; ++i) {
        fprintf(file, "%.4f, %.4f\n", creal(poles[i]), cimag(poles[i]));
    }
    fclose(file);

    printf("Poles saved to poles.txt file.\n");

    return 0;
}
