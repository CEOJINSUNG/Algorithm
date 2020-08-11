#include <stdio.h>

int Factorial(int n)
{
	int result = 1;
	for (int i = n; i > 0; --i)
	{
		result = result * i;
	}
	return result;
}

int main () {
    int num;
    scanf("%d", &num);
    printf("%d", Factorial(num));
    return 0;
}