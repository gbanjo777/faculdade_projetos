#include <stdio.h>
int main (){
  int idade;
  float altura;
  char nome[30];
  //sintaxe scanf
  // scanf("formato1", "formato2", &variavel1, &variavel2...);
  printf("Digite a sua idade: ");
  scanf("%d", &idade);
  printf("A sua idade é: %d\n", idade);
  printf("Digite a sua altura: ");
  scanf("%f", &altura);
  printf("A Altura é: %f\n", altura); //não precisa do & para strings
  print("Digite seu nome: ");
  scanf("%s", nome);
  print("O nome é: %s\n", nome);
}
//char letra;
//char nome[50];

//scanf("%c", &letra);
//scanf("%s", nome);