#include <iostream>
#include <cmath>

using namespace std;

int main ()
{
	//DATA TYPES
	char grade = 'A';
	string name ="John Guy";
	string substring;	
	int age = 65;
	double gpa = 5.6;
	bool isMale = true;
	
	//find index off string
	cout << name.find("Guy",0)  << endl;
	
	//take off some part of string
	cout << name.substr(5,3)  << endl;
	
	//store substring in another string
	substring = name.substr(0, 4);
	cout << substring <<endl;
	cout << " " <<endl;
	
		
	//OUTPUT STRINGS
	cout << "There once was a man Called " << name << endl;
	cout << "He was " <<age <<" years old" << endl;
	cout << "He liked the name " << name << endl;
	cout << "But did not like being " << age << endl;
	
	
	
	//Number Types 
	int Wnum = 5;
	double Dnum = 5.5;
	
	//basic operators for Numbers
	cout << 5 + 7;
	cout << 7 - 5;
	cout << 7 * 5;
	cout << 7 / 5;
	
	//Working with Var of Numbers
	
	Wnum ++;
	Wnum += 80;
	Wnum --;
	Wnum *= 3;

	//Math Functions 
	cout << pow(2,5); //elevado
	cout << sqrt(36); //raiz
	cout << round(4.3); //arredondar 
	cout << ceil(4.1); //arredondar pra cima
	cout << floor(4.1); // arredondar pra baixo
	cout << fmax(3,10); //mostra o maior entre eles
	cout << fmin (3,10); //mostra o menor entre eles
 	
	//USER INPUTS 
	
	int age1;
	cout << "Input your age: ";
	cin >> age1;	
	
	cout << "Your are " << age1 << "years old";
	
	
	//for string
	
	string name1;
	cout << "Enter your name";
	getline(cin,name1);
	cout << "hello" << name1;
	


	//BASIC CALCULATOR 
	
	double num1;
	double num2;
	
	cout << "Hello, Im a Online Calculator and i'm here to help you to sum" <<endl;
	cout << "Input the 1º number you want to sum " << endl;
	cin >> num1;	
	cout << "Input the 2º number you want to sum " << endl;
	cin >> num2;
	
	cout <<"The sum of the numbers it's: " << num1 + num2 ;
		
	
	return 0;
}


