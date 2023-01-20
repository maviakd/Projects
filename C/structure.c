/*
This program will query the user for his first name, 
last name, age, and height and save it in a structure.

Made from Djodan maviaki
11/31/2017
Language-C
*/

#include <stdio.h>

typedef struct{														//Creates an enumerated structure
		char f_name[10];											//Creates a character variable
		char l_name[10];											//Creates a character variable
		int age[2];													//Creates an integer variable 2 digits long
		int height[3];												//Creates an integer variable 3 digits long
	}person;														//The name of the structure 
	
	void get_letters(person *letters);								//Prototype for funtion
	void get_numbers(person *numbers, int *height, int *age);		//Prototype for funtion
	void print(person *letters, int *height, int *age);				//Prototype for funtion

int main(void){														//Main funtion header
	
	/*
	Main function
	Saves data
	Passes saved data to all functions
	*/
	
	int height, age;												//Creates an integer named height and age
	person letters;													
	person numbers;
	get_letters(&letters);											//Sends the structure letters to function get_letters
	get_numbers(&numbers, &height, &age);							//Sends the structure numbers, height and age to the funtion get_numbers
	print(&letters, &height, &age);									//Sends the structure letters, height, and age all passed by reference
	return 0;
}

void get_letters(person *letters){									//Header for function get_letters
	
	/*
	Funtion get_letters
	Gets the users first and last name
	Saves it in the structure
	*/
	
	printf("Enter your first name ");								//Prints out statement
	gets((*letters).f_name);										//Gets a string from the user
	printf("Enter your last name ");								//Prints out statement
	gets((*letters).l_name);										//Gets a string from the user
	return;															//Returns to the main function
}

void get_numbers(person *numbers, int *height, int *age){			//Header for function get_numbers
	
	/*
	Function get_numbers
	Gets numerical data from user 
	Such as age and height
	Stores it and passes it back by reference
	*/
	
	int a, h;														//Creates an integer named A and H
	printf("Enter your age ");										//Prints out statement
	scanf("%d", &a);												//Gets an integer from the user
	printf("Enter your height in inches ");							//Prints out statement
	scanf("%d", &h);												//Gets an integer from the user
	*age = a;														//Pointer *age is equal to local variable A
	*height = h;													//Pointer *height is equal to local veriable H
	return;															//return to the main function
	
}

void print(person *letters, int *height, int *age){					//Header for print function
	
	/*
	Function Print
	This function gathers all saved data
	Then prints it in a specific sequence 
	*/
	
	printf("Hello %s %s\nYou are %d years old and %d inches tall", 	//Prints out statement
	(*letters).f_name, (*letters).l_name,*age, *height);			//points to data stored in structure and data passed by reference
	return;															//Returns to main function
}

