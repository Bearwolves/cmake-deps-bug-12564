cmake_minimum_required(VERSION 3.24.1)
project(hello_exe CXX)

find_package(conan-libs REQUIRED)

add_executable(${PROJECT_NAME} src/main.cpp)

############### INCLUDE DIRECTORIES ###########################

get_property(main_inc_dirs_libs TARGET conan-libs::conan-libs PROPERTY INTERFACE_INCLUDE_DIRECTORIES)
message(STATUS "MAIN - main_inc_dirs_libs ${main_inc_dirs_libs}")

target_include_directories(${PROJECT_NAME} PUBLIC
    conan-libs::conan-libs
)

get_property(main_inc_dirs_hello TARGET ${PROJECT_NAME} PROPERTY INTERFACE_INCLUDE_DIRECTORIES)
message(STATUS "MAIN - main_inc_dirs_hello ${main_inc_dirs_hello}")

############### LINK DIRECTORIES ###########################

get_property(main_lib_dirs_libs TARGET conan-libs::conan-libs PROPERTY INTERFACE_LINK_DIRECTORIES)
message(STATUS "MAIN - main_lib_dirs_libs ${main_lib_dirs_libs}")

target_link_directories(${PROJECT_NAME} PUBLIC
    conan-libs::conan-libs
)

get_property(main_lib_dirs_hello TARGET ${PROJECT_NAME} PROPERTY INTERFACE_LINK_DIRECTORIES)
message(STATUS "MAIN - main_lib_dirs_hello ${main_lib_dirs_hello}")

target_link_libraries(${PROJECT_NAME} PUBLIC
    hellolib1
)

install(TARGETS ${PROJECT_NAME})
