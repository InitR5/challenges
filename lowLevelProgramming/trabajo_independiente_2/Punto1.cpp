/*
	Name: Trabajo independiente #2 Punto 1
	Author: Edward Mauricio Suarez
	Date: 22/03/2021
	Description: 
*/
#include <stdio.h>
#include <wchar.h>
#include <locale.h>
#include <stdlib.h>
#include <math.h>
main(void)
{
	setlocale(LC_ALL, "");
	int num1, num2, num3;
	double resultado;
	
	printf("Digite tres números: \n");
	scanf("%d %d %d", &num1, &num2, &num3);
	
	resultado=sqrt(((pow(num1, 2)+num2)/3)-num3*(1/4)+2);
	
	printf("El resultado es: %f", resultado);
}

