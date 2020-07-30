## @file Set.py
#  @author Christopher Andrade
#  @brief A Python file containing a single class called "Set"
#         that inherits another class called "Equality"
#  @date Monday, February 3, 2020

from Equality import Equality


## @brief A class "Set" inheriting class "Equality" to create
#         a set type object from a sequence
class Set(Equality):
    ## @brief A constructor that takes in one parameter "s"
    #         and creates a "Set" instance
    #  @param s An input parameter that is a sequence of different
    #           types, and will be transformed into a set
    def __init__(self, s):

        temp = []
        for item in s:
            if item not in temp:
                temp.append(item)
        self.__S = temp
    ## @brief A method "add" that takes in one parameter "e" of different
    #         types, and adds "e" to the "Set" instance if it is not already
    #         in the set, since sets do not contain duplicates by definition
    #  @param e An input parameter of different types that will be added to
    #           the "Set" instance
    def add(self, e):

        if self.member(e) is False:
            self.__S.append(e)
    ## @brief A method "rm" that takes in one parameter "e" of different types,
    #         and removes "e" from the "Set" instance if it exists in the set,
    #         otherwise a "ValueError" is raised
    #  @param e An input parameter of different types that will be removed from
    #           the "Set" instance
    #  @throws ValueError If input parameter "e" is not in the "Set" instance,
    #                     a ValueError will be raised
    def rm(self, e):

        if self.member(e) is True:
            self.__S.remove(e)
        else:
            raise ValueError
    ## @brief A method "member" that takes in one parameter "e" of different types,
    #         and checks if "e" is in the "Set" instance
    #  @param e An input parameter of different types that will be checked if it
    #           exists in the "Set" instance
    #  @return Returns a Boolean value True if the input parameter "e" exists in the
    #          set, otherwise returns Boolean value False
    def member(self, e):

        if e in self.__S:
            return True
        else:
            return False
    ## @brief A method "size" that calculates the size of the "Set" instance
    #  @return Returns a natural number value representing the size of the "Set" instance
    def size(self):

        return len(self.__S)
    ## @brief A method "equals" that takes in one parameter "R", a "Set" object,
    #         and checks if "R" has the same members as the "Set" instance in their set,
    #         and if they have the same size
    #  @param R An input parameter that is a "Set" object and will be
    #           compared to the "Set" instance
    #  @return Returns a Boolean value True if the input parameter "R" has the same
    #          members as the "Set" instance and have the same size set,
    #          otherwise returns False
    def equals(self, R):

        if self.size() != R.size():
            return False
        for item in R.to_seq():
            if self.member(item) is False:
                return False
        return True
    ## @brief A method "to_seq" that returns the sequence resulting from the
    #         transformation of the "Set" instance to a sequence
    #  @return Returns a sequence of different types that represents the
    #          "Set" instance as a sequence
    def to_seq(self):

        return self.__S
