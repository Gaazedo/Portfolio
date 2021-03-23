#include <sstream> //transforma numeros em string
#include "tad_fila.h"
#include <iostream>
using namespace std;

Fila::~Fila() {}

Fila::Fila() {}

Fila::Fila(int max) {
	this->fila = new int(max); 
	this->tamanhoMax = max;
	this->tamanho = 0;
	this->ini = -1;
	this->fim = -1;
}

bool Fila::vazia() {
	return this->tamanho == 0;
}

bool Fila::cheia() {
	return this->tamanho == this->tamanhoMax;
}

int Fila::inserir(int valor) {
	if (cheia()) {
		return -1;
	}
	fim = (fim + 1) % tamanhoMax; 
	if (ini == -1) {
		ini = 0;
	}
	this->fila[fim] = valor;
	this->tamanho++;
	int posicao = this->tamanho;
	return this->tamanho;
}

int Fila::extrair() {
  if(vazia()){
    this->ini =-1;
    this-> fim = -1;
    return -1;
  }
  int elemento=this->fila[ini];
  this->ini = (this->ini+1)%this->tamanhoMax;
  this->tamanho--;
  return elemento;
}
string Fila::imprimir() {

	stringstream ss;
	ss << "[ ";
	if (!this->vazia()) {
		for (int i = ini; i < this->tamanhoMax; i++) {
			ss << this->fila[i] << " ";
			if (i == fim) {
				break;
			}
		}
		if (fim < ini) {
			for (int i = 0; i <= fim; i++) {
				ss << this->fila[i] << " ";
			}
		}
	}
	ss << "]";
	return ss.str(); 
}
