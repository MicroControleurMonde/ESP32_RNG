# test_esp32_rng.py

from esp32_rng import ESP32RNG

# Create an instance of the ESP32RNG class
rng = ESP32RNG()

# Generate and display a random value
random_value = rng.generate_random_number()
print("Random Value:", random_value)
