#include <stdio.h>

int main()
{
    int N,temp=0;
    scanf("%d",&N);
    int coin[N-1];
    
    for(int i=0;i<N-1;i++){
        scanf("%d",&coin[i]);
        temp = temp^coin[i];
    }
    
    printf("%d ",temp);

    return 0;
}
