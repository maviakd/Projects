//Reference perameter

#include <stdio.h>

void snidley(int *dudley, int *nell);
void green_acres(int *fred, int *arnold);

int main (void){

int rocky = 3, bw = 4, boris = rocky + bw;

snidley(&rocky, &boris);

printf("rocky is %d be is %d boris is %d", rocky, bw, boris);

return 0;

}

void snidley(int *dudley, int *nell){

int oscar;
oscar = (*dudley) ^ (*nell);
*dudley = oscar + 2;
*nell = (*dudley) - 1;
printf("oscar is %d dudkey is %d nell is %d \n", oscar, *dudley, *nell);

green_acres(nell, &oscar);
///printf("oscar %d dudley %d nell %d", );

return ;

}

void green_acres(int *fred, int *arnold){

int haney;

haney = (*fred) + (*arnold)*2;
*fred = haney + 3;
*arnold = (*fred) + haney;
printf("fred is %d arnold is %d haney is %d\n", fred, arnold, haney);

return ;

}




