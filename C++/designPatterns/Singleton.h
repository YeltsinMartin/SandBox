#include<iostream>

class Singleton
{

    mutable int m_printCounter = 0;

    Singleton()
    {
        std::cout << "Singleton Class Created\n";
    }

    Singleton(const Singleton& other) = delete;

public:

    static Singleton* getInstance()
    {
        static Singleton mInstance;
        return &mInstance;
    }

    void printCount() const{
        m_printCounter++;
        std::cout << m_printCounter <<" Singleton \n";
    }

};
