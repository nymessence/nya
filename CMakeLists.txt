cmake_minimum_required(VERSION 3.10)

# Project name: LymDeya (Nya-Brahmanda Consciousness Achievement)
project(LymDeya)

# Set C++ standard to C++17 for modern features
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Add compiler flags for optimization and debugging
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -O2")

# Define the executable name as LymDeya (Nya-Lym Universal Consciousness)
add_executable(LymDeya
    lym-deya-core/LymDeya.cpp
    lym-deya-core/BrahmandaLym.cpp
    lym-deya-core/KarmaExec.cpp
)

# Include directories for header files
target_include_directories(LymDeya PRIVATE
    ${CMAKE_SOURCE_DIR}/lym-deya-core
)

# Install the executable to system path
install(TARGETS LymDeya DESTINATION bin)