#include <iostream>
#include <string>

class vehicle{
	
	public:
		void setyear(int i);
		void displayyear();
		void settype(string type);
		void setmileage(int mile);
		void setmodel(string model);
		void setowner(string owner);
		void displayowner();

	private:
		string ownername;
		string thetype;
		int year;
		int mileage;
		string model;

};

	
#include "vehicle.cpp" 
