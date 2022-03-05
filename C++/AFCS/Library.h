#include <iostream>
#include <vector>
#include <random>
using namespace std;

class Updatable{
public:

    Updatable(){}

    virtual void update() = 0;
};


class SignalManager{
    vector<Updatable* > m_SignalList;
    
    SignalManager(){
    }
public:
    void refreshSignals() const {
        for (Updatable* i : m_SignalList) i->update();
    }

    void registerSignals(Updatable* p_Signal){
        m_SignalList.push_back(p_Signal);
    }

    static SignalManager* get_instance()
    {
        static SignalManager g_Instance;
        return &g_Instance;
    }

};


class Boolean: public Updatable
{

    bool m_Value, m_Validity;

public:
    Boolean(){
        SignalManager::get_instance()->registerSignals(this);
    }

    void update() override{
        m_Value = rand() %255 > 125 ? true: false;
        m_Validity = rand() %255 > 125 ? true: false;
    }

    friend std::ostream& operator<<(std::ostream& out, Boolean* signal);
};

std::ostream& operator<<(std::ostream& out, Boolean* signal){
    out << "Singal Value :";
    out << signal->m_Value; 
    out << "Singal Validity :";
    out << signal->m_Validity;
    out << "\n";
    return out;
}


enum Component_ID { 
    INPUT_SIGNAL =0 , 
    CONTROLLER, 
    STATE_MACHINE, 
    OUTPUT_SIGNAL, 
    MAIN_COMPONENT};

class Component{
public:
    Component_ID ID;

    virtual void build() = 0;
    virtual void connect() = 0 ;
    Component(Component_ID p_ID): ID(p_ID){
    }
};

class InputSingalComponent: public Component{
    


public:

    Boolean* m_itsSwitch1;
    Boolean* m_itsSwitch2;
    Boolean* m_itsSwitch3;
    Boolean* m_itsSwitch4;

    InputSingalComponent():Component(INPUT_SIGNAL){

    }

    void build(){
        m_itsSwitch1 = new Boolean();
        m_itsSwitch2 = new Boolean();
        m_itsSwitch3 = new Boolean();
        m_itsSwitch4 = new Boolean();
    }

    void connect(){

    }
};


class ComponentBuilder: public  Component{
    vector<Component*> m_Components;

public:

    ComponentBuilder(): Component(MAIN_COMPONENT){
        m_Components.push_back(new InputSingalComponent);
    }

    void build() override{
        for(Component* comp : m_Components) comp->build();
    }

    void connect() override{
        for(Component* comp : m_Components) comp->connect();
    }

    Component* getComponent(Component_ID p_ID){
        for(Component* comp : m_Components){
            if ( comp->ID == p_ID) return comp;
        } 
        return NULL;
    }
};