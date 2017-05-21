import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import sys
from sys import platform as _platform

from distutils.dir_util import copy_tree

import urllib.request
import sys
import tarfile
import os
from enum import Enum
# Uses PEP8 style guide


#TODO Der Projektname wird nicht übernommen, da die Textersetzung für den Projektnamen bereits
#TODO im Konstruktor der Klasse CppAutomation passiert(Er wird auf Default gesetzt)

class CppAutomation(object):
    linux = False
    mac = False
    windows = False

    # Wofür war das?
    sfmlName = "SFML-2.4.1"
    macSfmlName = "SFML-2.4.1-osx-clang"


    def __init__(self, project_name):
        # 2-Dimensionales Array für die Verwaltung von platttformspezifischen Daten wie z.B. Download Addressen
        # oder CMake-Datein



        self.download_sfml_state = False
        #downloadGitState = False
        #downloadLuaState = False



        self.project_name = project_name;

        self.os_download_address = {}
        self.os_download_address["MAC"] = {}
        self.os_download_address["LINUX"] = {}
        self.os_download_address["WINDOWS"] = {}
        # Download Addresse für MAC von SFML
        self.os_download_address["MAC"]["SFML"] = "http://www.sfml-dev.org/files/SFML-2.4.1-osx-clang" \
                                                                 ".tar.gz "
        # Download Addresse für LINUX von SFML
        self.os_download_address["LINUX"]["SFML"]= "http://www.sfml-dev.org/files/SFML-2.4.1-linux" \
                                                                   "-gcc-64-bit.tar.gz "

        self.os_cmake = {}
        self.os_cmake["MAC"] = {}
        self.os_cmake["LINUX"] = {}
        self.os_cmake["WINDOWS"] = {}

        self.os_cmake["MAC"]["SFML"] = """
                                        cmake_minimum_required(VERSION 2.8.9)
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
                                        """.replace("$name", self.project_name)

        self.os_cmake["LINUX"]["SFML"] = """
                                        cmake_minimum_required(VERSION 2.8.9)
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
                                        """.replace("$name", self.project_name)

        self.os_cmake["UNSPECIFIC"] = """
                                        cmake_minimum_required(VERSION 2.8.9)
                                        project ($name)
                                        SET(CMAKE_CXX_FLAGS "-std=c++14 -O0")
                                        include_directories(include)
                                        
                                        # For the shared library:
                                        
                                        #However, the file(GLOB...) allows for wildcard additions:
                                        file(GLOB SOURCES "src/*.cpp")
                                        add_executable($name ${SOURCES})
                                        """.replace("$name", self.project_name)


        #TODO statisch machen
        self.os_main_code = {}
        self.os_main_code["SFML"] = {}
        self.os_main_code["NOTHING"] = {}

        self.os_main_code["SFML"] = (
                                    "#include <SFML/Graphics.hpp>\n\n\n\n"
                                    "int main()\n"
                                    "{\n"
                                    "    sf::RenderWindow window(sf::VideoMode(800, 600), \"My Window\");\n\n	\n"
                                    "    while (window.isOpen())\n"
                                    "    {\n"
                                    "        sf::Event event;\n"
                                    "        while (window.pollEvent(event))\n"
                                    "        {\n"
                                    "            if (event.type == s^f::Event::Closed)\n"
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

        self.os_main_code["NOTHING"] = (
                                        "#include <iostream>\n\n\n\n"
                                        "int main(int arc, char* argv[])\n"
                                        "{\n"
                                        "    std::cout << \"HELLO WORLD\" << std::endl\n;"
                                        "}\n"
                                        )




        # Plattform bestimmen
        if _platform == "linux" or _platform == "linux2":
            CppAutomation.linux = True
        elif _platform == "darwin":
            CppAutomation.mac = True
        elif _platform == "win32":
            CppAutomation.windows = True
            print("Windows is not supported")
            exit(-1)


    def downloadSfml(self):
        #TODO Irgendiwe anzeigen das gerade gedownloaded wird
        # SFML DOWNLOAD
        if CppAutomation.mac:
            print("I am on mac\n")
            urllib.request.urlretrieve(self.os_download_address["MAC"]["SFML"], "sfml")
            t = tarfile.open("sfml", 'r')
            t.extractall('.')
            os.remove("sfml")
        elif CppAutomation.linux:
            print("I am on linux\n")
            urllib.request.urlretrieve(self.os_download_address["MAC"]["SFML"], "sfml")
            t = tarfile.open("sfml", 'r')
            t.extractall('.')
            os.remove("sfml")
        else:
            print("I am on not supported\n")
















#################################################################
class CppAutomationGui(object):
    def __init__(self, root: tk.Tk):
        """
        Konstruktor für die Klasse Gui
        :param root: eine Tk-Instanz(Tk())
        """
        self.root = root
        self.downloadSfmlState = tk.IntVar()
        self.downloadGitState = tk.IntVar()
        self.downloadLuaState = tk.IntVar()

        self.project_name = tk.StringVar()
        self.dir_opt = {}
        self.path = 0
        self.project_window = 0
        self.project_options_go_button = 0
        self.project_options_close_button = 0

        self.download_sfml_box = 0
        self.download_lua_box = 0
        self.where_button = 0

        self.project_name_box = 0
        self.project_name_label = 0
        self.project_name_label_text = tk.StringVar()

        self.automation = CppAutomation("Default");


        self.new_project = tk.Button(
            self.root, text="New", command=self.new_project
        ).grid(row=0, column=0)
        self.exit_button = tk.Button(
            root, text="Exit", command=root.quit).grid(row=1, column=0)




    def ask_dir(self):
        """
        Speichert den Pfad den tk.filedialog zurückgibt in self.path
        """
        self.dir_opt['title'] = 'Please select directory'
        self.path = tk.filedialog.askdirectory(**self.dir_opt)
        if not self.path:
            return

    def new_project(self):
        """
        Öffnet das Fenster welches die Projektoptionen anzeigt
        :return: 
        """
        self.ask_dir()
        self.project_window = tk.Toplevel(self.root)
        self.project_window.title("Project Options")

        self.download_sfml_box = tk.Checkbutton(
            self.project_window, text="SFML", variable=self.downloadSfmlState)
        self.download_sfml_box.grid(row=0)
        # self.download_lua_box = tk.Checkbutton(
        #     self.project_window, text="Lua", variable=self.downloadLuaState).grid(row=0, column=1)

        self.project_options_go_button = tk.Button(
            self.project_window, text="Go", command=self.go
        ).grid(row=2, column=0)

        self.project_options_close_button = tk.Button(
            self.project_window, text="Close", command=self.project_window.destroy
        ).grid(row=2, column=1)

        self.project_name_box = tk.Text(
            self.project_window, height=1, width=30, relief="sunken", borderwidth=2
        )
        
        self.project_name_box.grid(row=1, column=2, sticky=tk.W)

        self.project_name_label = tk.Label(
            self.project_window, height=1, width=10, relief="sunken", anchor=tk.W, textvariable=self.project_name_label_text, borderwidth=2
        ).grid(row=1)
        self.project_name_label_text.set("Project Name")

    def go(self):
        """
        
        :return: 
        """
        #TODO Checken ob Pfad schon exisitiert
        #TODO Gehoert das Alles hier hin? Seperate Klasse? Eigene Funktion?
        project_name = self.project_name_box.get("1.0", "end-1c")
        if not project_name:
            tk.messagebox.showerror("No project name", "The project name must not be empty")
            return -1
        os.chdir(self.path)
        os.mkdir(project_name)
        os.chdir(project_name)

        os.mkdir("src")
        os.mkdir("include")
        os.mkdir("lib")
        if self.downloadSfmlState.get():
            os.mkdir("lib/SFML")

        self.automation.project_name = project_name

        if self.downloadSfmlState.get():
            self.automation.download_sfml_state = True
            self.automation.downloadSfml()
        else:
            self.automation.download_sfml_state = False

        os.chdir("src")

        mainFile = open("main.cpp", "w+")
        if self.automation.download_sfml_state == True:
            mainFile.write(self.automation.os_main_code["SFML"])
        else:
            mainFile.write(self.automation.os_main_code["NOTHING"])
        os.chdir("..")
        if self.automation.download_sfml_state:
            if CppAutomation.linux:
                # BUG Warum sieht das nicht so aus wie bei mac(1. copy_tree aufruf)?
                copy_tree("./" + CppAutomation.sfmlName + "/include/", "./include/")
                copy_tree("./" + CppAutomation.sfmlName + "/lib/", "./lib/SFML/")
                cmakeFile = open("CMakeLists.txt", "w+")
                cmakeFile.write(self.automation.os_cmake["LINUX"]["SFML"])
            elif CppAutomation:
                copy_tree("./" + self.automation.macSfmlName + "/include/", os.getcwd() + "/include/")
                copy_tree("./" + self.automation.macSfmlName + "/lib/", "./lib/SFML/")
                cmakeFile = open("CMakeLists.txt", "w+")
                cmakeFile.write(self.automation.os_cmake["MAC"]["SFML"])
            else:
                print("Windows is not supported")
                exit(-1)
        else:
            cmakeFile = open("CMakeLists.txt", "w+")
            cmakeFile.write(self.automation.os_cmake["UNSPECIFIC"])





    def run(self):
        """
        Startet die GUI
        """
        self.root.mainloop()


GUI = CppAutomationGui(tk.Tk())
GUI.run()
print(GUI.path)
