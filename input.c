%option noinput nounput noyywrap

%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_IDENT_LENGTH 50
#define MAX_SYMBOL_TABLE_SIZE 100

struct Symbol {
    char name[MAX_IDENT_LENGTH];
    int line;
};

struct Symbol symbolTable[MAX_SYMBOL_TABLE_SIZE];
int symbolCount = 0;

void addToSymbolTable(const char* name, int line) {
    if (symbolCount < MAX_SYMBOL_TABLE_SIZE) {
        strcpy(symbolTable[symbolCount].name, name);
        symbolTable[symbolCount].line = line;
        symbolCount++;
    }
}

void printSymbolTable() {
    printf("Symbol Table:\n");
    printf("------------------\n");
    printf("Name\t|\tLine\n");
    printf("------------------\n");
    for (int i = 0; i < symbolCount; i++) {
        printf("%s\t|\t%d\n", symbolTable[i].name, symbolTable[i].line);
    }
    printf("------------------\n");
}

%}

%%
[a-zA-Z_][a-zA-Z0-9_]*   {
                            addToSymbolTable(yytext, yylineno);
                            printf("Identifier: %s\n", yytext);
                        }

.                       ;

\n                      ;

%%

int main(int argc, char* argv[]) {
    if (argc < 2) {
        printf("Please provide a C file as input.\n");
        return 1;
    }

    FILE* inputFile = fopen(argv[1], "r");
    if (!inputFile) {
        printf("Failed to open input file.\n");
        return 1;
    }

    yyin = inputFile;
    yylex();

    fclose(inputFile);

    printSymbolTable();

    return 0;
}

