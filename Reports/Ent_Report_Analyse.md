# Analysis of ESP32 Random Number Generator (RNG)

This report analyzes the performance of the random number generator (RNG) of the ESP32 microcontroller. The test evaluates various statistical properties of the generated random data, such as entropy, compression, chi-square distribution, arithmetic mean, and serial correlation. 

## 1. Entropy

The measured entropy is **3.673 bits per byte**.

The ideal entropy of a completely random sequence would be **8 bits per byte**. The entropy of 3.673 bits indicates that the numbers generated are not perfectly random. This suggests that the output is relatively predictable, and there is some structure in the numbers produced.

## 2. Compression (Optimum Compression)

The report indicates that optimizing compression would reduce the file size by **54%**.

This suggests that the data generated contains a structure that allows for significant compression. The values produced by the RNG are not perfectly random, and there are patterns or redundancies that can be exploited for compression.

## 3. Chi-Square Distribution

The chi-square test for **14,141,167 samples** gives a value of **274,740,241.53**.

This value is compared with a theoretical distribution to determine whether the data conform to a uniform distribution model. According to the report, the probability of this value exceeding that obtained is less than **0.01%**. This indicates that the test results are statistically significant. While the ESP32 RNG does not produce perfectly random values (the distribution does not perfectly match a uniform distribution), the results are close enough to be considered reasonably aleatory.

## 4. Arithmetic Mean

The arithmetic mean of the byte values is **45.1836**.

The measured value (45.1836) is significantly lower than **127.5**, the expected value for a perfectly random sequence. This could indicate a bias in the data generated, suggesting that the RNG may favor certain values over others.

## 5. Value of Pi (Monte Carlo)

The value of Pi calculated using the **Monte Carlo method** is **4.000000000**, with an error of **27.32%**.

This indicates poor accuracy when applying the Monte Carlo method to this random number generator. The high error rate (27.32%) suggests that the ESP32 RNG is not reliable enough for advanced calculations that require high-quality randomness.

## 6. Serial Correlation

The **serial correlation** is **0.436625**, which is relatively high.

Serial correlation measures the extent to which one value in the sequence is correlated with the previous value. For a perfectly random sequence, this value should be close to **0**. The value of **0.436625** suggests that successive values are not entirely independent, indicating that the RNG has some degree of correlation between consecutive samples.

## 7. Conclusion

The test shows that, although the ESP32 random number generator produces relatively random data, it has several shortcomings:

- The entropy is not ideal, indicating a certain predictability in the results.
- Optimized compression of the data shows a high degree of redundancy.
- The average byte value is lower than expected.
- The Monte Carlo method for Pi provides a very imprecise result.
- There is noticeable correlation between successive samples, which is not ideal for a random generator.

In summary, while the ESP32 random number generator may be sufficient for general applications, it is not suitable for high-fidelity randomness required in areas such as **cryptography** and other sensitive applications.
