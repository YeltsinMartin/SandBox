#include"Header.h"
#include <iostream>
#include <chrono>
#include <thread>

using namespace std::chrono_literals;

int main()
{
    SingalManger* itsSingalManager = SingalManger::getInstance();
    MainComponetDirector* lmain = MainComponetDirector::getInstance();
    lmain->build();
    lmain->connect();

    while (1)
    {
        this_thread::sleep_for( 100ms );
        itsSingalManager->refreshSingals();
    }

}