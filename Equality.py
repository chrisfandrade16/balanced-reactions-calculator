## @file Equality.py
#  @author Christopher Andrade
#  @brief A Python file containing a single class called "Equality"
#  @date Monday, February 3, 2020

from abc import abstractmethod


## @brief A class "Equality" that contains a single abstract method
#         "equals" to be defined in other classes
class Equality:
    ## @brief An abstract method "equals" that takes in one parameter
    #         "t" of different types, and will be defined in other classes
    #  @param t An input parameter of different types, depending on the class
    #           of which it is defined, and will be compared to the state variable(s)
    @abstractmethod
    def equals(self, t):

        pass
