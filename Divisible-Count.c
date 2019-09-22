//problem- how many integer are divisible by d;
#include <stdio.h>

int main()
{
    int n,d,count=0;
    scanf("%d %d",&n,&d);
    int a[n];
    
        for(int i=0;i<n;i++){
            scanf("%d",&a[i]);
            if(a[i]%d==0)
                count++;
        }    
        
        printf("%d\n",count);
        
    return 0;
}

// 7 3
// 1
// 51
// 966369
// 7
// 9
// 999996
// 11

// Output:
// 4
