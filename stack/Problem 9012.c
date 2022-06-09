#include <stdio.h>
#include <stdlib.h>

#define MAX_STACK_SIZE 50

typedef char element;

typedef struct {
	element data[MAX_STACK_SIZE];
	int top;
}StackType;

void init_stack(StackType* s)
{
	s->top = -1;
}

int is_empty(StackType* s)
{
	return (s->top == -1);
}

int is_full(StackType* s)
{
	return (s->top == (MAX_STACK_SIZE - 1));
}

void push(StackType* s, element item)
{
	if (is_full(s))
	{
		return;
	}
	else s->data[++(s->top)] = item;
}

element pop(StackType* s)
{
	if (is_empty(s))
	{
		return -1;
	}
	else
		return s->data[(s->top)--];
}

element peek(StackType* s)
{
	if (is_empty(s))
	{
		return -1;
	}
	else return s->data[(s->top)];
}

int main()
{
	int k,i,flag,len;
	char t[50];
	StackType s;
	scanf("%d", &k);
	getchar();
	flag = 0;
	while (k--)//k번 반복
	{
		init_stack(&s);//스택 초기화
		flag = 0;
		scanf("%s", t);
		len = strlen(t);//괄호 개수 저장
		for (i = 0; i < len; i++)//괄호 개수만큼 검사
		{
			if (t[i] == '(')
				push(&s, t[i]);
			else// ')'
			{
				if (is_empty(&s))//비어있으면 flag에 1 넣고 빠져나옴
				{
					printf("NO\n");
					flag = 1;
					break;
				}
				else//()를 합쳐서 뺌(pop)
				{
					pop(&s);
				}
			}
		}
		if (flag)//앞에서 NO를 출력한 경우 중복출력을 피함
			continue;
		if (is_empty(&s))//'('가 남아있으면 안됨
			printf("YES\n");
		else
			printf("NO\n");
	}

	return 0;
}