#include <iostream>
#include <chrono>
#include <thread>

// Function to send RPM command to the VESC.
void vesc_send_rpm(int rpm) {
    // Add code to send RPM command to VESC.
    // This will depend on how you've set up communication with the VESC.
}

int main() {
    try {
        // Set the VESC to 300 RPM for 5 seconds
        vesc_send_rpm(300);
        std::this_thread::sleep_for(std::chrono::seconds(5));

        // Then set the VESC to 800 RPM
        vesc_send_rpm(800);
        std::this_thread::sleep_for(std::chrono::seconds(5)); // Adjust this duration as needed

        // Finally, turn off the VESC
        vesc_send_rpm(0);
    } catch (const std::exception& e) {
        std::cerr << "An exception occurred: " << e.what() << '\n';
    }

    return 0;
}