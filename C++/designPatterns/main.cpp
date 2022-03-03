#include"Singleton.h"
#include<iostream>

int main()
{

    Singleton* ptr = Singleton::getInstance();

    ptr->printCount();
    ptr->printCount();

}