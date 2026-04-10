%{
#include<stdio.h>

int keyword=0, identifier=0, number=0, operator=0, special_symbol=0;
%}

%%

int|float|char|if|else|while|for|return|do|break|continue { 
    printf("KEYWORD: %s\n", yytext); 
    keyword++; 
}

[0-9]+ { 
    printf("NUMBER: %s\n", yytext); 
    number++; 
}

[a-zA-Z_][a-zA-Z0-9_]* { 
    printf("IDENTIFIER: %s\n", yytext); 
    identifier++; 
}

[+\-*/=<>!] { 
    printf("OPERATOR: %s\n", yytext); 
    operator++; 
}

[(){};,] { 
    printf("SPECIAL SYMBOL: %s\n", yytext); 
    special_symbol++; 
}

[ \t\n]+   ;    

. { 
    printf("UNKNOWN: %s\n", yytext); 
}

%%

int main()
{
    printf("Enter the program:\n");
    yylex();

    printf("\nSummary:\n");
    printf("Keywords = %d\n", keyword);
    printf("Identifiers = %d\n", identifier);
    printf("Numbers = %d\n", number);
    printf("Operators = %d\n", operator);
    printf("Special Symbols = %d\n", special_symbol);

    return 0;
}

int yywrap()
{
    return 1;
}
