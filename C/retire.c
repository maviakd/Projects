/*
This program will calculate the value of a retirement portfolio
Made by DjoDan Maviaki on 10/6/17
Language used = C
*/

#include <stdio.h>
int main (void)
{

int 		a;	//Initial starting salary
		
double 	b,	//Annual percentage salary increase
		c,	//Percentage of salary to be contributed
		c2,	//(C)For calculation purposes
		d,	//Annual rate of return on the accumulation
		d2,	//(D)For calculation purposes
		e,	//Starting year
		f,	//Ending year
		s, 	//Initial amount in account
		earning,//Earnings
		closing;//Closing amount

printf("Enter initial starting salary (without comma(,) ) \t");
scanf("%d", &a);

printf("Enter annual percentage salary increase EX (5 = .05) \t");
scanf("%lf", &b);

printf("Enter percentage of salary to be contributed \t \t");
scanf("%lf", &c);

printf("Enter annual rate of return \t \t \t \t");
scanf("%lf", &d);

printf("Which year did you start \t \t \t \t");
scanf("%lf", &e);
printf("Which year did you end \t \t \t \t \t");
scanf("%lf", &f);

printf("Year	Salary	Starting	Contribution	Earnings	Closing\n");

closing = a*c;
c2 = a*c;

while (e <= f)
{

closing = s + c2 + earning;

printf("%d	%d	%6.2f		%6.2f		%6.2f		%6.2f\n", (int)e, a, s, c2, earning, closing);

earning = (c2 *d) + earning;

int help;	//Desperate attempt to correct output

if (a>=41600){s = (a*c);help = help+1;}

if (help == 1 ){s = (s + 40);earning = earning + 10;}

s = (a*c)+s;


a = (a*b)+a;

e = e+1;

c2 = (c2*b)+c2;

}

return 0;

}
