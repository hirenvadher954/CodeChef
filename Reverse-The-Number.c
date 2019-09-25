
#include <stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    
    while(n--){
        int a,reverse=0;
        scanf("%d",&a);
        while(a!=0){
            int temp = a%10;
            reverse = reverse*10 + temp;
            a = a/10;
        }
        printf("%d\n",reverse);
    }

    return 0;
}
