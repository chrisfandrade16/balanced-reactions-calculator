## @file ChemEntity.py
#  @author Christopher Andrade
#  @brief A Python file containing a single class called "ChemEntity"
#  @date Monday, February 3, 2020

from abc import abstractmethod


## @brief A class "ChemEntity" that contains two abstract methods, "num_atoms" and
#         "constit_elems", to be defined in other classes
class ChemEntity:
    ## @brief An abstract method "num_atoms" that takes in one parameter "e"
    #         of type "ElementT" and will be defined in other classes
    #  @param e An input parameter of type "ElementT" to be compared to the state variable(s)
    @abstractmethod
    def num_atoms(self, e):

        pass
    ## @brief An abstract method "constit_elems" that will be defined in other classes
    @abstractmethod
    def constit_elems(self):

        pass
