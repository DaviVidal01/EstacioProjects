#include <stdio.h>

int main()
{

    char Torre[20], Bispo[20], Rainha[20];
    int i = 0;

    // Torre 5 casas a Direita
    for (i = 0; i <= 5; i++)
    {
        printf("Torre movimenta a Direita");
    }
    i = 0;

    // Bispo 5 casas a Cima/Direita
    do
    {
        printf("Bispo movimenta a Cima/Direita");
        i++;
    } while (i <= 5);
    i = 0;

    // Rainha 8 casas a esquerda
    while (i <= 8)
    {
        printf("Rainha movimenta a esquerda");
        i++;
    }

    return 0;
}