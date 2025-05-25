#include <stdio.h> 

// Variável global para o total de itens no estoque 

int totalEstoque = 100;

// Procedimento para adicionar itens ao estoque 

void adicionarEstoque(int quantidade) {  // 'quantidade' é um parâmetro formal 

    totalEstoque += quantidade; 

    printf("Itens adicionados: %d\n", quantidade); 

    printf("Estoque atualizado: %d\n", totalEstoque); 

}

// Procedimento para remover itens do estoque 

void removerEstoque(int quantidade) {  // 'quantidade' é um parâmetro formal 

    if (quantidade <= totalEstoque) { 

        totalEstoque -= quantidade; 

        printf("Itens removidos: %d\n", quantidade); 

        printf("Estoque atualizado: %d\n", totalEstoque); 

    } else { 

        printf("Erro: Quantidade insuficiente no estoque!\n"); 

    } 

}

// Função principal 

int main() { 

    // Variável local para armazenar a quantidade de itens a ser processada 

    int quantidade; 

 

    // Adicionar itens ao estoque 

    quantidade = 20;  // 'quantidade' é um argumento passado para a função 

    adicionarEstoque(quantidade); 

 

    // Remover itens do estoque 

    quantidade = 15;  // 'quantidade' é um argumento passado para a função 

    removerEstoque(quantidade); 

 

    // Tentar remover uma quantidade maior do que o estoque 

    quantidade = 200;  // 'quantidade' é um argumento passado para a função 

    removerEstoque(quantidade); 

 

    return 0; 

}

