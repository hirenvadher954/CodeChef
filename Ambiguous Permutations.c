
#include <stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    while(n--){
        int a,rev=0;
        scanf("%d",&a);
        int bckp = a;
        
        while(a!=0){
            int temp=0;
            temp = a%10;
            rev = rev*10+temp;
            a = a/10;
        
        }
        
        if(bckp==rev){
            printf("wins\n");
        }else
            printf("losses\n");
    }

    return 0;
}
