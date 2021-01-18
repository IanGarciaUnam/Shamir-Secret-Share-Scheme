import random
import functools
import hashlib

from numpy.polynomial.polynomial import Polynomial as Poly
from Field import Field
import numpy.polynomial.polynomial as polynomial

class Polynomial():
    """
    A class used to apply Lagrange Interpolation method to find out secret

    Args:
        object ([type]): [description]
    """
    def __init__(self, prime_number, k, n, key):
        """
        Constructs Lagrange Polymial given a prime to use finite field arithmetic
        Args:
            prime_number (int): prime number to use finite field arithmetic
            k (int) : minimun number of shares to reconstruct the polynomial
            n (int) : number of shares to generate
            key (int) : secret to save
        """
        self.p = prime_number
        self.key = key
        self.partial_randomNumber = functools.partial(random.SystemRandom().randint, 0)
        self.k = k
        self.n = n
        self.polynomial = Poly(self.generate_random_poly())
        
        
    def generate_random_poly(self):
        """
        Generate a random polynomial

        Returns:
            list: List of coeficcients of a polynomial
        """
        poly = [self.partial_randomNumber(self.p - 1) for i in range(self.k)]
        
        poly[0] = self.key # Key
        
        return poly
    
        
    def generate_random_shares(self):
        """
        Generates random shares from our random polynomial

        Returns:
            list: A list of tuples (x,y), where x is the point, and y = P(x)
        """
        return [
            # We use % self.p below to take advantage of finite field arithmetic
            (x, polynomial.polyval(x, self.polynomial.coef) % self.p)
            for x in range(1, self.n + 1)
        ]
        
    def get_poly(self):
        """
        Return the random polynomial

        Returns:
            Polynomial: Random Polynomial
        """
        return self.polynomial
            

                
        



        