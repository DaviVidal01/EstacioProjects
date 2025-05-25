#include <stdio.h>
#include <ctype.h>

int main()
{
    char texto[] = "Programacao123";
    int i = 0;

    // Percorrendo cada caractere da string
    while (texto[i]){
        // Verificando se é uma letra
        if (isalpha(texto[i])){
            printf("%c - uma letra.\n", texto[i]);

            // Transformando em maiúsculo se for minúsculo
            if (islower(texto[i])){
                texto[i] = toupper(texto[i]);
                printf("Convertido para maiusculo: %c\n", texto[i]);
            }
            // Verificando se é um número
            else if (isdigit(texto[i])){
                printf("%c - um numero.\n", texto[i]);
            }
            i++;
        }
    }

    printf("Texto transformado: %s\n", texto);

    return 0;
}
