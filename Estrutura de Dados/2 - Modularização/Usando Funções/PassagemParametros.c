#include <stdio.h> 

// Função que dobra o valor (passagem por valor) 

void dobrar_valor(int num) { 

    num = num * 2;  // Modifica apenas a cópia do valor 

    printf("Dentro da função (por valor), o valor dobrado é: %d\n", num); 

}
// Função que dobra o valor (passagem por referência) 

void dobrar_valor_ref(int *num) { 

    *num = *num * 2;  // Modifica o valor original usando o ponteiro 

    printf("Dentro da função (por referência), o valor dobrado é: %d\n", *num); 

}
int main() { 

    int numero = 10; 

 

    // Passagem por valor 

    printf("Antes da função (por valor), o número é: %d\n", numero); 

    dobrar_valor(numero); 

    printf("Depois da função (por valor), o número é: %d\n", numero); 

 

    // Passagem por referência 

    printf("\nAntes da função (por referência), o número é: %d\n", numero); 

    dobrar_valor_ref(&numero);  // Passamos o endereço da variável 

    printf("Depois da função (por referência), o número é: %d\n", numero); 

 

    return 0; 

}