//biblioteca basica do c++
#include <iostream>

//namespace para nao usar std::
using namespace std;

//o main() � o primeiro a rodar no c�digo 
int main() {
  //determina o tamanho do vetor
  int c[12];
  int i;
  //loop para popular o vetor
  for(i=0;i<12;i++)
  	c[i] = i;
  //loop para dar saida dos valores	
  for(i=0;i<12;i++)
  	cout << c[i] << " ";
  	
  return 0;

}
