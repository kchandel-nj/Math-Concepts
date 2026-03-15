# Math-Concepts
In this repo, I will be applying techniques I learned in my various math classes to see how effective they would be when run by a computer.

Version 1.0:
Holds the first draft of the Sieve of Eratosthenes program, which filters prime numbers by eliminating identified prime multiples.

Version 1.1:
Fixed logical errors in the Sieve of Eratosthenes program.
Created the ConceptTesting file, which will be used to test all concepts implemented.
Imported the time library to measure execution time of functions.

Version 2.0:
Created the first draft of a Greatest Common Denominator finding program.
Implemented the first few tests for finding the GCD.

Version 2.1:
Fixed bugs with the Greatest Common Denominator program.

Version 2.1.5:
Merged all created concepts into one Concepts file.

Version 3.0:
Created and tested a method to factorize any number and return the prime factors.

Version 4.0:
Fixed critical bugs in the GCD method that would result in DivideByZero errors.
Created and tested a method to calculate the Least Common Multiple of any two numbers.

Version 5.0:
Created a method to calculate any root of any number using Binary Search.

Version 6.0:
Created a method to recursively calculate the factorial of any non-negative integer.

Version 6.1:
Added memoization using arrays to the factorial method to save time.
Began implementation of matrix (2D list) memoization to the GCD method to save time.

Version 6.2:
Changed memoization strategy of GCD from a matrix to a nested dict.
Put all tests in their own file. ConceptTesting.py now imports the test file to run it.
Tests can be not run by commenting out the import statement.

Version 6.3:
Memoized GCD should now work without error.
Realized I had some minor mathematical error in the print statements for the GCD tests.
Added a few tests to GCD tests.