#include <stdio.h>

int main()
{
    int n,a,b,t1=0,t2=0,d1=0,d2=0,lead1=0,lead2=0;
    scanf("%d",&n);
    while(n--){
        scanf("%d %d",&a,&b);
        t1 = t1 + a;
        t2 = t2 + b;
        
        if(t1>=t2)
            d1 = t1 - t2;
        if(t1<t2)
            d2 = t2 - t1;
        if(d1>lead1)
            lead1 = d1;
        if(d2>lead2)
            lead2 = d2;
        }
     if(lead1>lead2)
            printf("1 %d\n",lead1);
     if(lead2>lead1)
            printf("2 %d\n",lead2);        
    return 0;
}
