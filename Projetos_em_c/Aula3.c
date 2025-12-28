#include <stdio.h>
int main () {
  int idade = 25;
  float altura = 1.75;
  char opcao = 'S';
  char nome[20] = "Sergio";

  printf("A idade de %s é %d\n", nome, idade);
  printf("A altura é: %.2f\n", altura);
  printf("A altura é :%c\n", opcao);
  /*
  printf("%formato1 %formato2 %formato3", varivavel1, variavel2, variave3)
  %d: Imprime um inteiro no formato decimal.
  %i: Equivalente a %d.
  %f: Imprime um número de ponto flutuante no formato padrão.
  %e: Imprime um número de ponto flutuante na notação científica.
  %c: Imprime um único caractere.
  %s: Imprime uma cadeia (string) de caracteres.
  %%: Imprime o caractere de porcentagem (%).
  */
}