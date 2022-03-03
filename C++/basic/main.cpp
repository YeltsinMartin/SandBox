#include<iostream>
#include<string>
#include<vector>

using namespace std;

unsigned long fibonacci(int n){
    
    if(n<=2) 
    {
        if(n<=0) return 0;
        return 1;
    }
    return fibonacci(n-1) + fibonacci(n-2);
}

int main()
{
    cout <<"Parise the Lord\n";

    cout << "Fibonacci 10: "<<fibonacci(10)<<endl;

    vector<string> name = {"Yeltsin","Martin", "Babu", "Welcomes", "You"} ;

    for (auto &i:name)  cout << i <<" ";

    return 0;
}
