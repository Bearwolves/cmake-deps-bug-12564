cmake_minimum_required(VERSION 3.15)
project(hello_exe CXX)

find_package(conan-libs REQUIRED)

add_executable(hello_exe src/main.cpp)
target_include_directories(hello_exe PUBLIC
    conan-libs::conan-libs
    # ${conan-libs_INCLUDE_DIRS}
)

target_link_directories(hello_exe PUBLIC
    conan-libs::conan-libs
    # ${conan-libs_LIB_DIRS}
)

target_link_libraries(hello_exe PUBLIC
    hellolib1
)

install(TARGETS hello_exe)
