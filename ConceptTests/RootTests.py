# Imported Libraries
import time
from Concepts import Concepts

# Object creation
concepts = Concepts()

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