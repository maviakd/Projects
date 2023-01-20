/*
Made by Djodan Maviaki
9/17/17
This program will calculate the monthly payment of your car loan

p = principal(the amount borrowed)
i = monthly interest rate
n = total number of payments
a = anual interest rate
*/

#include <stdio.h>
#include <math.h>

int main(void)
{

double p, i, n, a, total;

printf("amount borrowed ");
scanf(" %lf", &p);

printf("annual interest rate ");
scanf(" %lf", &a);

printf("number of payments ");
scanf(" %lf",& n);

i = a/12;

total = (i*p)/(1-pow(1.0+i, -n));


// (i*p)(1-(1+i)**-n)

printf("Your total is %6.2f", total);

return 0;


}


