cmake_minimum_required(VERSION 3.15)
project(hellolibs CXX)

add_library(hellolib1 SHARED src/hellolib1.cpp)
target_include_directories(hellolib1 PUBLIC include)

set_target_properties(hellolib1 PROPERTIES PUBLIC_HEADER "include/hellolib1.h")
install(TARGETS hellolib1)


add_library(hellolib2 SHARED src/hellolib2.cpp)
target_include_directories(hellolib2 PUBLIC include)

set_target_properties(hellolib2 PROPERTIES PUBLIC_HEADER "include/hellolib2.h")
install(TARGETS hellolib2)


add_library(hellolib3 SHARED src/hellolib3.cpp)
target_include_directories(hellolib3 PUBLIC include)

set_target_properties(hellolib3 PROPERTIES PUBLIC_HEADER "include/hellolib3.h")
install(TARGETS hellolib3)

