#include<stdio.h>
#include<string.h>

int main(void){
    int t,count=0;
    scanf("%d",&t);
    
    while(t--){
        char a[100],flag=0;
        scanf("%s",a);
        
        for(int i=0;i<strlen(a);i++){
            if((a[i]=='c'&&a[i+1]=='h')||(a[i]=='h'&&a[i+1]=='e')||(a[i]=='e'&&a[i+1]=='f'))
	            flag=1;
        }
        
         if(flag==1)
	        count++;
    }
    
    printf("%d\n",count);
}
