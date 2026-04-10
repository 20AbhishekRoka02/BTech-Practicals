%{
#include<stdio.h>
#include<stdlib.h>

int yylex();
void yyerror(char *s);
%}

%token NUMBER

%left '+' '-'
%left '*' '/'

%%

input:
        exp '\n' { printf("Result = %d\n",$1); }
        ;

exp:
        NUMBER          { $$ = $1; }

      | exp '+' exp     { $$ = $1 + $3; }

      | exp '-' exp     { $$ = $1 - $3; }

      | exp '*' exp     { $$ = $1 * $3; }

      | exp '/' exp     { $$ = $1 / $3; }

      | '(' exp ')'     { $$ = $2; }
      ;

%%

void yyerror(char *s)
{
    printf("Invalid Expression\n");
}

int main()
{
    printf("Enter expression:\n");
    yyparse();
    return 0;
}
