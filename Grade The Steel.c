#include <stdio.h>

int main(void) {
  int t;
  scanf("%d", & t);
  while(t--){
    int x, z;
    float y;
    scanf("%d %f %d", & x, & y, & z);
    if (x > 50 && y < 0.7 && z > 5600)
      printf("10\n");
    else if (x > 50 && y < 0.7)
      printf("9\n");
    else if (y < 0.7 && z > 5600)
      printf("8\n");
    else if (x > 50 && z > 5600)
      printf("7\n");
    else if (x > 50 || y < 0.7 || z > 5600)
      printf("6\n");
    else
      printf("5\n");
  }
  return 0;
}
