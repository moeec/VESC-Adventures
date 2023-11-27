cmake_minimum_required(VERSION 3.5)
project(vesc)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)


# Uncomment if the package has a setup.py
# ament_python_install_package(${PROJECT_NAME})

# Include directories
include_directories(include)

# Declare a C++ executable
# add_executable(${PROJECT_NAME}_node src/vesc_node.cpp)

# Specify libraries to link a library or executable target against
# target_link_libraries(${PROJECT_NAME}_node
#   ${rclcpp_LIBRARIES}
#   ${std_msgs_LIBRARIES}
# )

# Install targets
install(TARGETS
  # ${PROJECT_NAME}_node
  DESTINATION lib/${PROJECT_NAME})

# Install launch files and other directories
install(DIRECTORY
  launch
  config
  DESTINATION share/${PROJECT_NAME}/
)

# Export dependencies
ament_package()

