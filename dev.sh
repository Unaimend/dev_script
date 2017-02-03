#Author: Thomas Dost
#falls kein Projektname angegeben ist wird das erste Argument zum Projektnamen.

#TODO: git, lua
#TODO STH DOESNT WORK.
#MAnuelles make im ordner funktioniert allerdings ist irwas im ordner falsch

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
    wget http://www.sfml-dev.org/files/SFML-2.4.0-osx-clang.tar.gz 
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


if (("$sfml" == "true"))
then

	echo "
/*************************
*Author: 	Thomas Dost
*Purpose:	
*Date:
*Changelog:	
*Todo:
**************************/

#include <SFML/Audio.hpp>
#include <SFML/Graphics.hpp>
int main()
{
    // Create the main window
    sf::RenderWindow window(sf::VideoMode(800, 600), \"SFML window\");
    // Start the game loop
    while (window.isOpen())
    {
        // Process events
        sf::Event event;
        while (window.pollEvent(event))
        {
            // Close window: exit
            if (event.type == sf::Event::Closed)
                window.close();
        }
        // Clear screen
        window.clear();
        // Update the window
        window.display();
    }
    return EXIT_SUCCESS;
}
" >> src/main.cpp
	echo "SFML main"
else
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
echo "Default cpp main"
fi

if (("$sfml" == "true"))
then
	
echo "
cmake_minimum_required(VERSION 2.8.9)
project ($name)
SET(CMAKE_CXX_FLAGS \"-std=c++14 -O0\")
include_directories(include)


link_directories( ./lib/)
# For the shared library:
set ( PROJECT_LINK_LIBS libsfml-graphics.dylib libsfml-window.dylib libsfml-system.dylib)


#However, the file(GLOB...) allows for wildcard additions:
file(GLOB SOURCES \"src/*.cpp\")
add_executable($name \${SOURCES})
target_link_libraries($name \${PROJECT_LINK_LIBS} )
" >> CMakeLists.txt

	echo "SFML CMake"
else

echo "
cmake_minimum_required(VERSION 2.8.9)
project ($name)
SET(CMAKE_CXX_FLAGS \"-std=c++14 -O0\")
include_directories(include)

file(GLOB SOURCES \"src/*.cpp\")
add_executable($name \${SOURCES})
# target_link_libraries(libtest \${PROJECT_LINK_LIBS} )
" >> CMakeLists.txt
echo "cpp default cmake"
fi


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
	tar xf SFML-2.4.0-osx-clang.tar.gz
    rm  SFML-2.4.0-osx-clang.tar.gz
    mv SFML-2.4.0-osx-clang $name
    cd $name/SFML-2.4.0-osx-clang
    mv include/* ../include/
    mv lib/*	../lib/

    echo "SFML was succesfully downloaded"
else
	echo "Failure"
fi


# http://www.sfml-dev.org/files/SFML-2.4.0-windows-gcc-4.9.2-tdm-64-bit.zip

exit 1