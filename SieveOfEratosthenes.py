class SieveOfEratosthenes:

    """
    Docstring for SieveOfEratosthenes

    The Sieve of Eratosthenes was a concept where all numbers up to a certain point were written out,
    then prime numbers would be circled, and the multiples of that prime would be crossed out.
    """
    def __init__(self, limit: int):
        """
        Docstring for __init__

        Initializes the object with an int describing the highest number to check.
        Creates a list of numbers that range from 2 to that given number.

        :param self: The object
        :param limit (int): The highest number the program will check
        """

        self.limit = limit
        self.numbers = list(range(2, limit + 1))

    def sieve(self) -> list:
        """
        Docstring for sieve
        
        :param self: The object
        :return: A list of prime numbers up to the limit
        :rtype: list
        """

        primes = self.numbers.copy()
        for num in primes[:]:
            for candidate in range(num * 2, self.limit + 1, num):
                if candidate in primes:
                    primes.remove(candidate)

        return primes