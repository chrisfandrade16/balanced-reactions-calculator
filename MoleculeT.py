## @file MoleculeT.py
#  @author Christopher Andrade
#  @brief A Python file containing a single class called "MoleculeT"
#         that inherits two classes called "ChemEntity" and "Equality"
#  @date Monday, February 3, 2020

from ChemEntity import ChemEntity
from Equality import Equality
from ElmSet import ElmSet


## @brief A class "MoleculeT" inheriting class "ChemEntity" and class
#         "Equality" to create a chemical molecule type object from
#         a natural number and an "ElementT" object
class MoleculeT(ChemEntity, Equality):
    ## @brief A constructor that takes in two parameters "n" and "e" and
    #         creates a "MoleculeT" instance from them
    #  @param n An input parameter that is a natural number used to represent
    #           the number of atoms in the "MoleculeT" instance
    #  @param e An input parameter that is an "ElementT" object used to represent
    #           the element in the "MoleculeT" instance
    def __init__(self, n, e):

        self.__num = n
        self.__elm = e
    ## @brief A method "get_num" that returns a natural number representing the number
    #         of atoms in the "MoleculeT" instance
    #  @return Returns the state variable representing the number of atoms in the
    #          "MoleculeT" instance
    def get_num(self):

        return self.__num
    ## @brief A method "get_elm" that returns an "ElementT" object representing the
    #         element in the "MoleculeT" instance
    #  @return Returns the state variable representing the element, an "ElementT"
    #          object, in the "MoleculeT" instance
    def get_elm(self):

        return self.__elm
    ## @brief A method "num_atoms" that takes in one parameter "e" of type "ElementT"
    #         and will return a natural number
    #  @param e An input parameter of type "ElementT" to be compared to compared to the
    #           element in the "MoleculeT" instance
    #  @return Returns a natural number representing how many atoms of the input parameter
    #          "e", an "ElementT" object, are in the "MoleculeT" instance
    def num_atoms(self, e):

        if e == self.get_elm():
            return self.get_num()
        else:
            return 0
    ## @brief A method "constit_elems" that returns an "ElmSet" object
    #  @return Returns an "ElmSet" set object of "ElementT" objects that represents what
    #          elements the "MoleculeT" instance consists of
    def constit_elems(self):

        return ElmSet([self.get_elm()])
    ## @brief A method "equals" that takes in one parameter "m", a "MoleculeT" object,
    #          and checks if "m" has the same element and number of element as the
    #          "MoleculeT" instance
    #  @param m An input parameter that is a "MoleculeT" object and will
    #           be compared to the "MoleculeT" instance
    #  @return Returns a Boolean value True if the input parameter "m" has the
    #          same "ElementT" state variable and same number of elements state
    #          variable as the "MoleculeT" instance, otherwise returns False
    def equals(self, m):

        if (self.get_elm() == m.get_elm()) and (self.get_num() == m.get_num()):
            return True
        else:
            return False
