# This file will be used to test different concepts as they are developed

# Imported Libraries
import time
from SieveOfEratosthenes import SieveOfEratosthenes

print("Finding all primes up to the number 10:")
sieve1 = SieveOfEratosthenes(10)
#print(sieve1.numbers)
start = time.perf_counter()
print(sieve1.sieve())
end = time.perf_counter()
print(f"Executed in {end - start} seconds.")

print("Finding all primes up to the number 100:")
sieve2 = SieveOfEratosthenes(100)
#print(sieve2.numbers)
start = time.perf_counter()
print(sieve2.sieve())
end = time.perf_counter()
print(f"Executed in {end - start} seconds.")