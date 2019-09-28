
#include <stdio.h>


int main()
{
    int t;
    scanf("%d",&t);
    while(t--){
        int a,b;
        scanf("%d %d",&a,&b);//2 //3
        for(int i=a;i>0;i--){
            b = (b*(b+1))/2;
        }
        printf("%d\n",b);
    }
    
    return 0;
}
