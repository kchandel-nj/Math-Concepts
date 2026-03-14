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