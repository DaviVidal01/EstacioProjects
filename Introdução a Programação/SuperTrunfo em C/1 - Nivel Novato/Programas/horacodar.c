/*Um programa em C para cadastrar os dados dos alunos.*/

#include <stdio.h>

int main(int argc, char const *argv[])
{
    int idade, matricula;
    float altura;
    char nome[50];

    printf("Digite sua idade: \n");
    scanf("%d",&idade);

    printf("Digite sua altura: \n");
    scanf("%f",&altura);

    printf("Digite seu nome: \n");
    scanf("%s",&nome);

    printf("Digite sua matricula: \n");
    scanf("%d",&matricula);

    printf("Nome do Aluno: %s - Matricula: %d\n", nome, matricula);
    printf("Idade: %d - Altura: %f\n", idade, altura);

    return 0;
}
