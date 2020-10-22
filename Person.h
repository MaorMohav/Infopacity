#ifndef PERSON_H
#define PERSON_H

#include<iostream>
#include<string.h>

using namespace std;

class Person
{
protected:
	string name;
	long id;
	int age;

public:

	Person(const string name = "?" , const long id = 0 , const int age = 0):name(name) , id(id) , age(age){}
	Person(const Person& Other)
	{
		name = Other.name;
		id = Other.id;
		age = Other.age;
	}
	virtual void Print()const
	{
		cout << "Name: " << name << endl << "id: " << id << endl << "age: " << age << endl;
	}
	void Print2()
	{
		cout << "hello" << endl;
	}
	virtual ~Person() = 0;


};
#endif
