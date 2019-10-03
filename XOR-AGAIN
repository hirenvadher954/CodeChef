
#include <stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    while(n--){
      int N;
      scanf("%d",&N);
      
      int a[N];
      
       for(int i=0;i<N;i++){
           scanf("%d",&a[i]);
       }
      int index =0;
      for(int i=0;i<N;i++){
          a[i]=2*a[i];
      }
       for(int i=1;i<N;i++){
          a[i]^=a[i-1];
      }
      printf("%d\n",a[N-1]);
      
}
    return 0;
}
