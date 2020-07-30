## @file ReactionT.py
#  @author Christopher Andrade
#  @brief A Python file containing a single class called "ReactionT"
#  @date Monday, February 3, 2020

from math import gcd
from sympy import Matrix


## @brief A class "ReactionT" to create a balanced chemical reaction
#         type object from a 2 sequences of "CompoundT" objects
class ReactionT:
    ## @brief A constructor that takes in two parameters "L" and "R"
    #         and creates a "ReactionT" instance from them
    #  @param L An input parameter that is a sequence of "CompoundT"
    #           objects on the left side of a desired chemical equation to be balanced
    #  @param R An input parameter that is a sequence of "CompoundT" objects on the right
    #           side of a desired chemical equation to be balanced
    #  @throw ValueError If the reaction cannot be balanced or the balanced coefficients are
    #                    equal or less than 0, a ValueError will be raised
    #  @details Will take two sequences of compounds, each representing a left and right side
    #           of a chemical equation, and will balance them (using a matrix) by solving the
    #           linear system of equations it represents, and will create 4 state variables, 2
    #           of which are simply the the input parameters, and the other 2 are sequences of
    #           real numbers consisting of the coefficients of each side of the equation after
    #           it is balanced, but it will raise a value error if the equation cannot be
    #           balanced
    #           with positive, non-zero coefficients
    def __init__(self, L, R):

        numofcompoundsleft = len(L)
        numofcompoundsright = len(R)
        numofcompoundstotal = numofcompoundsleft + numofcompoundsright

        elementstotal = []
        for k in L:
            for l in k.get_molec_set().to_seq():
                if l.get_elm() not in elementstotal:
                    elementstotal.append(l.get_elm())

        for m in R:
            for n in m.get_molec_set().to_seq():
                if n.get_elm() not in elementstotal:
                    elementstotal.append(n.get_elm())
        numofelementstotal = len(elementstotal)

        vectorsleft = []
        for i in range(numofcompoundsleft):
            vectorsleft.append([])
            for a in range(numofelementstotal):
                vectorsleft[i].append(0)

        vectorsright = []
        for j in range(numofcompoundsright):
            vectorsright.append([])
            for b in range(numofelementstotal):
                vectorsright[j].append(0)

        for o, p in zip(L, vectorsleft):
            for q in o.get_molec_set().to_seq():
                for r in range(numofelementstotal):
                    if q.get_elm() == elementstotal[r]:
                        index = r
                p[index] = q.get_num()

        for s, t in zip(R, vectorsright):
            for u in s.get_molec_set().to_seq():
                for v in range(numofelementstotal):
                    if u.get_elm() == elementstotal[v]:
                        index = v
                t[index] = -1 * u.get_num()

        vectorstotal = []
        vectorstotal.extend(vectorsleft)
        vectorstotal.extend(vectorsright)

        matrixnormal = Matrix(vectorstotal).T
        matrixtuple = matrixnormal.rref()
        matrixrref = matrixtuple[0]

        finalcolumn = matrixrref.col(-1)
        finalvalues = []
        finaldenominators = []

        for w in range(numofelementstotal):
            finalvalues.append(-1 * finalcolumn[w])
            finaldenominators.append(finalvalues[w].as_numer_denom()[1])

        if len(finalvalues) < numofcompoundstotal:
            for c in range(numofcompoundstotal - len(finalvalues)):
                finalvalues.append(1)
                finaldenominators.append(finalvalues[-1])

        leastcommonmultiple = finaldenominators[0]
        for itm in finaldenominators[1:]:
            leastcommonmultiple = (itm * leastcommonmultiple) / gcd(leastcommonmultiple, itm)

        coefficientsleft = []
        coefficientsright = []

        for x in range(numofcompoundstotal):
            finalvalues[x] = finalvalues[x] * leastcommonmultiple

        for y in range(numofcompoundsleft):
            coefficientsleft.append(finalvalues[y])

        for z in range(numofcompoundsleft, numofcompoundstotal):
            coefficientsright.append(finalvalues[z])

        for value in coefficientsleft:
            if value <= 0:
                raise ValueError

        for itm in coefficientsright:
            if itm <= 0:
                raise ValueError

        self.__lhs = L
        self.__rhs = R
        self.__coeffL = coefficientsleft
        self.__coeffR = coefficientsright
    ## @brief A method "get_lhs" that returns a sequence of "CompoundT" objects that
    #         represent a state variable of the "CompoundT" instance, specifically
    #         the first input parameter from the constructor, representing the left
    #         hand side of the chemical equation before it is balanced
    #  @return Returns a state variable, a sequence of "CompoundT" objects, representing
    #          the set of compounds from the left hand side of the chemical equation
    #          before it is balanced (the first input parameter in the constructor)
    def get_lhs(self):

        return self.__lhs
    ## @brief A method "get_rhs" that returns a sequence of "CompoundT" objects that
    #         represent a state variable of the "CompoundT" instance, specifically the
    #         second input parameter from the constructor, representing the right hand
    #         side of the chemical equation before it is balanced
    #  @return Returns a state variable, a sequence of "CompoundT" objects, representing
    #          the set of compounds from the right hand side of the chemical equation
    #          before it is balanced (the second input parameter in the constructor)
    def get_rhs(self):

        return self.__rhs
    ## @brief A method "get_lhs_coeff" that returns a sequence of real numbers
    #  @return Returns a sequence of real numbers representing the left hand
    #          side of coefficients after balancing the equation from the input
    #          parameters in the constructor
    def get_lhs_coeff(self):

        return self.__coeffL
    ## @brief A method "get_rhs_coeff" that returns a sequence of real numbers
    #  @return Returns a sequence of real numbers representing the right hand
    #          side of coefficients after balancing the equation from the input
    #          parameters in the constructor
    def get_rhs_coeff(self):

        return self.__coeffR
