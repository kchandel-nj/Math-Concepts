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

# Prime factorization testing
print("Factorize 4: 2, 2")
print(concepts.factorize(4))

print("Factorize 3: 3")
print(concepts.factorize(3))

print("Factorize 36: 2, 2, 3, 3")
print(concepts.factorize(36))

# LCM testing
print("LCM 4, 2: 4")
print(concepts.lcm(4, 2))

print("LCM 13, 6: 78")
print(concepts.lcm(13, 6))

print("LCM 26, 4: 52")
print(concepts.lcm(26,4))

# Root testing
print("2nd root of 3: 1.73ish")
print(concepts.root(3, 2))

print("2nd root of 4: 2")
print(concepts.root(4, 2))

print("2nd root of 99: 9.949ish")
start = time.perf_counter()
print(concepts.root(99, 2))
end = time.perf_counter()
print(f"Took {end - start} seconds to calculate using my method.")
start = time.perf_counter()
print(99 ** (1/2))
end = time.perf_counter()
print(f"Took {end - start} seconds to calculate using Python's built in method.")