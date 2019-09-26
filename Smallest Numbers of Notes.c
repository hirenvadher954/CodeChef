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
/*
Diffrent Way to solve it.
#include <stdio.h>

int main(void) {
    int i,t,n,s,a,b,c,p,q,sum;
	scanf("%d",&t);
	for(i=0; i<t; i++)
	{
	    scanf("%d",&n);
	    s=n/100;
	    n=n%100;
	    a=n/50;
	    n=n%50;
	    b=n/10;
	    n=n%10;
	    c=n/5;
	    n=n%5;
	    p=n/2;
	    n=n%2;
	    q=n/1;
	    sum=s+a+b+c+p+q;
	    printf("%d\n",sum);
	}
	
	return 0;
}
*/



