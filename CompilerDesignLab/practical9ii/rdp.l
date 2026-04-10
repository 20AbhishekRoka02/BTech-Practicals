%{
#include<stdio.h>

#define ID 1
#define PLUS 2
#define MUL 3
#define LP 4
#define RP 5

extern int token;
%}

%%

"id"      { return ID; }

"+"       { return PLUS; }

"*"       { return MUL; }

"("       { return LP; }

")"       { return RP; }

[ \t\n]   ;

.         { return yytext[0]; }

%%

int yywrap()
{
return 1;
}
