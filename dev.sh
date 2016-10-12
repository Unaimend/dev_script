#Author: Thomas Dost
#falls kein Projektname angegeben ist wird das erste Argument zum Projektnamen.



# http://www.sfml-dev.org/files/SFML-2.4.0-windows-gcc-4.9.2-tdm-64-bit.zip
sfml="false"

if (( "$#" == 0 )) 
	then 
		
		echo "Pls enter a project name"
		read -p "Enter: " name
		name=${name}
	else
		#echo "YAY"
		#echo $1
		name=${1}
fi

if (( "$@" == "-sfml" ))
then
    wget http://www.sfml-dev.org/files/SFML-2.4.0-windows-gcc-4.9.2-tdm-64-bit.zip 
    $sfml = true;
else
    echo "NO"
fi

#echo $name
mkdir $name
cd $name

mkdir src
mkdir include
mkdir lib
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
	std::cout << \"Hello, $name\" << std::endl;
}
" >> src/main.cpp


echo "
cmake_minimum_required(VERSION 2.8.9)
project ($name)
SET(CMAKE_CXX_FLAGS \"-std=c++14 -O0\")
include_directories(include)



#For the shared library:
#set ( PROJECT_LINK_LIBS libsfml-graphics.so libsfml-window.so libsfml-system.so liblua.a)
#link_directories( /usr/lib/x86_64-linux-gnu/)
#link_directories( ~/dev/cpp/sfml/Engine/lib/lua)


#However, the file(GLOB...) allows for wildcard additions:
file(GLOB SOURCES \"src/*.cpp\")
add_executable($name \${SOURCES})
" >> CMakeLists.txt



cmake .
make
echo "
{
	\"build_systems\":
	[
		{
			
		}
	],
	\"folders\":
	[
		{
			\"path\": \"./include\",
			\"path\": \"./src\",
			\"path\": \".\",
			//"file_exclude_patterns": 
			//[

			//]
		},
		// {
		// 	"path": "Kapitel"

		// }
	],
	\"settings\":
	{
		\"tab_size\": 4
	}
}

"	>> $name".sublime-project"

sublime $name".sublime-project" 

if (("$sfml" == "true"))
then
	cd ..
	unzip SFML-2.4.0-windows-gcc-4.9.2-tdm-64-bit.zip
    rm -r SFML-2.4.0-windows-gcc-4.9.2-tdm-64-bit.zip
    mv SFML-2.4.0 $name
    cd $name/SFML-2.4.0
    mv include/* ../include/
    mv lib/*	../lib/

    echo "SFML was succesfully downloaded"
else
	echo "Failure"
fi


# http://www.sfml-dev.org/files/SFML-2.4.0-windows-gcc-4.9.2-tdm-64-bit.zip

exit 1