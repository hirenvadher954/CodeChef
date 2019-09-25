#include <stdio.h>

int main(void) {
    	int n;
    	scanf("%d",&n);
    	
    	while(n--){
    	    int a,b;
    	    scanf("%d %d",&a,&b);
    	    printf("%d %d\n",a>b?a:b,a+b);
    	}
	return 0;
}
