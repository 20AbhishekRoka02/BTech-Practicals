%{
#include<stdio.h>
#include<string.h>
%}

%%

int|float|char|if|else|while|for|return    { printf("Invalid Identifier (Keyword)\n"); }

[a-zA-Z_][a-zA-Z0-9_]*                    { printf("Valid Identifier\n"); }

.*                                        { printf("Invalid Identifier\n"); }

%%

int main()
{
    printf("Enter Identifier:\n");
    yylex();
    return 0;
}

int yywrap()
{
    return 1;
}
