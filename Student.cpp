#include "Student.h"

Student::Student(string sname,long sid,int sage,int saverage,string sinstitute):Person(sname,sid,sage),average(saverage),institute(sinstitute){}

Student::~Student(){}

void Student::print() {
	Person::print();
	cout << "the average is: " << average << endl;
	cout << "the name of the institute is: " << institute << endl;
}