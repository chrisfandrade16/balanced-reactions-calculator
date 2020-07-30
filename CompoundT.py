## @file CompoundT.py
#  @author Christopher Andrade
#  @brief A Python file containing a single class called "CompoundT"
#         that inherits two classes called "ChemEntity" and "Equality"
#  @date Monday, February 3, 2020

from ChemEntity import ChemEntity
from Equality import Equality
from ElmSet import ElmSet


## @brief A class "CompoundT" inheriting class "ChemEntity" and class
#         "Equality" to create a chemical compound type object from a "MolecSet" object
class CompoundT(ChemEntity, Equality):
    ## @brief A constructor that takes in one parameter "M" and creates a
    #         "CompoundT" instance
    #  @param M An input parameter that is a "MolecSet" object used to represent
    #           the molecules in the "CompoundT" instance
    def __init__(self, M):

        self.__C = M
    ## @brief A method "get_molec_set" that returns a "MolecSet" object that is
    #         the state variable of the "CompoundT" instance
    #  @return Returns the state variable, a "MolecSet" object, representing the
    #          set of molecules in the "CompoundT" instance
    def get_molec_set(self):

        return self.__C
    ## @brief A method "num_atoms" that takes in one parameter "e" of type "ElementT"
    #         and will return a natural number
    #  @param e An input parameter of type "ElementT" to be compared to compared to
    #           the elements in the "CompoundT" instance
    #  @return Returns a natural number representing how many atoms of the input parameter
    #          "e", an "ElementT" object, are in the "CompoundT" instance
    def num_atoms(self, e):

        atoms = 0
        for item in self.get_molec_set().to_seq():
            if e == item.get_elm():
                atoms += item.get_num()
        return atoms
    ## @brief A method "constit_elems" that returns an "ElmSet" object
    #  @return Returns an "ElmSet" set object of "ElementT" objects that represents what
    #          elements the "CompoundT" instance consists of
    def constit_elems(self):

        elements = ElmSet([])
        for item in self.get_molec_set().to_seq():
            elements.add(item.get_elm())
        return elements
    ## @brief A method "equals" that takes in one parameter "D", a "CompoundT" object, and
    #         checks if "D" is equal to the "CompoundT" instance using the "MoleculeT" class'
    #         "equals" method for each molecule in the compound
    #  @param D An input parameter that is a "CompoundT" object and will be compared
    #           to the "CompoundT" instance
    #  @return Returns a Boolean value True if the input parameter "D" is equal to
    #          the "CompoundT" instance using the "equals method" from the "MoleculeT"
    #          class for each molecule in the compound (so must have the same
    #          elements and number of elements), otherwise returns False
    def equals(self, D):

        if self.get_molec_set().size() != D.get_molec_set().size():
            return False
        for a, b in zip(self.get_molec_set().to_seq(), D.get_molec_set().to_seq()):
            if a.equals(b) is False:
                return False
        return True
