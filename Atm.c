#include <stdio.h>

int main(void) {
    int n,sum=0,i;
    scanf("%d",&n);
    while(n--){
        int num,temp;
         scanf("%d",&num);
          temp = num % 10;
         while(num!=0){
             i=num;
          num = num / 10;
         }
         
         printf("%d\n",i+temp);
    }     
	return 0;
}
