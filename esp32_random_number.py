import machine
import urandom

# Function to obtain a 32-bit random number
def get_random():
    return urandom.getrandbits(32)

# Function to fill a buffer with random bytes
def fill_random(buffer):
    for i in range(len(buffer)):
        buffer[i] = urandom.getrandbits(8)

# Example of use
print("32-bit random number:", get_random())

# Create a 16-byte buffer
buffer = bytearray(16)
fill_random(buffer)
print("Random buffer:", buffer)

# Generate a random number periodically
def periodic_random(timer):
    print("Periodic random number:", get_random())

# Configure a timer to generate a number every 5 seconds
timer = machine.Timer(0)
timer.init(period=5000, mode=machine.Timer.PERIODIC, callback=periodic_random)
