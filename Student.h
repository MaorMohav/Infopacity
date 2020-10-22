#pragma once
#include "Person.h"
#include <iostream>
#include <string>
using namespace std;

class Student :public Person {
	int average;
	string institute;
public:
	Student(string = "unknown", long = 0, int = 0, int = 0, string = "unknown");
	~Student();
	void print();
};