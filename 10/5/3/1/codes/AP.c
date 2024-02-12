#include <stdio.h>

void generateAP(float initial, float commonDiff, int terms, int n_values[], float y_values[]) {
    for (int i = 0; i < terms; i++) {
        n_values[i] = i;
        y_values[i] = initial + i * commonDiff;
    }
}

void saveToDatFile(int n_values[], float y_values[], int terms) {
    FILE *fp;
    fp = fopen("ap_data.dat", "w");
    if (fp == NULL) {
        return;
    }

    fprintf(fp, "n_value y_value\n");
    for (int i = 0; i < terms; i++) {
        fprintf(fp, "%d %f\n", n_values[i], y_values[i]);
    }

    fclose(fp);
}

int main() {
    float initial, commonDiff;
    int terms;
    
    printf("Enter initial term: ");
    scanf("%f", &initial);
    
    printf("Enter common difference: ");
    scanf("%f", &commonDiff);
    
    printf("Enter number of terms: ");
    scanf("%d", &terms);

    int n_values[terms];
    float y_values[terms];

    generateAP(initial, commonDiff, terms, n_values, y_values);
    saveToDatFile(n_values, y_values, terms);

    return 0;
}

