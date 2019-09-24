#include <stdio.h>

int main()
{
    int n,a;
    scanf("%d",&n);
    while(n--){
        int count=0;
        scanf("%d",&a);
        
        while(a!=0){
            int temp;
             temp = a%10;
             if(temp == 4)
                count++;
             a = a/10;
        }
        printf("%d\n",count);
    }
    
    return 0;
}
