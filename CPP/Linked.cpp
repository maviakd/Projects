/*
1. Description: Implement of LinkedList and sort a given integer array
2. Author: Djodan
3. Date: 02/01/2018
*/

#include <iostream>
#include <stdio.h>      /* printf, scanf, NULL */

using namespace std;

struct node
{
    int value;
    node *nxt;
};

node* Insert(node *p, int k);
void printLinkedList(node *p);

int main()
{
    int test[] ={4, 8, 2, 1, 5, 6, 66, -11, 34, 7, 3, 21, 17, 7, 9};
    
    node *head = new node; 
    head->value = test[0]; 
    head->nxt = NULL;
    
    for(int i=1; i < 15; i++)
    {
    	
    	
        // call insertion ;  what should you do here ? ???
    }

    // call printlinkedList 
    printLinkedList(head);
    return 0;
}

node* Insert(node *p, int k)
{
    // previous node;  what should you do here ? ???
    
    
    // current node;  what should you do here ? ???
    
    // input node ;  what should you do here ? ???
    
    // bool: append at the end of list or not 
    bool toEnd = true; 
    
    //till the end of the linked list 
    while(current != NULL)
    {
        // insertion before current head
        if(input->value <= p->value)
            {
                // what should you do here ? ???
            }
            
        else
        {
            // great than head, move on for both previous and current
            
            // insertion at tail; do it outside the while loop (this is when current is NULL, how did this happen?)
            if(current == NULL)
                // ?? do something here 
            
            // insertion between head and tail (since not tail and greater than head)  
            if(input->value <= current->value)
                {
                    // what should you do here 
                }
            else 
                continue; 
        }    
        
    }
    
    // insertion at tail; practice on the ? : operation 
    prev->nxt =(toEnd)? input:NULL; 
    return p; 
}

void printLinkedList(node *p)
{
   // print out the elements in p linkedlist 
    cout << endl; 
}
	
}
