# This file will be used to test different concepts as they are developed

# Imported Libraries
import time
from SieveOfEratosthenes import SieveOfEratosthenes
from CommonNumbers import CommonNumbers

# Sieve of Eratosthenes testing
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

# GCD testing
commonFinder = CommonNumbers()
print("Finding gcd of 20, 10 = 10:")
print(commonFinder.gcd(20, 10))

print("Finding gcd of 450, 95 = 5:")
print(commonFinder.gcd(450, 95))

print("Finding gcd of 14, 3 = 1:")
print(commonFinder.gcd(14, 3))