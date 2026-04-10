#include<stdio.h>
#include<string.h>

char stack[50], input[50];
int top=-1,i=0;

void push(char c){ stack[++top]=c; }
void pop(){ top--; }

int main()
{
    printf("Enter string: ");
    scanf("%s",input);

    strcat(input,"$");

    push('$');
    push('E');

    printf("\nStack\tInput\tAction\n");

    while(top>=0)
    {
	if (stack[top] == '$') break;
        printf("%s\t%s\t",stack,input+i);

        if(stack[top]==input[i]) 
        {
            printf("Match %c\n",input[i]);
            pop();
            i++;
        }

        else if(stack[top]=='E')
        {
            printf("E->TA\n");
            pop(); push('A'); push('T');
        }

        else if(stack[top]=='A' && input[i]=='+')
        {
            printf("A->+TA\n");
            pop(); push('A'); push('T'); push('+');
        }

        else if(stack[top]=='A')
        {
            printf("A->e\n");
            pop();
        }

        else if(stack[top]=='T')
        {
            printf("T->FB\n");
            pop(); push('B'); push('F');
        }

        else if(stack[top]=='B' && input[i]=='*')
        {
            printf("B->*FB\n");
            pop(); push('B'); push('F'); push('*');
        }

        else if(stack[top]=='B')
        {
            printf("B->e\n");
            pop();
        }

        else if(stack[top]=='F' && input[i]=='i')
        {
            printf("F->i\n");
            pop(); push('i');
        }

        else if(stack[top]=='F' && input[i]=='(')
        {
            printf("F->(E)\n");
            pop(); push(')'); push('E'); push('(');
        }

        else
        {
            printf("Error\n");
            return 0;
        }
    }

    if(input[i]=='$')
        printf("\nString Accepted\n");
    else
        printf("\nString Rejected\n");
}
