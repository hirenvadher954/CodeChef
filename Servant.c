#include <stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    
    while(n--){
        int a;
        scanf("%d",&a);
        if(a<10){
            printf("What an obedient servant you are!\n");
        }else
            printf("-1\n");
    }

    return 0;
}
