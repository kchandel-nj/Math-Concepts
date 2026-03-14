# Imported Libraries
import time
from Concepts import Concepts

# Object creation
concepts = Concepts()

# GCD testing
print("Finding gcd of 5, 0 = 5:")
print(concepts.gcd(5, 0))

print("Finding gcd of 5, 1 = 5:")
print(concepts.gcd(5, 1))

print("Finding gcd of 0, 5 = 5:")
print(concepts.gcd(0, 5))

print("Finding gcd of 0, 6 = 6:")
print(concepts.gcd(0, 6))

print("Finding gcd of 1, 5 = 5:")
print(concepts.gcd(1, 5))

print("Finding gcd of 1, 6 = 6:")
print(concepts.gcd(1, 6))

print("Finding gcd of 20, 10 = 10:")
print(concepts.gcd(20, 10))

print("Finding gcd of 450, 95 = 5:")
print(concepts.gcd(450, 95))

print("Finding gcd of 14, 3 = 1:")
print(concepts.gcd(14, 3))