#include <stdio.h>

int main(){
    int idade;
    float altura;
    char nome[20];

    printf("Digite a sua idade: ");
    scanf("%d", &idade);
    printf("A idade é: %d", idade);

    printf("Digite a sua altura: ");
    scanf("%f", &altura);
    printf("A altura é: %f", altura);

    printf("Digite o seu nome: ");
    scanf("%s", &nome);
    printf("O nome é: %s", nome);

    return 0;
}