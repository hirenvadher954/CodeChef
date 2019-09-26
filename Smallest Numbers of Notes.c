#include <stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    
    while(n--){
       int a,count=0;
       scanf("%d",&a);
       if(a>=100){
           count += a/100;
           a = a%100;
       }
       if(a>=50){
           count += a/50;
           a = a%50;
       }
       if(a>=10){
           count += a/10;
           a = a%10;
       }
        if(a>=5){
           count += a/5;
           a = a%5;
       }
        if(a>=2){
           count += a/2;
           a = a%2;
       }
        if(a>=1){
           count += a/1;
           a = a%1;
       }
       
       printf("%d\n",count);
    }

    return 0;
}
