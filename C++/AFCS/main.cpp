#include"Library.h"
#include"chrono"
#include"thread"

int main()
{

    ComponentBuilder* itsComponentBuilder =  new ComponentBuilder();

    itsComponentBuilder->build();
    itsComponentBuilder->connect();

    InputSingalComponent* itsInputSingal = (InputSingalComponent*) itsComponentBuilder->getComponent(INPUT_SIGNAL);

    SignalManager* itsSignalManager = SignalManager::get_instance();

    
    while (true)
	{
		itsSignalManager->refreshSignals();
		std::cout << itsInputSingal->m_itsSwitch1 << itsInputSingal->m_itsSwitch2 << itsInputSingal->m_itsSwitch3 << itsInputSingal->m_itsSwitch4;
		std::this_thread::sleep_for(std::chrono::milliseconds(1000));
	}

}