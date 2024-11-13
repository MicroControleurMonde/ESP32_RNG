# ESP32_RNG

A Micro-python library which provides an interface to generate a TRUE random number using the ESP32's hardware RNG. 
It enables Wi-Fi temporarily to enhance entropic noise, reads a random value from the RNG_DATA_REG, and then disables Wi-Fi.

* Library :          esp32_rng.py
* Libarary test:     test_esp32_rng.py
* Example:           esp32_rng_random_number.py

Source:  Esp32 technical reference manual (Version 5.2) / Section 25.Random Number Generator (RNG) / Page #604


Example of "Classical" code not using the direct call to the ESP32 hardware and calling 'urandom' lib instead (pseudo random number)
* esp32_random_number.py

The ESP32 RNG generates random integer numbers as 32-bit values.

# RNG validation
* Considering that the Espressif ESP32 chip has already been tested and approved using the Dieharder Random Number Test Suite (version 3.31.1),
I will not repeat the tests to validate the reliability of the generator.

