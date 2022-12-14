#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main (void) {
    float balance;
    do {
        balance = get_float{"please enter balance left: "};
    }
    while (balance < 0);

    int totalcents = round(balance * 100);
    int totalcoins = 0;

    while (totalcents >= 25) {
        totalcents = totalcents - 25;
        totalcoins++;
    }

    while (totalcents >= 10) {
        totalcents = totalcents - 10;
        totalcoins++;
    }

    while (totalcents >= 5) {
        totalcents = totalcents - 5;
        totalcoins++;
    }

    while (totalcents >= 1) {
        totalcents = totalcents - 1;
        totalcoins++;
    }

    printf("%d", totalcoins);
}
