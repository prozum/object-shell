cmake_minimum_required(VERSION 3.9)
project(object_shell)

set(CMAKE_CXX_STANDARD 17)

find_package(PkgConfig REQUIRED)
pkg_check_modules(JSON_CPP REQUIRED jsoncpp )

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/Commands)
file(COPY Commands DESTINATION ${CMAKE_BINARY_DIR})
file(COPY Schemas DESTINATION ${CMAKE_BINARY_DIR})
file(COPY Rules DESTINATION ${CMAKE_BINARY_DIR})

add_executable(Select Select.cpp)
target_link_libraries(Select ${JSON_CPP_LIBRARIES})
target_include_directories(Select PUBLIC ${JSON_CPP_INCLUDE_DIRS})
