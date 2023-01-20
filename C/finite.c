#include <stdio.h>

void even (int start, int end);
void all (int start, int end);

int main (void){
	
	int num, start, end;
	
	printf("Enter 1 for all numbers 2 for odd numbers ");
	scanf("%d", &num);
	printf("Enter the starting number ");
	scanf("%d", &start);
	printf("Enter the ending number ");
	scanf("%d", &end);
	
	if (num == 1)all(start, end);
	else if (num == 2)even(start, end);
	else return ;
	
}


void all (int start, int end){
	
	int a, b, i = start, x = start;
	
	while (i < end){
		i++;
		x  = x + i;
	}
	printf("The sum of all numbers from %d to %d is %d\n", start, end, x);
}

void even (int start, int end){
	
	int a, b, i = start, x = start, even;
	
	while (i < end){
		
		i++;
		even = i % 2;
		if (even == 0){
			x = x + i;
		//printf("i is %d\n", i);
		}
		
		
	}
	printf("The sum of even numbers from %d to %d is %d\n", start, end, x-1);
}
