%{
#include<stdio.h>
#include<stdlib.h>

int yylex();
void yyerror(char *s);
%}

%token NUM

%left '+'
%left '*'

%%

E : E '+' T   { printf("Reduce E->E+T\n"); }
  | T         { printf("Reduce E->T\n"); }
  ;

T : T '*' F   { printf("Reduce T->T*F\n"); }
  | F         { printf("Reduce T->F\n"); }
  ;

F : '(' E ')' { printf("Reduce F->(E)\n"); }
  | NUM       { printf("Reduce F->NUM\n"); }
  ;

%%

void yyerror(char *s)
{
    printf("Invalid Expression\n");
}

int main()
{
    printf("Enter Expression:\n");
    yyparse();
    printf("Valid Expression\n");
    return 0;
}
