#include <stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    
    while(n--){
        int b,a;
        scanf("%d %d",&a,&b);
        printf("%d\n",a+b);
    }

    return 0;
}
