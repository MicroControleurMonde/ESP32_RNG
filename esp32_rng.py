# esp32_rng.py
"""
Random Number Generator

RNG Library (Call to ESP32 chip hard-coded RNG function) 

This library provides an interface to generate a random number using the ESP32's hardware RNG.
It enables Wi-Fi temporarily to enhance entropic noise, reads a random value from the RNG_DATA_REG, 
and then disables Wi-Fi.
"""
import network
import machine
import time

class ESP32RNG:
    def __init__(self):
        self.rng_data_reg = 0x3FF75144  # Address of the ESP32 RNG data register
        self.wlan = network.WLAN(network.STA_IF)

    def activate_wifi(self):
        """Activate Wi-Fi on the ESP32."""
        if not self.wlan.active():
            self.wlan.active(True)
            # print("Wi-Fi enabled.")

    def deactivate_wifi(self):
        """Deactivate Wi-Fi on the ESP32."""
        if self.wlan.active():
            self.wlan.active(False)
            # print("Wi-Fi disabled.")

    def get_random_number(self, delay=0.1):
        """ Read a random number from RNG_DATA_REG with a delay.
        Args:
            delay (float): Delay before reading the number in seconds.
        """
        time.sleep(delay)  # Delay before reading
        return machine.mem32[self.rng_data_reg]

    def generate_random_number(self, delay=0.1):
        """Full process to generate a random number: activate Wi-Fi, read number, deactivate Wi-Fi."""
        self.activate_wifi()
        random_number = self.get_random_number(delay)
        self.deactivate_wifi()  # Now ensure Wi-Fi is disabled after reading the number
        return random_number

# Example of using the library
if __name__ == "__main__":
    rng = ESP32RNG()
    random_value = rng.generate_random_number()
    print("Random Value:", random_value)
