#include <stdio.h>
int main(){
	int x, y;
	for(;;){
		scanf("%d %d", &x, &y);
		if(x == 0 && y == 0)
			break;
		x > y ? printf("Yes\n") : printf("No\n");
	}
}