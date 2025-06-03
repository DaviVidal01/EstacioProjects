/*Neste primeiro nível, seu objetivo é construir a base do 
nosso jogo Super Trunfo de Países: um sistema para cadastrar 
as cartas com informações sobre as cidades. Você vai praticar 
a leitura de dados do usuário, o armazenamento em variáveis e 
a exibição dessas informações na tela.*/

// Inclusão das Bibliotecas
#include <stdio.h>
#include <string.h> //Tive que adicionar a biblioteca string para ações com Strings

// Iniciando Função Main.
int main()
{
    /*Criar um programa em C que permita ao usuário inserir os
    dados de duas cartas do Super Trunfo. Para cada carta, o
    usuário deverá fornecer as seguintes informações:*/

    // ---> Definindo Variáveis
    // Carta 1
    char estado;
    char codigo_carta[4];
    char nome_cidade[50];
    int populacao;
    float area;
    float pib;
    int numero_pontos_turisticos;

    // Carta 2
    char estado2;
    char codigo_carta2[4];
    char nome_cidade2[50];
    int populacao2;
    float area2;
    float pib2;
    int numero_pontos_turisticos2;

    // ---> Leitura e Entrada dos Dados
    // Carta 1
    printf("---[Cadastrando | Carta 1]\n");
    printf("Digite o Estado (Letra 'A' a 'H'):\n");
    scanf(" %c",&estado); 
    printf("Codigo da Carta (ex: A01, B03):\n");
    scanf(" %3s", &codigo_carta);
    printf("Nome da Cidade:\n");
    getchar(); //Limpa o \n do buffer antes de fgets
    fgets(nome_cidade, sizeof(nome_cidade), stdin); //Cadastra o nome da cidade
    nome_cidade[strcspn(nome_cidade, "\n")] = '\0'; // remove \n do final
    printf("O numero de Habitantes:\n");
    scanf("%d", &populacao);
    printf("A area da cidade em Quilometros Quadrados:\n");
    scanf("%f",&area);
    printf("O Produto Interno Bruto da cidade:\n");
    scanf("%f",&pib);
    printf("A quantidade de Pontos Turisticos na cidade:\n");
    scanf("%d", &numero_pontos_turisticos);

    // Carta 2
    printf("---[Cadastrando | Carta 2]\n");
    printf("Digite o Estado (Letra 'A' a 'H'):\n");
    scanf(" %c",&estado2);
    printf("Codigo da Carta (ex: A01, B03):\n");
    scanf(" %3s", &codigo_carta2);
    printf("Nome da Cidade:\n");
    getchar(); //Limpa o \n do buffer antes de fgets
    fgets(nome_cidade2, sizeof(nome_cidade2), stdin); //Cadastra o nome da cidade
    nome_cidade2[strcspn(nome_cidade2, "\n")] = '\0'; // remove \n do final
    printf("O numero de Habitantes:\n");
    scanf("%d", &populacao2);
    printf("A area da cidade em Quilometros Quadrados:\n");
    scanf("%f",&area2);
    printf("O Produto Interno Bruto da cidade:\n");
    scanf("%f",&pib2);
    printf("A quantidade de Pontos Turisticos na cidade:\n");
    scanf("%d", &numero_pontos_turisticos2);

    /*Após o usuário inserir os dados de cada carta, seu 
    programa deve exibir na tela as informações cadastradas, 
    de forma organizada e legível. Para cada carta, imprima cada 
    informação em uma linha separada, com uma descrição clara.*/

    // Carta 1
    printf("---[Apresentando | Carta 1]\n");
    printf("Estado: %c\n",estado);
    printf("Codigo: %s\n",codigo_carta);
    printf("Nome da Cidade: %s\n",nome_cidade);
    printf("Populacao: %d\n",populacao);
    printf("Area: %.2f km²\n",area);
    printf("PIB: R$%.2f\n",pib);
    printf("Numero de Pontos Turisticos: %d\n", numero_pontos_turisticos);

    //Carta 2
    printf("---[Apresentando | Carta 2]\n");
    printf("Estado: %c\n",estado2);
    printf("Codigo: %s\n",codigo_carta2);
    printf("Nome da Cidade: %s\n",nome_cidade2);
    printf("Populacao: %d\n",populacao2);
    printf("Area: %.2f km²\n",area2);
    printf("PIB: R$%.2f\n",pib2);
    printf("Numero de Pontos Turisticos: %d\n", numero_pontos_turisticos2);

    // Finalizador do Sistema
    return 0;
}
