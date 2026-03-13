class Concepts:

    """
    Docstring for Concepts

    Applies various mathematical concepts learned in classes through Python and various programming techniques.
    """

    def __init__(self):
        """
        Docstring for __init__

        Initializes the object.
        Creates lists for faster calculation of various recursive algorithms.
        
        :param self: The object
        """

        self.calculated_factorials = []
        self.calculated_primes = []
        self.calculated_GCDs = [[]]
        self.calculated_GCDs.insert(0, [0])

    def sieve(self, limit: int) -> list:
        """
        Docstring for sieve
        
        :param self: The object
        :return: A list of prime numbers up to the limit
        :rtype: list
        """

        primes = list(range(2, limit + 1))
        for num in primes[:]: # Iterates over a shallow copy
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
        if num1 == 0 and num2 == 0:
            return self.calculated_GCDs[num1][num2]
        if num2 == 0:
            try:
                self.calculated_GCDs[num1][num2] = abs(num1)
            except IndexError:
                try:
                    self.calculated_GCDs[num1].insert(num2, abs(num1))
                except IndexError:
                    self.calculated_GCDs.insert(num1, [])
                    self.calculated_GCDs[num1].insert(num2, abs(num1))
            
            return abs(num1)
        return self.gcd(num2, num1 % num2)
        
    def factorize(self, num: int):
        """
        Docstring for factorize

        Returns the prime factorization of a number.
        
        :param self: The object
        :param num: The number to factorize
        :return: A list of prime factors
        :rtype: list[int]
        """

        return self._factors(num, self.sieve(num), [])
        
    def _factors(self, num: int, primesBelow: list[int], factorization: list[int]):
        """
        Docstring for _factors

        Calculate the prime factorization of a number recursively.
        
        :param self: The object
        :param num: The number
        :type num: int
        :param primesBelow: The prime numbers less than or equal to the number
        :type primesBelow: list[int]
        :param factorization: The already calculated factors
        :type factorization: list[int]
        :return: The list of prime factors
        :rtype: list[int]
        """

        if primesBelow[-1] == num:
            factorization.append(num)
            return factorization
        else:
            for p in primesBelow:
                if num % p == 0:
                    factorization.append(p)
                    newNum = int(num / p)
                    return self._factors(newNum, self.sieve(newNum), factorization)
                
    def lcm(self, num1: int, num2: int) -> int:
        """
        Docstring for lcm

        Calculates the Least Common Multiple of two numbers.
        
        :param self: The object
        :param num1: The first number
        :type num1: int
        :param num2: The second number
        :type num2: int
        :return: The LCM of the numbers
        :rtype: int
        """

        # LCM = |num1 * num2| / GCD(num1, num2)
        return int(abs(num1 * num2) / self.gcd(num1, num2))
    
    def root(self, num: float, root: int) -> float:
        """
        Docstring for root

        Calculates the nth root of a number, where n is supplied by the user (root).
        
        :param self: The object
        :param num: The number
        :type num: float
        :param root: The root to calculate
        :type root: int
        :return: The rootth root of the number
        :rtype: float
        """

        return self._root(num, root, 0, num)
    
    def _root(self, num: float, root: int, low: float, high: float) -> float:
        """
        Docstring for _root

        Uses binary search to calculate the nth root of a number, where n is supplied by the user (root).
        
        :param self: The object
        :param num: The number
        :type num: float
        :param root: The root to calculate
        :type root: int
        :param low: The low end of the range
        :type low: float
        :param high: The high end of the range
        :type high: float
        :return: The rootth root of the number
        :rtype: float
        """
        
        mid = (low + high) / 2
        midToRoot = mid ** root
        if abs(midToRoot - num) < 1e-6: # Float math is not fully precise
            return mid
        elif midToRoot < num:
            return self._root(num, root, mid, high)
        else:
            return self._root(num, root, low, mid)
        
    def factorial(self, num: int) -> int:
        """
        Docstring for factorial

        Recursively calculates the factorial of any non-negative integer.
        
        :param self: The object
        :param num: The number
        :type num: int
        :return: The factorial of the number
        :rtype: int
        """

        if num < 0:
            raise ValueError("Cannot calculate factorial of a negative number.")
        if num == 0:
            if len(self.calculated_factorials) == 0:
                self.calculated_factorials.insert(num, 1)
            return 1
        else:
            if num >= len(self.calculated_factorials):
                self.calculated_factorials.insert(num, num * self.factorial(num - 1))
                return self.calculated_factorials[num]
            else:
                return self.calculated_factorials[num]