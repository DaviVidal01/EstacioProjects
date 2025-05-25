#include <stdio.h>

int main()
{
    FILE *arquivo; //Ponteiro para o arquivo
    char nome[50];
    int idade;

    // Abrindo o arquivo no modo "w" para escrita
    arquivo = fopen("dados.txt","w");
    if (arquivo == NULL){
        printf("Erro ao abrir o arquivo!\n");
        return 1;
    }

    // Coletando dados do usuário
    printf("Digite seu nome: ");
    scanf("%s", nome);
    printf("Digite a idade: ");
    scanf("%d", &idade);

    // Gravando os dados no arquivo
    fprintf(arquivo, "Nome: %s\nIdade: %d\n", nome, idade);

    // Fechando o arquivo
    fclose(arquivo);

    // Reabrindo o arquivo no modo "r" para leitura
    arquivo = fopen("dados.txt", "r");
    if (arquivo == NULL){
        printf("Erro ao abrir o arquivo!\n");
        return 1;
    }

    // Lendo os dados do arquivo
    fscanf(arquivo, "Nome: %s\nIdade: %d\n", nome, &idade);

    // Exibindo os dados lidos
    printf("Dados lidos do arquivo:\n");
    printf("Nome: %s\nIdade: %d\n", nome, idade);
    
    // Fechando o arquivo
    fclose(arquivo);
    
    return 0;
}
