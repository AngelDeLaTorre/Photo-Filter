cmake_minimum_required(VERSION 2.8)
project( imageproc )

find_package(OpenMP REQUIRED)
if(OPENMP_FOUND)
message(STATUS "Enabling OpenMP support")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} ${OpenMP_EXE_LINKER_FLAGS}")
else()
message(STATUS "Disabling OpenMP support")

endif()

message("${CMAKE_CXX_FLAGS}")
message("${CMAKE_C_FLAGS}")

find_package( OpenCV REQUIRED )
add_executable( imageproc main.cpp)
target_link_libraries( imageproc ${OpenCV_LIBS} )