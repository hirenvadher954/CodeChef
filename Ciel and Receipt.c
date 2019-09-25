
#include <stdio.h>
#include<math.h>
int main()
{
    int n;
    scanf("%d",&n);
    
    while(n--){
        int a,count=0;
        scanf("%d",&a);
        if(a>2048){
            count = a/2048;
            a = a%2048;
        }
        while(a!=0){
            if(a%2)
                count++;
            a = a/2;    
        }
       
        printf("%d\n",count);
    }

    return 0;
}
