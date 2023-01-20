#include <iostream>
//#include <String>

using namespace std;

template <class T>
T sum (T a, T b)
{
	T result;
	result = a + b;
	return result;
}

struct human {
		int height, weight;
		string name;
		char gender;
	};
	

int main (){
	
	human Donald;
	
	human *p;
	p = &Donald;
	
	Donald.height = 175;
	Donald.weight = 150;
	Donald.name = "Jorden Blue";
	Donald.gender = 'M';
	
	cout<<Donald.name<<endl;
	cout<< p->name<<endl;
	p->name = "Hi";
	cout<< p->name<<endl;
	
	/*
	int a = 1, b = 2, x;
	double c = 3.0, d = 4.0, y;
	
	/*
	cout<<"Please enter first number"<<endl;
	cin<<a;
	cout<<"Please enter second number"<<endl;
	cin<<b;
	
	
	x = sum<int>(a, b);
	y = sum<double>(c, d);
	cout<<x<<endl;
	cout<<y<<endl;
	*/
	
}
