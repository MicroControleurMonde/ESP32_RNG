# esp32_rng_random_number.py
"""
This script activates Wi-Fi on the ESP32 (for entropic noise generation), reads random values from the 
RNG_DATA_REG, and then deactivates the Wi-Fi. It displays 10 random values with a short delay between readings.
When the WiFi module is active, the high-speed ADC readings may saturate in extreme cases, reducing entropy.
Therefore, it is advisable to enable the SAR ADC as an additional noise source for the random number generator.
High-speed ADC is enabled automatically when the Wi-Fi or Bluetooth modules is enabled. The ESP32's RNG_DATA_REG
generates random integer numbers as 32-bit values, which can range from −2^31 to 2^31−1 (-2,147,483,648 to 2,147,483,647).

Esp32 technical reference manual / Section 25.Random Number Generator (RNG) / Page #604
"""
import network
import machine
import time

print("ESP32 Random Numbers Generator - 32-bit integers")
# Activate Wi-Fi
wlan = network.WLAN(network.STA_IF)
if wlan.active():
    print("Wi-Fi already active.")
else:
    wlan.active(True)
    print("Wi-Fi enabled.")

try:
    # Address of the ESP register 'RNG_DATA_REG'
    RNG_DATA_REG = 0x3FF75144
    
    # Display 10 random values
    for i in range(10):
        # Access the register
        rng_value = machine.mem32[RNG_DATA_REG]
        print(f"Value from RNG_DATA_REG ({i+1}/{10}): {rng_value}")
        time.sleep(0.1)  # pause between readings
        
except Exception as e:
    print(f"Error reading register RNG_DATA_REG: {e}")

finally:
    # Deactivate Wi-Fi
    wlan.active(False)
    print("\nWi-Fi désactivé.")
