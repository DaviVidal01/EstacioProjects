#include <stdio.h>

// Protótipos das funções
float calcular_area_circulo(float raio);
int calcular_area_retangulo(int largura, int altura);

int main(int argc, char const *argv[])
{
    float raio = 5.0;
    int largura = 4;
    int altura = 6;

    // CHamando as funções antes de suas definições completas
    printf("Area de circulo: %.2f\n", calcular_area_circulo(raio));
    printf("Area do retangulo: %d\n", calcular_area_retangulo(largura, altura));

    return 0;
}

// Definição da função para calcular a área de um circulo
float calcular_area_circulo(float raio){
    return 3.14159 * raio * raio; // Fórumula da área de circulo
}

// Definição da função para calcular a área de um retangulo
int calcular_area_retangulo(int largura, int altura){
    return largura * altura; // Fórmula da área de retangulo
}
