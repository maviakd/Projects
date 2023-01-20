/*
1. Description: Implement of LinkedList and sort a given integer array
2. Author: Fu
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
void addNode(node *p, int k); 

int main()
{
    int test[] ={4, 8, 2, 1, 5, 6, 66, -11, 34, 7, 3, 21, 17, 7};
    int arrySize = sizeof(test)/4;
    
    node *head = new node; 
    head->value = test[0]; 
    head->nxt = NULL;
    
    for(int i=1; i < arrySize; i++)
    {
        head = Insert(head, test[i]);
    }

    printLinkedList(head);
    return 0;
}

node* Insert(node *p, int k)
{
    node *prev = new node; 
    prev->nxt = p; 
    
    node *current;  
    current = p; 
    
    node *input = new node;
    input->value = k;
    input->nxt = NULL;
    
    bool toEnd = true; 
    
    while(current != NULL)
    {
        // insertion before current head
        if(input->value <= p->value)
            {
                prev->nxt = input; 
                input->nxt = p; 
                p = input; 
                return p; 
            }
            
        else
        {
            prev = current; 
            node *tmp = current->nxt; 
            current = tmp; 
            
            // insertion at tail; do it outside the while loop 
            if(current == NULL)
                break; 
            
            // insertion between head and tail 
            if(input->value <= current->value)
                {
                    prev->nxt = input; 
                    input->nxt = current; 
                    return p; 
                }
            else 
                continue; 
        }    
        
    }
    prev->nxt =(toEnd)? input:NULL; 
    return p; 
}

void printLinkedList(node *p)
{
    while (p != NULL)
    {
        cout << p->value << "  ";
        p = p->nxt; 
    }
    cout << endl; 
}
