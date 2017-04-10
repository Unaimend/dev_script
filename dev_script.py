import urllib.request
import sys
import tarfile
import os
from distutils.dir_util import copy_tree
print(sys.argv)
from sys import platform as _platform
"""
	TODO:
      look at deft file
"""

mainCodeWithOutSfml = 	("#include <iostream>\n\n\n\n"
						 "int main(int arc, char* argv[])\n"
						 "{\n"
						 "    std::cout << \"HELLO WORLD\" << std::endl\n"
						 "}\n"
						)
mainCodeWithSfml =		(	"#include <SFML/Graphics.hpp>\n\n\n\n"
							"int main()\n"
							"{\n"
							"    sf::RenderWindow window(sf::VideoMode(800, 600), \"My Window\");\n\n	\n"
							"    while (window.isOpen())\n"
							"    {\n"
							"        sf::Event event;\n"
							"        while (window.pollEvent(event))\n"
							"        {\n"
							"            if (event.type == sf::Event::Closed)\n"
							"            {\n"
							"                window.close();\n"
							"            }\n"
							"      }\n"
							"      window.clear(sf::Color::Black);\n"
							"      //draw everything here...\n"
							"      window.display();\n"
							"     }\n"
							"     return 0;\n"
							"}\n"
							)



projectName = ""
projectName = input("Project name pls: ")

LinuxCmakeSfml = """cmake_minimum_required(VERSION 2.8.9)
project ($name)
SET(CMAKE_CXX_FLAGS "-std=c++14 -O0")
include_directories(include)


# For the shared library:
link_directories( ./lib/SFML/)
set ( PROJECT_LINK_LIBS libsfml-graphics.so libsfml-window.so libsfml-system.so)

#However, the file(GLOB...) allows for wildcard additions:
file(GLOB SOURCES "src/*.cpp")
add_executable($name ${SOURCES})
target_link_libraries($name ${PROJECT_LINK_LIBS} )
""".replace("$name", projectName)




macCmakeSfml = """cmake_minimum_required(VERSION 2.8.9)
project ($name)
SET(CMAKE_CXX_FLAGS "-std=c++14 -O0")
include_directories(include)


# For the shared library:
link_directories( ./lib/SFML/)
set ( PROJECT_LINK_LIBS libsfml-graphics.dylib libsfml-window.dylib libsfml-system.dylib)

#However, the file(GLOB...) allows for wildcard additions:
file(GLOB SOURCES "src/*.cpp")
add_executable($name ${SOURCES})
target_link_libraries($name ${PROJECT_LINK_LIBS} )
""".replace("$name", projectName)
#print(LinuxCmakeSfml)

LinuxSfmlAdress = "http://www.sfml-dev.org/files/SFML-2.4.1-linux-gcc-64-bit.tar.gz"
MacSfmlAdress = "http://www.sfml-dev.org/files/SFML-2.4.1-osx-clang.tar.gz"

sfmlName = "SFML-2.4.1"
macSfmlName ="SFML-2.4.1-osx-clang"
sfml = False
"""Which plattofrm am I on?"""
mac = True
linux = False


if _platform == "linux" or _platform == "linux2":
        linux = True
elif _platform == "darwin":
        mac = True
elif _platform == "win32":
        print("Windows is not supported")
        exit(-1)


if "-sfml" in sys.argv:
	sfml = True


os.mkdir(projectName)
os.chdir(projectName)
os.mkdir("src")
os.mkdir("lib")
if sfml == True:
	os.mkdir("lib/SFML")
os.mkdir("include")


#SFML DOWNLOAD

if mac == True:
	print("I am on mac\n")
	if sfml == True:
		urllib.request.urlretrieve(MacSfmlAdress, "sfml")
		t = tarfile.open("sfml",'r')
		t.extractall('.')
		os.remove("sfml")
elif linux == True:
	print("I am on linux\n")
	if sfml == True:
		urllib.request.urlretrieve(LinuxSfmlAdress, "sfml")
		t = tarfile.open("sfml",'r')
		t.extractall('.')
		os.remove("sfml")
else:
	print("I am on not supported\n")
	#STIRB


os.chdir("src")

mainFile = open("main.cpp","w+")
if sfml == True:
	mainFile.write(mainCodeWithSfml)
else:
	mainFile.write(mainCodeWithOutSfml)
os.chdir("..")
if sfml == True:
    if linux == True:
        copy_tree("./" + sfmlName + "/include/", "./include/")
        copy_tree("./" + sfmlName + "/lib/", "./lib/SFML/")
    else:
        print(os.getcwd())
        copy_tree("./"+ macSfmlName + "/include/", os.getcwd() +  "/include/")
        copy_tree("./" + macSfmlName + "/lib/", "./lib/SFML/")
    cmakeFile = open("CMakeLists.txt","w+")
    cmakeFile.write(macCmakeSfml)
else:
    #different cmake
    print("Nicht implementiert")




