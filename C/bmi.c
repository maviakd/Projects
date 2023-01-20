/*
This program will calculate an individuals BMI
Made by Djodan Maviaki 10/3/17
Language written in C
*/

#include <stdio.h>
int main (void)
{
double	weight,
		height,
		bmi;

printf("Enter your weight ");
scanf("%lf", &weight);
printf("Enter your height in inches ");
scanf("%lf", &height);
bmi = (704*weight)/(height*height);

if (bmi< 18.5) {printf("you are underweight\n");}
else if (bmi <= 25.0){printf("you are Normal\n");}
else if (bmi <= 30.0) {printf("You are Overweight\n");}
else {printf("You are Obese\n");}

printf("Your body mass index (BMI) is %6.1f \n", bmi);
return 0;


}


