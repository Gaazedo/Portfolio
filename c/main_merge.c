//autor: Gabriel Augusto Torres Azevedo - 32020309

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

void printfVet(int *V  , int N){
    int i;
    for(i = 0; i < N; i++)
        printf("%2d ",V[i]);
    printf("\n");
}

void merge(int *V, int inicio, int meio, int fim){
    int *temp, p1, p2, tamanho, i, j, k;
    int fim1 = 0, fim2 = 0;
    tamanho = fim-inicio+1;
    p1 = inicio;
    p2 = meio+1;
    temp = (int *) malloc(tamanho*sizeof(int));
    if(temp != NULL){
        for(i=0; i<tamanho; i++){
            if(!fim1 && !fim2){
                if(V[p1] < V[p2])
                    temp[i]=V[p1++];
                else
                    temp[i]=V[p2++];

                if(p1>meio) fim1=1;
                if(p2>fim) fim2=1;
            }else{
                if(!fim1)
                    temp[i]=V[p1++];
                else
                    temp[i]=V[p2++];
            }
        }
        for(j=0, k=inicio; j<tamanho; j++, k++)
            V[k]=temp[j];
    }
    free(temp);
}

void mergeSort(int *V, int inicio, int fim){
    int meio;
    if(inicio < fim){
        meio = floor((inicio+fim)/2);
        mergeSort(V,inicio,meio);
        mergeSort(V,meio+1,fim);
        merge(V,inicio,meio,fim);
    }
}

int main(){

    int p1 [4] = {1,4,2,3};
    int p2 [4] = {7,0,6,5};
    int N =sizeof(p1[4])+ sizeof(p2[4]);
    int temp [8] = {};

//MISTURA OS DOIS VETORES
memcpy( temp, p1, sizeof(p1) );

memcpy( temp + (sizeof(p1)/sizeof(int)), p2, sizeof(p2) );

//SORT DO VETOR GERAL MISTURADO 
mergeSort(temp, 0, N);
printfVet(temp, N);

    return 0;
}
