#include<iostream>

using namespace std;

unsigned long fibonacci(int n){
    if(n==0) return 0;
    if(n<=2) return 1;
    return fibonacci(n-1) + fibonacci(n-2);
}

int main()
{
    cout <<"Parise the Lord\n";
    cout << "Fibonacci 10: "<<fibonacci(10)<<endl;
    cout << "Fibonacci 6: "<<fibonacci(6)<<endl;
    cout << "Fibonacci 5: "<<fibonacci(5)<<endl;
    return 0;
}
