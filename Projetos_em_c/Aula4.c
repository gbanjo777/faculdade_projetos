# include <stdio.h>
int mains (){
  int idade, matricula;
  float altura;
  char nome[50];
  printf("Digite sua idade: \n");
  scanf("%d", &idade);
  printf("Digite sua matricula: ");
  scanf("%d", &matricula);
  printf("Digite sua altura: ");
  scanf("%f", &altura);
  printf("Digite seu nome: ");
  scanf("%s", nome);
}