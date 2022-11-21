#include <iostream>
#include "hellolib2.h"

void hellolib2(){
    // ARCHITECTURES
    #if __x86_64__
    std::cout << "  hellolib/0.1: __x86_64__ defined\n";
    #endif

    #if __aarch64__
    std::cout << "  hellolib/0.1: __aarch64__ defined\n";
    #endif
}
