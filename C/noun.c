/*

This program will query the user for a non plural noun 
and return the plural version of the word

Made Djodan Maviaki on 11/10/17

Language - C

*/

#include <stdio.h>
#include <string.h>

int main () {									//Main class
	int 
	len; 										//Length of the string								
    char 
	str[50], 									//String location
	last;										//Last digit of the string
	
	printf("Please enter a noun\n");			//prints statement
	scanf("%s", &str);							//Provides input for the string(noun)
		
    len = strlen(str);							//Length of the string
    last = str[len-1];							//Last letter of the string
   
    printf("Length of |%s| is |%d|\n", str, len);
    printf("Position[%d] is %c\n", len, last);	//prints the last letter of the string
	
	if (last == 'y'){							//checks if the last letter is 'Y'
		str[len-1] = 'i';						//Overwrites last letter of string with 'i'
		str[len] = 'e';							//Overwrites last letter of string with 'e'
		str[len+1] = 's';						//Overwrites last letter of string with 's'
		str[len+2] = '\0';						//Adds a null at the end of the string
		printf("The new word is %s", str);
		return 0;
	}
	else if (last == 's'){
		str[len] = 'e';							//Overwrites last letter of string with 'e'
		str[len+1] = 's';						//Overwrites last letter of string with 's'
		str[len+2] = '\0';						//Adds a null at the end of the string
		printf("The new word is %s", str);		
		return 0;
	}
	else if (last == 'h'){
		str[len] = 'e';							//Overwrites last letter of string with 'e'
		str[len+1] = 's';						//Overwrites last letter of string with 's'
		str[len+2] = '\0';						//Adds a null at the end of the string
		printf("The new word is %s", str);		
		return 0;	
	}
	else if (last == 'c' && last == 'h'){
		str[len] = 'e';							//Overwrites last letter of string with 'e'
		str[len+1] = 's';						//Overwrites last letter of string with 's'
		str[len+2] = '\0';						//Adds a null at the end of the string
		printf("The new word is %s", str);	
		return 0;
	}
	else if (last == 'n'){
		str[len] = 's';							//Overwrites last letter of string with 's'
		str[len+1] = '\0';						//Adds a null at the end of the string
		printf("The new word is %s", str);
		return 0;
	}
	else if (last == 'f'){
		str[len-1] = 'v';						//Overwrites last letter of string with 'v'
		str[len] = 'e';							//Overwrites last letter of string with 'e'
		str[len+1] = 's';						//Overwrites last letter of string with 's'
		str[len+2] = '\0';						//Adds a null at the end of the string
		printf("The new word is %s", str);
		return 0;
	}
	else {
		str[len] = 's';							//Overwrites last letter of string with 's'
		str[len+1] = '\0';						//Adds a null at the end of the string
		printf("The new word is %s", str);		
		return 0;
	}	
   
   return(0);
}

