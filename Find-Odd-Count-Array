//Problem-Find out Odd number of count from given Array
//Input - 8
//Input - 1 1 2 2 3 2 3
//Output- 2

#include <stdio.h>

int main()
{
    int N;
    scanf("%d",&N);
    int coin[N-1];
    
    for(int i=0;i<N-1;i++){
        scanf("%d",&coin[i]);
    }
    
    for(int i=0;i<N-1;i++){
        int count=0;
        for(int j=0;j<N-1;j++){
            if(coin[i]==coin[j]){
                count++;
            }
        }
          if(count%2 == 1){
              printf("%d ",coin[i]);
              return 0;
          }
    }

    return 0;
}
