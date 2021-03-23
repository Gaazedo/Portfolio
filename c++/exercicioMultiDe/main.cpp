
//Ana Cecília Barbosa Alves e Gabriel Augusto Torres Azevedo 
// TIA 32084935 e 32020309

#include <iostream>
#include "tad_fila.h"
#include "mainDesmul.h"
#include "mainMulti.h"
using namespace std;


int main(){
  int opcao;
  cout << "Escolha:\n 1 - multiplexador \n 2 - desmultiplexador "<< endl;
  cout<<"Sua escolha é ";
  cin >> opcao;
  if(opcao ==1){
    mainMultiplexador();
  }else if(opcao ==2){
    mainDesmultiplexador();
  }
}