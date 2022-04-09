#include"header.h"
#include"chrono"
#include"thread"
#include"ProblemHeaders.h"

int main()
{
    /*
        SignalManager* itsSignalManager = SignalManager::get_instance();


    ComponentBuilder* itsComponentBuilder = new ComponentBuilder();

    itsComponentBuilder->build();
    itsComponentBuilder->connect();

    InputSingalComponent* itsInputSingal = (InputSingalComponent*)itsComponentBuilder->getComponent(INPUT_SIGNAL);

    while (true)
    {
        itsSignalManager->refreshSignals();
        std::cout << itsInputSingal->m_itsSwitch1 << itsInputSingal->m_itsSwitch2 << itsInputSingal->m_itsSwitch3 << itsInputSingal->m_itsSwitch4;
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }


    IceCreamMachineBuilder* builder = new IceCreamMachineBuilder;
    IceCreamMachineDirector* director = new IceCreamMachineDirector;
    director->setBuilder((IceCreamBuilderInterface*)builder);

    IceCream* chociIce = director->buildChociIceCream();
    IceCream* BerryIce = director->buildStrawBerryCream();
    IceCream* VanillaIce = director->buildVanillaIceCream();
    */


    gameOfLife({ {0,1,0,0,0,0,1,0,0,0,0,0,0},{0,0,1,1,0,0,0,1,0,0,0,0,0},{0,0,1,0,0,1,1,1,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0,0,0,0} });
}

/*

    symmetricDifference({ 1, 2, 3 }, { 5, 2, 1, 4 });

    inventoryUpdate({ {21, "Bowling Ball"},
                      {2, "Dirty Sock"},
                      {1, "Hair Pin"},
                      {5, "Microphone"} },

               {      {21, "Bowling Ball"},
                      {2, "Dirty Sock"},
                      {1, "Hair Pin"},
                      {5, "Microphone"} });

    slidingWindowCompare({ 1,2,2,3,4,5,6,6,6,7 }, 5);

    map<int, unsigned long long> data;
    cout << "fib 50: " << fibonacci(50, data) << endl;

    set<int, less<int>> data1 = { 6,1,4,2,8,3,10,5, 9 };
    set<int, greater<int>> data1 = { 6,1,4,2,8,3,10,5, 9 };

    set<int, grtr<int>> data1 = { 6,1,4,2,8,3,10,5, 9 };


    vector<int> data = { 1,4,20,70,200,202,500,602,700,702,704,1012,6012,7015 };
    binarySearch(data, 6012);
    binarySearch(data, 4);
    binarySearch(data, 99);

    LinkedList<string> name({ "alex", "maria", "albert","nicole" });

    cout << twoCitySchedCost({{10,20},{30,200},{400,50},{30,20} });

    allCellsDistOrder(2, 3, 1, 2);

    cout << maxSumTwoNoOverlap({ 0, 6, 5, 2, 2, 5, 1, 9, 4 }, 1, 2)<< "\n";
    cout << maxSumTwoNoOverlap({ 3,8,1,3,2,1,8,9,0 }, 3,2) << "\n";
    cout << maxSumTwoNoOverlap({ 2, 1, 5, 6, 0, 9, 5, 0, 3, 8 }, 4, 3) << "\n";
        
    Node<int> *res = addLists(LinkedList({ 8,2,4 }).getHead(), LinkedList({ 8,2,4 }).getHead());

    cout << eraseOverlapIntervals({ {1,2},{2,3},{3,4},{1,3} });

    cout << numRescueBoats({ 3,2,2,1 }, 3);

    splitOddEvenSort({ 15, 8, 2,6,3,5,7,9,10, 0 });

    findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT");

    rotateArray({ 1,2,3,4,5,6,7 }, 3);
    
    cout << reverseBits(43261596);

    cout << findMedianSortedArrays({ 1,2 }, {3, 4});

    cout << climbStairs(3);

    cout << isAnagram("anagram", "naagram");

    cout << isHappy(19);
    cout << isHappy(2);

    cout << lastStoneWeight({ 2,7,4,1,8,1 });

    reverseString({ 'a','b','c', 'd'});

    firstandLast({ 1,1,2,3,5,5,5,5,5,6,6,7,8 }, 5);

    cout << canCompleteCircuit({ 1, 2, 3, 4, 5 }, { 3, 4, 5, 1, 2 });

    gameOfLife({ {1, 1},{1, 0} });
*/
