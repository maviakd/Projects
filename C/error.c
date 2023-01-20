/*

This will display the representational error 
between fractions from 1/2 to 1/30

Program made in C by Djodan Maviaki
10/30/17
*/

#include <stdio.h>

int main (void){					//Main parameter of the program
	
double n = 1.0, d = 2.0, c, sum, x;	//Initiates variables used for this program


for (d = 2; d <= 30; d++){			//primary for loop, increments denominator
	
	for (c = 1; c <= d; c++){		//Secondary for loop, adds an amount a repeated number of times
		x = 0;						//Resets value of x to 0	
		x = n/d;					//Calculation of the fraction
		sum = sum + x;				//sums up the divisions of the fraction and stores it
		
		
	}
	
	int num =  n , den = d;			//Integer values of numerator and denomirator
	if (sum == 1)printf("adding %d/%d %d times is equal to one\n", num, den, den);		//Checks if sum is equal to 1
	else if (sum < 1)printf("adding %d/%d %d times is less than one\n", num, den, den);	//Checks if sum is less than 1
	else printf("adding %d/%d %d times is greater than one\n", num, den, den);			//Checks if sum is greater than 1
	sum = 0;						//resets the value of the sum to 0
	
}

}
