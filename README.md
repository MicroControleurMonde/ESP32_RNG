# ESP32_RNG

A Micro-python library which provides an interface to generate a TRUE random number using the ESP32's hardware RNG. 
It enables Wi-Fi temporarily to enhance entropic noise, reads a random value from the RNG_DATA_REG, and then disables Wi-Fi.

* Library :          esp32_rng.py
* Libarary test:     test_esp32_rng.py
* Example:           esp32_rng_random_number.py

Example of "Classical" code not using the direct call to the ESP32 hardware and calling 'urandom' lib instead (pseudo random number)
* esp32_random_number.py
