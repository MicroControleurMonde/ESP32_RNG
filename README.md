# ESP32_RNG

A Micro-python library which provides an interface to generate a TRUE random number using the ESP32's hardware RNG. 
It enables Wi-Fi temporarily to enhance entropic noise, reads a random value from the RNG_DATA_REG, and then disables Wi-Fi.

* Library :            **esp32_rng.py**
* Libarary test:       **test_esp32_rng.py**
* Example:             **esp32_rng_random_number.py**

Source:  Esp32 technical reference manual (Version 5.2) / Section 25.Random Number Generator (RNG) / Page #604


Example of "Classical" code **not using** the direct call to the ESP32 hardware and calling 'urandom' lib instead (pseudo random number)
* esp32_random_number.py

The ESP32 RNG generates random integer numbers as 32-bit values.

# TRNG validation
~~* Considering that the Espressif ESP32 chip has already been tested and approved using the Dieharder Random Number Test Suite (version 3.31.1),~~
~~I will not repeat the tests to validate the reliability of the generator.~~
### Update(24.11.24)

While testing my RNG on RP2040 [Link](https://github.com/MicroControleurMonde/RP2040-RNG), I became very aware of the entropy weakness provided by my MCU generator. 

So the decision was to also test the Espressif ESP32 chip to confirm its reliability as a TRNG.

Testing tools used:

* Ent (28.01.2008)
* Dieharder version 3.31.1

# Ent Test Report 
  ([www.fourmilab.ch](https://www.fourmilab.ch/random/)) John Walker
- Sample size: **13.4 MB**
- Total generated: **1'180'000 values**

- [Ent Report -Raw](https://github.com/MicroControleurMonde/ESP32_RNG/blob/main/Reports/Ent_Report_ESP32.txt)
- [Ent Report Analyse](https://github.com/MicroControleurMonde/ESP32_RNG/blob/main/Reports/Ent_Report_Analyse.md)

# Dieharder Test Report
(https://webhome.phy.duke.edu/~rgb/General/dieharder.php) Robert G. Brown

- Sample size: **13.4 MB**
- Total generated: **1'180'000 values**

- [Dieharder Report - Raw](https://github.com/MicroControleurMonde/ESP32_RNG/blob/main/Reports/DieHard_Tests_esp32%20%232.txt)
- [Dieharder Report Analyses](https://github.com/MicroControleurMonde/ESP32_RNG/blob/main/Reports/DieHard_Tests_Analyses.md)

  
  
# Special tribute:

## Passing of John Walker

We are deeply saddened to hear of the passing of John Walker, one of the founders of Autodesk. He died at home in Switzerland, on 2nd February 2024, aged 74.

[The announcement was shared here.](https://www.engineering.com/a-cad-legend-passes-autodesk-founder-john-walker-1949-to-2024/)
