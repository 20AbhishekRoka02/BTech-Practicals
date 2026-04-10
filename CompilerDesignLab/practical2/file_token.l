%{
#include<stdio.h>
%}

%%
int|float|char|if|else|while|for|return     { printf("KEYWORD: %s\n", yytext); }

[0-9]+                                     { printf("NUMBER: %s\n", yytext); }

[a-zA-Z_][a-zA-Z0-9_]*                     { printf("IDENTIFIER: %s\n", yytext); }

[+\-*/=%]                                  { printf("OPERATOR: %s\n", yytext); }

[(){};,]                                   { printf("SPECIAL SYMBOL: %s\n", yytext); }

[ \t\n]+                                   ;   /* ignore whitespace */

.                                          { printf("UNKNOWN: %s\n", yytext); }

%%

int main(int argc, char *argv[])
{
    FILE *fp;

    if(argc != 2)
    {
        printf("Usage: ./file_token <filename>\n");
        return 0;
    }

    fp = fopen(argv[1], "r");

    if(fp == NULL)
    {
        printf("File not found\n");
        return 0;
    }

    yyin = fp;

    yylex();

    fclose(fp);

    return 0;
}

int yywrap()
{
    return 1;
}
