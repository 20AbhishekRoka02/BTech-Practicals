%{
#include<stdio.h>
%}

%%

"++"|"--"                 { printf("Increment/Decrement Operator: %s\n", yytext); }

"=="|"!="|"<="|">="       { printf("Relational Operator: %s\n", yytext); }

"&&"|"||"|"!"             { printf("Logical Operator: %s\n", yytext); }

"+"|"-"|"*"|"/"|"%"       { printf("Arithmetic Operator: %s\n", yytext); }

"="                       { printf("Assignment Operator: %s\n", yytext); }

"<"|">"                   { printf("Relational Operator: %s\n", yytext); }

[ \t\n]                   ;

.                         { printf("Invalid Operator: %s\n", yytext); }

%%

int main()
{
    printf("Enter expression:\n");
    yylex();
    return 0;
}

int yywrap()
{
    return 1;
}
