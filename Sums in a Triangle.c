
#include <stdio.h>

int main()
{
    int t;
    scanf("%d",&t);
    while(t--){
        int n,i,j;
        scanf("%d",&n);
        int arr[n][n];
        for(i=0;i<n;i++){
			for(j=0;j<=i;j++)
				scanf("%d",&arr[i][j]);
		}
		
		for(i=n;i>1;i--)
		{
			for(j=0;j<i;j++)
			{
				if(arr[i-1][j]<arr[i-1][j+1])
					arr[i-2][j]+=arr[i-1][j+1];
				else
					arr[i-2][j]+=arr[i-1][j];
			}
		}
        
        printf("%d\n",arr[0][0]);
    }

    return 0;
}
