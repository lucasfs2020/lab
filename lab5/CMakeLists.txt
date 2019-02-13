cmake_minimum_required(VERSION 3.3)
project(lab_example)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

add_library(myLib_shared SHARED source/block.c)
add_library(myLib_static STATIC source/block.c)

add_executable(dynamic program.c)
target_link_libraries(dynamic myLib_shared)

add_executable(static program.c)
target_link_libraries(static myLib_static)