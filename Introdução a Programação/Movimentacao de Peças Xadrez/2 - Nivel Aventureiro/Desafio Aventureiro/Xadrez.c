#include <stdio.h>

int main()
{
    int i = 0;
    int salto;
    int passo = 0;

    // Torre 5 casas a Direita
    for (i = 0; i < 5; i++)
    {
        printf("Torre movimenta a Direita\n");
    }
    i = 0;

    // Bispo 5 casas a Cima/Direita
    do
    {
        printf("Bispo movimenta a Cima/Direita\n");
        i++;
    } while (i < 5);
    i = 0;

    // Rainha 8 casas a esquerda
    while (i < 8)
    {
        printf("Rainha movimenta a esquerda\n");
        i++;
    }

    // Quantos saltos do cavalo.
    for (salto = 0; salto < 1; salto++)
    {

        // 2 passos para baixo
        while (passo < 2)
        {
            printf("Cavalo movimenta para Baixo\n");
            passo++;
        }

        // 1 passo para esquerda
        printf("Cavalo movimenta para Esquerda\n");
    }

    return 0;
}