/*

Keloids
printf("The selected number was %d\n", a);

*/
#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#define randnum(min, max) \
((rand() % (int)(((max) + 1) - (min))) + (min))

void get_mode(int *in);
void easy_mode(int *in, int *pott);
void hard_mode(int *in, int *pott);

int main (void){
	
	srand(time(NULL));
	
	int input, pot, gold, mode;
	
	get_mode(&input);

	if (input == 2)easy_mode(&input, &pot);
	if (input == 1)hard_mode(&input, &pot);
	
}

void get_mode(int *in){
	int a, b, num;
	printf("Choose a level \n Level 1(Easy) Level 2(Hard) or pick 3 for random \nEx(1, 2, 3) ");
	scanf("%d", &num);
	
	if (num == 3){
		a = randnum(1, 20);
		b = a % 2;
		if (b == 0)a = 1;
		else a = 2;
	}
	else if (num == 2)a = 2;
	else if (num == 1)a = 1;
	else {
		printf("Please enter a valid number");
		return;
	}
	*in = a;
	return;
}

void easy_mode(int *in, int *pott){
	printf("Welcome to easy mode\n");
	int doom, x;
	char select;
	
	printf("Would you like to select your pot number? (Y/N)\n");
	scanf("\n%c", &select);
	printf("You have selected %c", select);
	
while (x < 4){	//Loop to check for incorrect user input
if (select == 'y' || select == 'Y' || select == 'n' || select == 'N')break;
else {printf("Unrecognized Input. Try Again");return 0;}
}
	
}

void hard_mode(int *in, int *pott){
	
	printf("Welcome to Hard mode");
	
}
