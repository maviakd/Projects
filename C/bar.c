#include <stdio.h>
/*
This program will...
*/

int main (void){
	
	int bar[12], i = 1, x = 0, odd, even, sum, check;
	
	for (i = 0; i < 12; i++){
		
		bar[i] = 0;
		
		printf("Enter number %d\n", i);
		scanf("%d", &x);
		if (x>9){printf("Your digit is greater than 9 \nAborting session");return 0;}
		bar[i] = 0;
		bar[i] = x;		
		
		
		
	}
	
	printf("%d %d %d %d %d %d %d %d %d %d %d %d\n",
	bar[0], bar[1], bar[2], bar[3], bar[4], bar[5], bar[6], bar[7], bar[8], bar[9], bar[10],bar[11]);

	odd = (bar[0] + bar[2] + bar[4] + bar[6] + bar[8] + bar[10]) * 3; 
	even = (bar[1] + bar[3] + bar[5] + bar[7] + bar[9] + bar[11]) ; 
	sum = even + odd;
	printf("The suum is %d\n", sum);

	int n, sums = 0, r, q, b=0, num[3];
	n = sum;
	while (n != 0){
	b++;
	r = n%10;
	num[b] = r;
	q=n/10;
	sums = sums+r;
	n = q;
//	printf("r is %d\t", r);
	}
	printf("\nP1 %d P2 %d P3 %d\n",num[2], num[1], num[0]);
	printf("odds are %d\tevens are %d\tthe sum is %d\n", odd, even, sum);
	
	if (num[0] == 0){check = 0;}
	else {check = 10 - num[0];}
	printf("check is %d", check);
	getchar();getchar();
}
