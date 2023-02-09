# Written without looking at the handout for Lecture 8, only the problem 
# statement in the slides.

import math

class Fraction():
    def __init__(self, num, denom):
        """
        num = integral numerator of the Fraction.
        denom = integral denominator of the Fraction.
        """
        # Added assertion after looking at handout
        assert type(num) == int and type(denom) == int, "Ints not used."
        self.num = num
        self.denom = denom
    def rationalize(self, other):
        """
        Rationalizes two Fractions (ie, makes their denoms equal)
        """
        new_denom = math.lcm(self.denom, other.denom)
        self.num *= new_denom // self.denom
        other.num *= new_denom // other.denom
        self.denom = new_denom
        other.denom = new_denom
    def simplify(self):
        """
        Simplifies/reduces a Fraction (ie, divides num and denom by their gcd)
        """
        g = math.gcd(self.num, self.denom)
        self.num = self.num // g
        self.denom = self.denom // g
    def __str__(self):
        """
        Returns the Fraction, expressed as a float
        """
        return str(self.num / self.denom)
    def __add__(self, other): # Changed to __add__ from simple add(self, other) 
        # after looking at handout
        """
        Adds two Fractions. Simplifies and returns the answer.
        """
        self.rationalize(other)
        ans = Fraction(self.num + other.num, self.denom)
        ans.simplify()
        return ans
    def __sub__(self, other):
        """
        Subtracts one Fraction from another. Simplifies and returns the answer.
        """
        self.rationalize(other)
        ans = Fraction(self.num - other.num, self.denom)
        ans.simplify()
        return ans
    def invert(self):
        """
        Returns the inverse of a Fraction.
        """
        self.simplify()
        # After looking at handout, changed from: 
        # self.num, self.denom = self.denom, self.num
        # to:
        return Fraction(self.denom, self.num)
