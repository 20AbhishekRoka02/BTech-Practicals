#include<stdio.h>
#include<string.h>

char stack[50];
char input[50];
int top = 0;

void reduce()
{
    int flag = 1;

    while(flag)
    {
        flag = 0;

        // E -> i
        if(stack[top] == 'i')
        {
            stack[top] = 'E';
            printf("Reduce E->i\n");
            flag = 1;
        }

        // E -> E+E
        else if(stack[top] == 'E' && stack[top-1] == '+' && stack[top-2] == 'E')
        {
            top = top - 2;
            stack[top] = 'E';
            stack[top+1] = '\0';

            printf("Reduce E->E+E\n");
            flag = 1;
        }

        // E -> E*E
        else if(stack[top] == 'E' && stack[top-1] == '*' && stack[top-2] == 'E')
        {
            top = top - 2;
            stack[top] = 'E';
            stack[top+1] = '\0';

            printf("Reduce E->E*E\n");
            flag = 1;
        }

        // E -> (E)
        else if(stack[top] == ')' && stack[top-1] == 'E' && stack[top-2] == '(')
        {
            top = top - 2;
            stack[top] = 'E';
            stack[top+1] = '\0';

            printf("Reduce E->(E)\n");
            flag = 1;
        }
    }
}

int main()
{
    int i = 0;

    printf("Enter expression: ");
    scanf("%s", input);

    strcat(input,"$");

    stack[0] = '$';
    stack[1] = '\0';

    printf("\nStack\tInput\tAction\n");

    while(input[i] != '$')
    {
        printf("%s\t%s\tShift %c\n", stack, input+i, input[i]);

        stack[++top] = input[i];
        stack[top+1] = '\0';

        i++;

        reduce();
    }

    reduce();

    if(strcmp(stack,"$E") == 0)
        printf("\nString Accepted\n");
    else
        printf("\nString Rejected\n");

    return 0;
}
