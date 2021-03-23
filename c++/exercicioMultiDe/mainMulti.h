#include <iostream>
#include "tad_fila.h"
using namespace std;
Fila criaFila(int x){
  Fila fila(100);
  int elemento=0;
  while(elemento!=-1){
    cout<<"Digite o número para inserir na fila "<< x <<":";
    cin >>elemento;
    if(elemento!=-1) fila.inserir(elemento); 
  }
  return fila;
}

Fila multiplexFila(Fila fila1, Fila fila2, Fila fila3){
  Fila mult(300);
  while(!fila1.vazia() || !fila2.vazia()|| !fila3.vazia()){
    if(!fila1.vazia()) mult.inserir(fila1.extrair());
    if(!fila2.vazia())mult.inserir(fila2.extrair());
    if(!fila3.vazia())mult.inserir(fila3.extrair());
  }
  return mult;
}



int mainMultiplexador(){
  int cont =1;
  Fila filaUm = criaFila(cont);
  cont+=1;
  Fila filaDois=criaFila(cont);
  cont+=1;
  Fila filaTres=criaFila(cont);

  cout<< "Primeira fila: "<< filaUm.imprimir()<< "\n";
  cout << "Segunda fila: "<<filaDois.imprimir()<<"\n";
  cout<<"Terceira fila: "<<filaTres.imprimir()<<"\n";

  Fila filaMult = multiplexFila(filaUm, filaDois, filaTres);
  filaMult.imprimir();
  return 0;
  
}