#include <stdio.h>
long long int GCD(long long int a, long long int b) {
    if(b == 0) return a;
    else return GCD(b, a%b);
}
int main(void) {
	int T;
	long long int a, b;
	scanf("%d", &T);
	for(int i = 0; i<T; i++){
	    scanf("%lld %lld", &a, &b);
	    long long int gcd = GCD(a, b);
	    long long int lcm = a*b/gcd;
	    printf("%lld %lld\n", gcd, lcm);
	}
	return 0;
}
