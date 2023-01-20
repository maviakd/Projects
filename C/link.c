/*
{This program was adopted from "Linked lists of appointments" by Ronald Sarner }

This program illustrates a linked list
to ask for 3 individuals first name, last name, a 3 digit id number

Made by Djodan Maviaki 12/12/2017
Language - C
*/

#include <stdio.h>	
#include <stdlib.h>       //needed for malloc
#include <string.h>			//Amount of people

#define amount 4

typedef struct people
  {char Fname[21];         //20 character array for first name
   char Lname[21];         //Last name array for last name
   int id;               	//integer for user id number
   struct people *next;   	//Link to the next list
  }pple;					//name of struct


pple* inputs(pple *first, char fname[], char lname[], int mintime);

int main(void)
{
  pple *head,                //pointer to the head of the list
       *p;                   //Pointer to the next liest
  char client[21];           
  char lname[21];
  int  id,
       j,                   
       k;                    
  char ch,                   
       nl;                   

  head=NULL;
  for(j=0;j<21;j++)          
    client[j]=' ';
  for(j=0;j<21;j++)          
    lname[j]=' ';
  for(k=0;k<amount;k++)    				//The amount of people
   {printf("Enter first name\n");
    gets(client);							//Gets the first name of the person and stores it in client
    printf("Enter last name:  ");
    gets(lname);							//Gets the last name of the person and stores it in lname
    printf("Enter the Employee ID number:  ");
    scanf("%d", &id);
    scanf("%c", &nl);
    head=inputs (head,client,lname,id);
    for (j=0;j<21;j++)
      client[j]=' ';
    for (j=0;j<21;j++)
      lname[j]=' ';
   }                        //End of the loop
   							//All people are made and all data is entered

   p=head;                  //points to the begining of the list


	k=0;
  while (k!=3)			/*IF AMOUNT IS CHANGED, THIS MUST ALSO BE CHANGED TO -1 */
    { 
    k++;
    p=p->next;
    }
    
    printf("The person with the highest ID number is \n %s, %s",p->Fname,p->Lname);
    printf("\n");
    printf("The employee number is: %d",p->id);
    
    
    
    
}

pple* inputs (pple *first, char fname[], char lname[], int CUR_id)
/* 
This funciton will organize the linked structure and maintain it
Made by Djodan Maviaki
*/

{ pple *p,
       *q,
       *newp;
  int found,
      len,
      i;
  found=0;
  q=first;
  p=first;

  //Finds the correct location or positioning for each list

  while ((p!=NULL) && (!found))		//Is the curent ID higher or lower than the box p is currently representing
    { if (p->id<=CUR_id)			//If higher move over one
          {q=p;
           p=p->next;
          }
      else							//Otherwise put it here
        found=1;
    }

  newp=(pple*) malloc(sizeof(pple));   //Creates a new record pointed to by newp
  newp->id=CUR_id;
  strncpy(newp->Fname, fname, 21);
  strncpy(newp->Lname, lname, 21);

  /*adjust pointers*/

  newp->next=p;							// New p will point to p
  if(q!=p)								//Determining id p and q are the same if not the same , store new p after q 
   q->next=newp;						
  else                                // otherwise we havent made a box yet
   first=newp;
  return(first);
}

