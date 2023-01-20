/*Program to illustrate insertion into a linked list
  Adapted from Mullick & Sarner, Structure of Programming Languages, 1996
  pp. 93-94...nested structs eliminated

  Language: C (gcc target)

*/

#include <stdio.h>
#include <stdlib.h>       //needed for malloc
#include <string.h>



typedef struct people{														//Creates an enumerated structure
		char f_name[10];											//Creates a character variable
		char l_name[10];											//Creates a character variable
		int id;													//Creates an integer variable 3 digits long
		struct people *next;
	}info;
	
//void get_letters(info *f_name, info *l_name);								//Prototype for funtion
//void get_numbers(info id);

int main(){
	
	int i;
	info *head;
	info *p;
	info *q;
	
	p = (info*) malloc(sizeof(info));
	printf("Enter your first name \t");
	scanf("%s",(p->f_name));
	printf("Enter your last name \t");
	scanf("%s",(p->l_name));
	printf("Enter your id number \t");
	scanf("%d",&p->id);
	
	
	q = (info*) malloc(sizeof(info));
	printf("Enter your first name \t");
	scanf("%s",(q->f_name));
	printf("Enter your last name \t");
	scanf("%s",(q->l_name));
	printf("Enter your id number \t");
	scanf("%d",&q->id);
	q = p->next;
	
	if ()
		
}
