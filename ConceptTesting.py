# This file will be used to test different concepts as they are developed

# Imported Libraries
import time
from Concepts import Concepts

# Object creation
concepts = Concepts()

# Sieve of Eratosthenes testing
print("Finding all primes up to the number 10:")
sieve1 = concepts.sieve(10)
#print(sieve1.numbers)
start = time.perf_counter()
print(sieve1)
end = time.perf_counter()
print(f"Executed in {end - start} seconds.")

print("Finding all primes up to the number 100:")
sieve2 = concepts.sieve(100)
#print(sieve2.numbers)
start = time.perf_counter()
print(sieve2)
end = time.perf_counter()
print(f"Executed in {end - start} seconds.")

# GCD testing
print("Finding gcd of 20, 10 = 10:")
print(concepts.gcd(20, 10))

print("Finding gcd of 450, 95 = 5:")
print(concepts.gcd(450, 95))

print("Finding gcd of 14, 3 = 1:")
print(concepts.gcd(14, 3))