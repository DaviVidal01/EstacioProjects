#include <stdio.h>

void moverTorreCima(int casas)
{
    if (casas <= 0)
        return;
    printf("Cima\n");
    moverTorreCima(casas - 1);
}

void moverBispoDiagonal(int vertical, int horizontal)
{
    if (vertical <= 0 || horizontal <= 0)
        return;

    for (int i = 0; i < vertical; i++)
    {
        for (int j = 0; j < horizontal; j++)
        {
            printf("Cima\n");
            printf("Direita\n");
        }
    }

    moverBispoDiagonal(vertical - 1, horizontal - 1);
}

void moverRainha(int casas)
{
    moverTorreCima(casas);
    moverBispoDiagonal(casas, casas);
}

void moverCavalo()
{
    int movimentosFeitos = 0;

    for (int i = 0; i < 3; i++)
    {
        if (i == 2)
            break; // para fazer apenas 2 movimentos para cima

        printf("Cima\n");
        movimentosFeitos++;
    }

    int j = 0;
    while (j < 2)
    {
        j++;

        if (j != 1)
            continue; // pula a primeira iteração

        printf("Direita\n");
        movimentosFeitos++;
    }

    // Verificação final
    if (movimentosFeitos == 3)
        printf("Movimento do Cavalo concluído.\n");
}

int main()
{
    int casas = 3; // Pode ser ajustado

    printf("Movimento da Torre:\n");
    moverTorreCima(casas);
    printf("\n");

    printf("Movimento do Bispo:\n");
    moverBispoDiagonal(casas, casas);
    printf("\n");

    printf("Movimento da Rainha:\n");
    moverRainha(casas);
    printf("\n");

    printf("Movimento do Cavalo:\n");
    moverCavalo();
    printf("\n");

    return 0;
}