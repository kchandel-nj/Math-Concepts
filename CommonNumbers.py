class CommonNumbers:
    """
    Docstring for CommonNumbers

    This class will provide functionality for finding numbers such as the
    Greatest Common Denominator or Least Common Multiple.
    """

    def __init__(self):
        """
        Docstring for __init__

        Prepares an object.

        :param self: The object
        """
        pass

    def gcd(self, num1: int, num2: int):
        """
        Docstring for gcd

        Finds the Greatest Common Denominator of two numbers using the Euclidean algorithm.
        
        :param self: The object
        :param num1: The first number
        :type num1: int
        :param num2: The second number
        :type num2: int
        """

        # num1 = num2 * (num1 / num2) + num1 % num2
        # num1 = num2 * _integerDivide(num1, num2) + _remainder(num1, num2)
        if num1 % num2 == 0:
            return num2
        elif num1 % num2 == 1:
            return 1
        else:
            return self.gcd(num2, num1 % num2)