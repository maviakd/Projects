#include <iostream>
#include <string>

using namespace std;
#include "vehicle.h"

int main (){
	
	vehicle x;
	
	int myear, mileage;
	string owner, thetype, themodel;
	
	cout<<"please enter year ";
	cin>>myear;
	
	x.setyear(myear);
    x.displayyear();
   
}
