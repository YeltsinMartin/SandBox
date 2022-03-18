#pragma once
#include<iostream>
#include<vector>

using namespace std;

class Updtatable {

public:
    virtual void update() = 0;

    Updtatable();
};

class SingalManger
{
    vector<Updtatable*> myList;

    SingalManger() {};

    SingalManger( const SingalManger& other ) = delete;

public:

    void refreshSingals() {
        for (Updtatable* item : myList) item->update();
    }

    static SingalManger* getInstance() {
        static SingalManger g_Instance;
        return &g_Instance;
    }

    void registerSignal( Updtatable* ptr )
    {
        myList.push_back( ptr );
    };
};

Updtatable::Updtatable() {
    SingalManger::getInstance()->registerSignal( this );
}


class Boolean: protected Updtatable {

public:
    bool value, valid;
    Boolean( bool pval = false, bool pvalid = false ) :value( pval ), valid( pvalid )
    {

    }
protected:
    void update() override {
        //logic how it gets the singal from newtowrk
        value = rand() % 200 > 60 ? true : false;
        valid = rand() % 200 > 60 ? true : false;
    }
};

class Float : protected Updtatable
{

public:
    float value;
    bool valid;
    Float( float pval = false, bool pvalid = false ):value(pval), valid( pvalid )
    {

    }
protected:
    void update() override {
        //logic how it gets the singal from newtowrk
        value = rand() % 200;
        valid = rand() % 200 > 60 ? true : false;
    }
};

enum ComponetID{ MAIN, INPUT, CLAW, OUTPUT,NONE };

class Componet
{
public:
    ComponetID  myID = NONE;
    virtual void build() = 0;

    virtual void connect() = 0;

};


class CruiseController : protected Updtatable
{
    void update() override {
        if (cruiseSwitch->valid && cruiseSwitch->value)
        {
            pedalPosition->value -= (currentSpeed->value - targetSpeed->value) * propotionalGain;
            cout << "Target Position : " << pedalPosition->value << endl;
        }
    }

protected:

    float propotionalGain;

public:
    Boolean* cruiseSwitch;
    Float*   targetSpeed;
    Float*   currentSpeed;
    Float*   pedalPosition;


    CruiseController( float pPropotionalGain ) : propotionalGain( pPropotionalGain ) {
        cruiseSwitch = nullptr;
        targetSpeed = nullptr;
        currentSpeed = nullptr;
        pedalPosition = nullptr;
    }



};

class MainComponetDirector : protected Componet
{
    vector<Componet*> myComponets;

    MainComponetDirector();

public:
    static MainComponetDirector* getInstance() {
        static MainComponetDirector instance;
        return &instance;
    }

    Componet* getComponent(ComponetID pID) {
        for (Componet* i : myComponets) {
            if (i->myID == pID) return i;
        }
    }

    void build() override {
        for (auto i : myComponets) i->build();
    }

    void connect() override {
        for (auto i : myComponets) i->connect();
    }

};

class InputSingalComponetBuilder : protected Componet
{

    void build() override {
        cruiseSwitch = new Boolean;
        targetSpeed = new Float;
        currentSpeed = new Float;
        pedalPosition = new Float;
    }

    void connect() override {

    }
public:
    Boolean* cruiseSwitch;
    Float* targetSpeed;
    Float* currentSpeed;
    Float* pedalPosition;

    InputSingalComponetBuilder() {
        myID = INPUT;
    }
};

class ControlLawBuilder :protected Componet {

    void build() override {
        m_CruiseController = new CruiseController( 0.2f );
    }

    void connect() override {
        InputSingalComponetBuilder* lIputPtr = (InputSingalComponetBuilder * )MainComponetDirector::getInstance()->getComponent(INPUT);
        m_CruiseController->cruiseSwitch = lIputPtr->cruiseSwitch;
        m_CruiseController->targetSpeed = lIputPtr->targetSpeed;
        m_CruiseController->currentSpeed = lIputPtr->currentSpeed;
        m_CruiseController->pedalPosition = lIputPtr->pedalPosition;
    }

public:

    CruiseController* m_CruiseController;

    ControlLawBuilder() {
        myID = CLAW;
    }
};

MainComponetDirector::MainComponetDirector()
{
    myComponets.push_back( (Componet*) new InputSingalComponetBuilder );
    myComponets.push_back( (Componet*) new ControlLawBuilder );
    myID = MAIN;
}
