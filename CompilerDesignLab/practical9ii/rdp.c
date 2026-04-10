#include<stdio.h>
#include<stdlib.h>

int yylex();

int token;   // declared only here

#define ID 1
#define PLUS 2
#define MUL 3
#define LP 4
#define RP 5


void match(int expected)
{
    if(token == expected)
        token = yylex();
    else
    {
        printf("Invalid String\n");
        exit(0);
    }
}

void E();
void E_dash();
void T();
void T_dash();
void F();


void E()
{
    T();
    E_dash();
}

void E_dash()
{
    if(token == PLUS)
    {
        match(PLUS);
        T();
        E_dash();
    }
}

void T()
{
    F();
    T_dash();
}

void T_dash()
{
    if(token == MUL)
    {
        match(MUL);
        F();
        T_dash();
    }
}

void F()
{
    if(token == ID)
        match(ID);

    else if(token == LP)
    {
        match(LP);
        E();
        match(RP);
    }

    else
    {
        printf("Invalid String\n");
        exit(0);
    }
}


int main()
{
    printf("Enter expression:\n");

    token = yylex();

    E();

    if(token == 0)
        printf("String Accepted\n");
    else
        printf("Invalid String\n");

    return 0;
}
