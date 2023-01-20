/*
This program will...
Made by Djodan Maviaki 10/16/17
Language used - C

odd number - a number that is not divisible by 2
even number - number that is divisible by two
prime number - number that is only divisible by one and itsleft
composite - 
*/
#include <stdio.h>


void get_input(int *in);
void check_input(int *input, int *answer, int *summ, int *prim);

int main (void){

	int num, ans, sum, prime;

	get_input(&num);	//Gets the User input
	printf("Main number = %d\n", num);
	
	check_input(&num, &ans, &sum, &prime);	//Where all the calculations are done
	
	//part one
	if (ans == 1) printf("The number %d is a multiple of 7\n", num);
	else if (ans == 2)printf("The number %d is a multiple of 11\n", num);
	else if (ans == 3)printf("The unumber %d is a multiple of 13\n", num);
	else printf("The Number %d is not a multiple of 7, 11, 13\n", num);
	
	//part two
	printf("The Sum is %d\n",sum);
	
	//part three
	if (prime == 1)printf("The number %d is a prime number\n", num);
	else if(prime == 0)printf("The number %d is not a prime number\n", num);
	return 0;

}


void get_input(int *in){	//scans for integer
	printf("Input an integer ");
	int a;
	scanf("%d", &a);
	*in = a;
	return ;

}

void check_input(int *input, int *answer, int *summ, int *prim){
int one, two, three, four;

//part one 
one = *input % 7;
two = *input % 11;
three = *input % 13;
if (one == 0) *answer = 1;
else if (two == 0) *answer = 2;
else if (three == 0) *answer = 3;
else *answer = 0;


//part two
int n, sum = 0, r, q;
n = *input;
while (n != 0){
	r = n%10;
	q=n/10;
	sum = sum+r;
	n = q;
}
*summ = sum;

//part three
int prime, calc = 2;
prime = *input;
while (calc != prime){
	if (*input % calc != 0){
	// (prime % calc == 0){
		*prim = 1;
		calc = calc + 1;
		}
	else{
		calc = *input;
		*prim = 0;
		}
}

four = *input % 2;
if (four == 0){*prim = 0;}
return ;
	
}
