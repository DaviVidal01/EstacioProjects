#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int numeroJogador, numeroComputador, resultado;
    char tipoComparacao;

    // Gerar número aleatório
    srand(time(0));
    numeroComputador = rand() % 100 + 1; // Número entre 1 e 100

    // Início do jogo
    printf("Bem-vindo ao jogo Maior, Menor ou Igual!\n");
    printf("Você deve escolher um número e o tipo de comparação.\n");
    print("M. Maior\n");
    print("N. Menor\n");
    print("I. Igual\n");

    printf("Escolha a comparação: ");
    scanf("%c", &tipoComparacao);

    // Exibir número do computador
    printf("O número do computador é: %d\n", numeroComputador);

    // Comparando números
    switch (tipoComparacao)
    {
    case 'M':
    case 'm':
        printf("Você escolheu a opção maior!\n");
        resultado = numeroJogador > numeroComputador ? 1 : 0;
        break;
    case 'N':
    case 'n':
        printf("Você escolheu a opção menor!\n");
        resultado = numeroJogador < numeroComputador ? 1 : 0;
        break;
    case 'I':
    case 'i':
        printf("Você escolheu a opção igual!\n");
        resultado = numeroJogador == numeroComputador ? 1 : 0;
        break;
    default:
        printf("Opção Invalida");
        break;
    }

    // Resultado
    printf("O número do computador é: %d e o do Jogador é: %d\n", numeroComputador, numeroJogador);
    if (resultado == 1)
    {
        printf("Você venceu!\n");
    }
    else
    {
        printf("Você perdeu!\n");
    }
    return 0;
}