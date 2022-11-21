#include <iostream>
#include "hellolib1.h"

void hellolib1(){
    #ifdef NDEBUG
    std::cout << "hellolib/0.1: Hello World Release!\n";
    #else
    std::cout << "hellolib/0.1: Hello World Debug!\n";
    #endif
}
