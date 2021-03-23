#include <iostream>
#include "tad_fila.h"
using namespace std;

Fila recebeFila(){
  Fila fila(300);
  int elemento=0;
  while(elemento!=-1){
    cout<<"Digite o número para inserir na fila: ";
    cin >>elemento;
    if(elemento!=-1) fila.inserir(elemento); 
  }
  return fila;
}
int imprimeFilas(Fila fil1,Fila fil2, Fila fil3){
  cout << "Primeira fila: " << fil1.imprimir();
  cout << "\nSegunda fila: " << fil2.imprimir();
  cout << "\nTerceira fila: " << fil3.imprimir();
  return -1;
}


Fila desmultiplexFila(Fila fila){
  Fila filaUm(100);
  Fila filaDois(100);
  Fila filaTres(100);
  while(!fila.vazia()){
    int x = fila.extrair();
    filaUm.inserir(x);
    int y = fila.extrair();
    filaDois.inserir(y);
    int z = fila.extrair();
    filaTres.inserir(z);

}
  imprimeFilas(filaUm,filaDois, filaTres);
  return -1;
}



int mainDesmultiplexador(){
  Fila fila = recebeFila();
  cout<< "Fila: "<< fila.imprimir()<< "\n";
  

  Fila filaFinal = desmultiplexFila(fila);
  filaFinal.imprimir();
  return -1;
  
}