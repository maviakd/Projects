#include <stdio.h>
#define randnum(min, max) \
((rand() % (int)(((max) + 1) - (min))) + (min))

void get_in(int array[], int *num);
void get_put(int a, int *n);

int main (void){
	srand(time(NULL));
	
	int a[10], n;
	
	get_input(a, &n);
	
	
}


void get_put(int a, int *n){
	
	int entry, i;
	printf("enter a max of 10 digits. Enter -1 to end");
	scanf("%d", &entry);
	while (entry >= 0){
		
		
	}
	
}
