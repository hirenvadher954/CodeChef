
#include <stdio.h>

int main()
{
    int n,e=0,o=0;
    scanf("%d",&n);
    
    int a[n];
    
    for(int i=0;i<n;i++)
        scanf("%d",&a[i]);
        
    for(int i=0;i<n;i++){
        if(a[i]%2==0)
            e++;
       else if(a[i]%2==1)
            o++;
    }   
    
    if(e>o)
        printf("READY FOR BATTLE\n");
    else if(o>=e)
        printf("NOT READY\n");
    return 0;
}
