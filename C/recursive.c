#include <stdio.h>

/*

Made by Djodan Maviaki
11/20/2017

This program will query the  user for a number 
If the number is less than 0 it will go through (n*(-6)+3)
If the number is greater than 0 it will go through (n-2)+n-4

Language C


*/

int recur(int n);								//Prototype for recur parameter

int main (void){								//Main parameter
	
	/*
	This is the main oarameter
	Where everything is returned to once calculated
	*/
	
	int x, recursive;							//Initiates two variables
	printf("Enter a Number ");					//Prints out Enter a Number
	scanf("%d", &x);							//Reads inout and saves it as the variable x
	
	recursive = recur(x);						//Calls function recur and saves result from recur as recursive
	
	printf("The output is %d", recursive);		//Prints out the output of recursive 
	
}

int recur(int n){								//Header for recur function
	
	/*
	Made by DjoDan
	This is where all calculations are done sent back
	*/
	
	if (n <= 0)									 
	return(n*(-6)+3);							//Returns this result of n if n is lower than 0
	else 
		return(recur(n-2)+n-4);					//Returns this result if n is greater than 0

	}	
