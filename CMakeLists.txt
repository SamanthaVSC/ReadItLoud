cmake_minimum_required(VERSION 3.21)

project(ReadItLoud VERSION 1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt6 REQUIRED COMPONENTS
    Widgets
    WebEngineWidgets
)

# We want Qt's automatic MOC, but we explicitly manage .ui files with qt_add_ui().
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC OFF)
set(CMAKE_AUTORCC ON)

qt_add_executable(ReadItLoud
    src/main.cpp
    src/ui/appwindow.cpp
    src/ui/appwindow.h
    src/handler.cpp
    src/handler.h
    src/workers/appmodel.h
    src/workers/appmodel.cpp
    src/ui/loadingmessage.ui
    assets/resources.qrc
)

# Explicitly register the Designer form. This avoids AUTOUIC searching for it.
qt_add_ui(ReadItLoud
    SOURCES src/ui/appwindow.ui
)

target_link_libraries(ReadItLoud PRIVATE
    Qt6::Widgets
    Qt6::WebEngineWidgets
)

target_include_directories(ReadItLoud PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/src
)

set_target_properties(ReadItLoud PROPERTIES
    WIN32_EXECUTABLE ON
    MACOSX_BUNDLE ON
)