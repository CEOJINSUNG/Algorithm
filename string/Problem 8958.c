#include <stdio.h>

int main() {
	int a,score=0;
	int add=1;
	scanf("%d",&a);
	char arr[81];
	for (int i=0;i<a;i++)
	{
		
		scanf("%s",arr);
		for (int I=0;I<80;I++)
		{
			if (arr[I]=='O')
			{
				score+=add;
				add++;
			}
			else
			{
				add=1;
			}
			arr[I]='\0';
		}
		printf("%d\n",score);
		add=1;
		score=0;
	}
}