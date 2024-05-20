# Compiler
CXX = g++

# Compiler flags
CXXFLAGS = -Iinclude -Iinclude/components -Wall -Wextra -std=c++20

# Source files
SRC = src/main.cpp \
      src/application_manager.cpp \
      src/system_manager.cpp \
      src/monitoring_platform.cpp \
      src/components/cpu_component.cpp \
      src/components/disk_component.cpp \
      src/components/memory_component.cpp \
      src/components/network_component.cpp

# Object files
OBJ = $(SRC:.cpp=.o)

# Executable
EXEC = monitoring_platform

# Default target
all: $(EXEC)

# Link object files to create executable
$(EXEC): $(OBJ)
	$(CXX) $(CXXFLAGS) -o $@ $^

# Compile source files into object files
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Build Docker image
build:
	docker build -t drp-image .

# Run Docker container in interactive mode and mount current directory to /local
run: build
	docker run -it --rm -v $(shell pwd):/local drp-image

# Clean object files and executable
clean:
	rm -f $(OBJ) $(EXEC) perf_logs

.PHONY: all clean build run
