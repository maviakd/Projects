/*
Made by Djodan Maviaki
This is a gambling game
You are awarded gold after every round
If the your number is divisivle by your doom number
You loose everything and the game is over

					Rules
Welcome to gamble The rules are simple. You are given a number between 2-7 lableled as your doom number. After your first turn, you have the option to end the game and keep your gold, or gamble it and attempt to get more, also risking loosing it all. You loose if your amount of gold is divisible by your curent amount of gold

*/


#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#define randnum(min, max) \
((rand() % (int)(((max) + 1) - (min))) + (min))

int main(void)
{
srand(time(NULL));

int 	game, 
	gold, 
	ngold, 
	doom, 
	tries = 4, 
	pot, div, 
	game_over;

pot = randnum(1, 7);
doom = randnum(2, 4);

if (pot == 1){gold = randnum(1, 100);}
if (pot == 2){gold = randnum(100, 200);}
if (pot == 3){gold = randnum(200, 300);}
if (pot == 4){gold = randnum(300, 400);}
if (pot == 5){gold = randnum(400, 500);}


printf("POT Number\t = \t %d \n", pot);
printf("DOOM Number\t = \t %d \n", doom);


if (doom > 4){printf("Your number is greater than 3\nAborting session");return 0;}

while (game < 4){

char gamble = ' ';	//Variable for user input

printf("Gold \t Trial left \t Gamble?(Y/N) \n");
printf("%d \t %d \t \t ", gold, tries);
scanf("%s", &gamble);


while (game < 4){	//Loop to check for incorrect user input
if (gamble == 'y' || gamble == 'Y' || gamble == 'n' || gamble == 'N')break;
else {printf("Unrecognized Input. Try Again");return 0;}
}


if (gamble == 'n' || gamble == 'N'){	//Breaks the loop if
printf("You have ended with %d", gold);//condition is met
return 0;}

int pots = 0;		
pots = randnum(1, 5);	// Selects random number between 1-5

if (pots == 1){ngold = randnum(1, 100);}
if (pots == 2){ngold = randnum(100, 200);}
if (pots == 3){ngold = randnum(200, 300);}
if (pots == 4){ngold = randnum(300, 400);}
if (pots == 5){ngold = randnum(400, 500);}



div = gold % doom;

if (div == 0){printf("Game over -_- You ended with 0"); 
game_over == game_over + 1;
gold = 0;
return 0;}


game = game + 1;
tries = tries - 1;
gold = gold + ngold;
}

if (game_over == 0){printf("Congrats, You ended with \t %d", gold);}

}
