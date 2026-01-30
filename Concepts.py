class Concepts:

    """
    Docstring for Concepts

    Applies various mathematical concepts learned in classes through Python and various programming techniques.
    """

    def __init__(self):
        """
        Docstring for __init__

        Initializes the object.
        
        :param self: The object
        """
        pass

    def sieve(self, limit: int) -> list:
        """
        Docstring for sieve
        
        :param self: The object
        :return: A list of prime numbers up to the limit
        :rtype: list
        """

        primes = list(range(2, limit + 1))
        for num in primes[:]:
            for candidate in range(num * 2, limit + 1, num):
                if candidate in primes:
                    primes.remove(candidate)

        return primes
    
    def gcd(self, num1: int, num2: int) -> int:
        """
        Docstring for gcd

        Finds the Greatest Common Denominator of two numbers using the Euclidean algorithm.
        
        :param self: The object
        :param num1: The first number
        :type num1: int
        :param num2: The second number
        :type num2: int
        :return: The GCD of the two numbers
        :rtype: int
        """

        # num1 = num2 * (num1 / num2) + num1 % num2
        # num1 = num2 * _integerDivide(num1, num2) + _remainder(num1, num2)
        if num1 % num2 == 0:
            return num2
        elif num1 % num2 == 1:
            return 1
        else:
            return self.gcd(num2, num1 % num2)
        
    def factorize(self, num: int):# -> list[int]:
        """
        Docstring for factorize

        Returns the prime factorization of a number.
        
        :param self: The object
        :param num: The number to factorize
        :return: A list of prime factors
        :rtype: list[int]
        """

        return self._factors(num, self.sieve(num), [])
        
    def _factors(self, num: int, primesBelow: list[int], factorization: list[int]):# -> list[int]:
        if primesBelow[-1] == num:
            factorization.append(num)
            return factorization
        else:
            for p in primesBelow:
                if num % p == 0:
                    factorization.append(p)
                    newNum = int(num / p)
                    return self._factors(newNum, self.sieve(newNum), factorization)