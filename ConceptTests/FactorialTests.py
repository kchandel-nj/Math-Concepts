# Imported Libraries
import time
from Concepts import Concepts

# Object creation
concepts = Concepts()

# Factorial testing
print("0! = 1, 1! = 1")
print(concepts.factorial(0))
print(concepts.factorial(1))

print("5! = 120")
print(concepts.factorial(5))

print("Negative factorial throws error")
try:
    print(concepts.factorial(-1))
except:
    print("Exception thrown.")