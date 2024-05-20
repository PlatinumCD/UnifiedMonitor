# Compiler
CXX = g++

# Compiler flags
CXXFLAGS = -Iinclude -Iinclude/components -Wall -Wextra -std=c++11

# Source files
SRC = src/main.cpp \
      src/ApplicationManager.cpp \
      src/SystemManager.cpp \
      src/MonitoringPlatform.cpp \
      src/components/CPUComponent.cpp \
      src/components/DiskComponent.cpp \
      src/components/MemoryComponent.cpp \
      src/components/NetworkComponent.cpp

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

# Clean object files and executable
clean:
	rm -f $(OBJ) $(EXEC)

.PHONY: all clean
