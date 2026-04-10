%{
#include<stdio.h>
%}

%%

^abb$      { printf("Accepted under rule: abb\n"); }

^a$        { printf("Accepted under rule: a\n"); }

^a*b+$     { printf("Accepted under rule: a*b+\n"); }

.*         { printf("Not accepted\n"); }

%%

int main()
{
    printf("Enter string:\n");
    yylex();
    return 0;
}

int yywrap()
{
    return 1;
}
