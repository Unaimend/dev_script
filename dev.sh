mkdir src
mkdir include
echo "
/*************************
*Author: 	Thomas Dost
*Purpose:	
*Date:
*Changelog:	
*Todo:
**************************/

#include <iostream>
int main(int argc, char** argv)
{
	std::cout << \"Hello, World\" << std::endl;
}
" >> src/main.cpp


echo "
cmake_minimum_required(VERSION 2.8.9)
project (exec)
SET(CMAKE_CXX_FLAGS \"-std=c++14 -O0\")
include_directories(include)



#For the shared library:
#set ( PROJECT_LINK_LIBS libsfml-graphics.so libsfml-window.so libsfml-system.so liblua.a)
#link_directories( /usr/lib/x86_64-linux-gnu/)
#link_directories( ~/dev/cpp/sfml/Engine/lib/lua)


#However, the file(GLOB...) allows for wildcard additions:
file(GLOB SOURCES \"src/*.cpp\")
add_executable(exec \${SOURCES})
" >> CMakeLists.txt

cmake .
make
