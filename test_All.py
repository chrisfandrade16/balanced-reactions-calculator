from ChemTypes import ElementT
from MolecSet import MolecSet
from Set import Set
from MoleculeT import MoleculeT
from CompoundT import CompoundT
from ReactionT import ReactionT
from pytest import raises


def test_set_add():

    addset = Set([0, 0, -2, -5, 28392, 9, 2, 2])
    addset.add(0)
    addset.add(1)
    assert addset.member(1), "Test Case Failed"
    assert addset.to_seq() == [0, -2, -5, 28392, 9, 2, 1], "Test Case Failed"
    assert addset.size() == 7, "Test Case Failed"


def test_set_rm():

    rmset = Set([1, 2, 1, 3, 2, 4, 5, -1])
    rmset.rm(1)
    rmset.rm(2)
    rmset.rm(3)
    rmset.rm(4)
    rmset.rm(5)
    assert rmset.to_seq() == [-1], "Test Case Failed"
    assert rmset.size() == 1, "Test Case Failed"
    assert rmset.member(5) is False, "Test Case Failed"
    assert rmset.member(-1), "Test Case Failed"
    with raises(ValueError) as excinfo:
        rmset.rm(6)
        assert "Test Case Failed" in str(excinfo.value)


def test_set_member():

    memberset = Set([-0, 0, 0, 0, 0, 1])
    assert memberset.member(-0), "Test Case Failed"
    assert memberset.member(+0), "Test Case Failed"
    assert memberset.member(1), "Test Case Failed"
    assert memberset.member(-1) is False, "Test Case Failed"


def test_set_size():

    sizeset = Set([])
    assert sizeset.size() == 0, "Test Case Failed"
    sizeset.add(100)
    sizeset.add(100)
    assert sizeset.size() == 1, "Test Case Failed"
    sizeset.rm(100)
    assert sizeset.size() == 0, "Test Case Failed"


def test_set_equals():

    equalsset1 = Set([100, 500, 2, 1, 5, 0, -1, 2000, 2000])
    equalsset2 = Set([0, 5, 1, 2, -1, 500, 100, 2000])
    assert equalsset1.equals(equalsset2), "Test Case Failed"
    equalsset1.rm(2000)
    equalsset2.rm(2000)
    equalsset1.add(-1)
    equalsset1.add(-1)
    assert equalsset1.equals(equalsset2), "Test Case Failed"
    equalsset1.add(101)
    assert equalsset1.equals(equalsset2) is False, "Test Case Failed"


def test_set_to_seq():

    toseqset = Set([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1])
    assert toseqset.to_seq() == [1, 2, 3, 4, 5], "Test Case Failed"
    toseqset.add(1)
    assert toseqset.to_seq() == [1, 2, 3, 4, 5], "Test Case Failed"


def test_moleculet_get_num():

    getnummolec1 = MoleculeT(-1, ElementT.H)
    getnummolec2 = MoleculeT(0, ElementT.P)
    getnummolec3 = MoleculeT(1, ElementT.Ti)
    assert getnummolec1.get_num() == -1, "Test Case Failed"
    assert getnummolec2.get_num() == 0, "Test Case Failed"
    assert getnummolec3.get_num() == 1, "Test Case Failed"


def test_moleculet_get_elm():

    getelmmolec1 = MoleculeT(31312, ElementT.Lv)
    getelmmolec2 = MoleculeT(7657324225, ElementT.Ts)
    getelmmolec3 = MoleculeT(5353536, ElementT.Og)
    assert getelmmolec1.get_elm() == ElementT.Lv, "Test Case Failed"
    assert getelmmolec2.get_elm() == ElementT.Ts, "Test Case Failed"
    assert getelmmolec3.get_elm() == ElementT.Og, "Test Case Failed"


def test_moleculet_num_atoms():

    numatomsmolec = MoleculeT(50 - 20 - 20 - 20 + 35, ElementT.Sg)
    assert numatomsmolec.num_atoms(ElementT.Sg) == 25, "Test Case Failed"
    assert numatomsmolec.num_atoms(ElementT.Sg) != 24, "Test Case Failed"
    assert numatomsmolec.num_atoms(ElementT.Bh) == 0, "Test Case Failed"


def test_moleculet_constit_elems():

    constitelemsmolec = MoleculeT(50, ElementT.Es)
    assert constitelemsmolec.constit_elems().to_seq() == [ElementT.Es], "Test Case Failed"


def test_moleculet_equals():

    equalsmolec1 = MoleculeT(0, ElementT.H)
    equalsmolec2 = MoleculeT(0, ElementT.H)
    equalsmolec3 = MoleculeT(1, ElementT.H)
    equalsmolec4 = MoleculeT(1, ElementT.He)
    assert equalsmolec1.equals(equalsmolec2), "Test Case Failed"
    assert equalsmolec2.equals(equalsmolec3) is False, "Test Case Failed"
    assert equalsmolec3.equals(equalsmolec4) is False, "Test Case Failed"


def test_compoundt_get_molec_set():

    gtmolsetcomp = CompoundT(MolecSet([MoleculeT(2, ElementT.H), MoleculeT(1, ElementT.C)]))
    temp = gtmolsetcomp.get_molec_set().to_seq()
    assert temp[0].equals(MoleculeT(2, ElementT.H)), "Test Case Failed"
    assert temp[1].equals(MoleculeT(1, ElementT.C)), "Test Case Failed"


def test_compoundt_num_atoms():

    numatomscomp = CompoundT(MolecSet([MoleculeT(2, ElementT.H), MoleculeT(1, ElementT.C)]))
    assert numatomscomp.num_atoms(ElementT.H) == 2, "Test Case Failed"
    assert numatomscomp.num_atoms(ElementT.C) == 1, "Test Case Failed"


def test_compoundt_constit_elems():

    conelmcmp = CompoundT(MolecSet([MoleculeT(2, ElementT.H), MoleculeT(1, ElementT.C)]))
    assert conelmcmp.constit_elems().to_seq() == [ElementT.H, ElementT.C], "Test Case Failed"


def test_compoundt_equals():

    equalscomp1 = CompoundT(MolecSet([MoleculeT(2, ElementT.H), MoleculeT(1, ElementT.C)]))
    equalscomp2 = CompoundT(MolecSet([MoleculeT(2, ElementT.H), MoleculeT(1, ElementT.C)]))
    equalscomp3 = CompoundT(MolecSet([MoleculeT(2, ElementT.C), MoleculeT(1, ElementT.C)]))
    assert equalscomp1.equals(equalscomp2), "Test Case Failed"
    assert equalscomp2.equals(equalscomp3) is False, "Test Case Failed"


def test_reactiont_get_lhs():

    hydrogen2 = MoleculeT(2, ElementT.H)
    hydrogen8 = MoleculeT(8, ElementT.H)
    carbon1 = MoleculeT(1, ElementT.C)
    carbon3 = MoleculeT(3, ElementT.C)
    oxygen1 = MoleculeT(1, ElementT.O)
    oxygen2 = MoleculeT(2, ElementT.O)

    propane = CompoundT(MolecSet([carbon3, hydrogen8, oxygen2]))
    oxygen = CompoundT(MolecSet([oxygen2]))
    water = CompoundT(MolecSet([hydrogen2, oxygen1]))
    carbdioxide = CompoundT(MolecSet([carbon1, oxygen2]))

    reaction = ReactionT([propane, oxygen], [water, carbdioxide])

    lhsresult = reaction.get_lhs()
    lhsexpected = [propane, oxygen]

    assert lhsresult[0].equals(lhsexpected[0]), "Test Case Failed"
    assert lhsresult[1].equals(lhsexpected[1]), "Test Case Failed"


def test_reactiont_get_rhs():

    hydrogen2 = MoleculeT(2, ElementT.H)
    hydrogen8 = MoleculeT(8, ElementT.H)
    carbon1 = MoleculeT(1, ElementT.C)
    carbon3 = MoleculeT(3, ElementT.C)
    oxygen1 = MoleculeT(1, ElementT.O)
    oxygen2 = MoleculeT(2, ElementT.O)

    propane = CompoundT(MolecSet([carbon3, hydrogen8, oxygen2]))
    oxygen = CompoundT(MolecSet([oxygen2]))
    water = CompoundT(MolecSet([hydrogen2, oxygen1]))
    carbdioxide = CompoundT(MolecSet([carbon1, oxygen2]))

    reaction = ReactionT([propane, oxygen], [water, carbdioxide])

    rhsresult = reaction.get_rhs()
    rhsexpected = [water, carbdioxide]

    assert rhsresult[0].equals(rhsexpected[0]), "Test Case Failed"
    assert rhsresult[1].equals(rhsexpected[1]), "Test Case Failed"


def test_reactiont_get_lhs_coeff():

    hydrogen1 = MoleculeT(1, ElementT.H)
    hydrogen2 = MoleculeT(2, ElementT.H)
    hydrogen3 = MoleculeT(3, ElementT.H)
    hydrogen4 = MoleculeT(4, ElementT.H)
    hydrogen8 = MoleculeT(8, ElementT.H)
    hydrogen12 = MoleculeT(12, ElementT.H)
    carbon1 = MoleculeT(1, ElementT.C)
    carbon3 = MoleculeT(3, ElementT.C)
    nitrogen1 = MoleculeT(1, ElementT.N)
    nitrogen2 = MoleculeT(2, ElementT.N)
    nitrogen3 = MoleculeT(3, ElementT.N)
    oxygen1 = MoleculeT(1, ElementT.O)
    oxygen2 = MoleculeT(2, ElementT.O)
    oxygen3 = MoleculeT(3, ElementT.O)
    oxygen4 = MoleculeT(4, ElementT.O)
    oxygen40 = MoleculeT(40, ElementT.O)
    phosphorus1 = MoleculeT(1, ElementT.P)
    mbdenum1 = MoleculeT(1, ElementT.Mo)
    mbdenum12 = MoleculeT(12, ElementT.Mo)

    propane = CompoundT(MolecSet([carbon3, hydrogen8]))
    oxygen = CompoundT(MolecSet([oxygen2]))
    water = CompoundT(MolecSet([hydrogen2, oxygen1]))
    carbdioxide = CompoundT(MolecSet([carbon1, oxygen2]))
    nitrdioxide = CompoundT(MolecSet([nitrogen1, oxygen2]))
    nitracid = CompoundT(MolecSet([hydrogen1, nitrogen1, oxygen3]))
    phosacid = CompoundT(MolecSet([hydrogen3, phosphorus1, oxygen4]))
    ammonorth = CompoundT(MolecSet([nitrogen2, hydrogen8, mbdenum1, oxygen4]))
    ammonphos = CompoundT(MolecSet([nitrogen3, hydrogen12, phosphorus1, oxygen40, mbdenum12]))
    ammonnitr = CompoundT(MolecSet([nitrogen2, hydrogen4, oxygen3]))

    reaction1 = ReactionT([propane, oxygen], [water, carbdioxide])
    reaction2 = ReactionT([phosacid, ammonorth, nitracid], [ammonphos, ammonnitr, water])

    assert reaction1.get_lhs_coeff() == [1, 5], "Test Case Failed"
    assert reaction2.get_lhs_coeff() == [1, 12, 21], "Test Case Failed"
    with raises(ValueError) as excinfo:
        reaction3 = ReactionT([water, nitrdioxide], [nitracid])
        reaction3.get_lhs_coeff()
        assert "Test Case Failed" in str(excinfo.value)


def test_reactiont_get_rhs_coeff():

    hydrogen1 = MoleculeT(1, ElementT.H)
    hydrogen2 = MoleculeT(2, ElementT.H)
    hydrogen3 = MoleculeT(3, ElementT.H)
    hydrogen4 = MoleculeT(4, ElementT.H)
    hydrogen8 = MoleculeT(8, ElementT.H)
    hydrogen12 = MoleculeT(12, ElementT.H)
    carbon1 = MoleculeT(1, ElementT.C)
    carbon3 = MoleculeT(3, ElementT.C)
    nitrogen1 = MoleculeT(1, ElementT.N)
    nitrogen2 = MoleculeT(2, ElementT.N)
    nitrogen3 = MoleculeT(3, ElementT.N)
    oxygen1 = MoleculeT(1, ElementT.O)
    oxygen2 = MoleculeT(2, ElementT.O)
    oxygen3 = MoleculeT(3, ElementT.O)
    oxygen4 = MoleculeT(4, ElementT.O)
    oxygen40 = MoleculeT(40, ElementT.O)
    phosphorus1 = MoleculeT(1, ElementT.P)
    mbdenum1 = MoleculeT(1, ElementT.Mo)
    mbdenum12 = MoleculeT(12, ElementT.Mo)

    propane = CompoundT(MolecSet([carbon3, hydrogen8, oxygen2]))
    oxygen = CompoundT(MolecSet([oxygen2]))
    water = CompoundT(MolecSet([hydrogen2, oxygen1]))
    carbdioxide = CompoundT(MolecSet([carbon1, oxygen2]))
    nitrdioxide = CompoundT(MolecSet([nitrogen1, oxygen2]))
    nitracid = CompoundT(MolecSet([hydrogen1, nitrogen1, oxygen3]))
    phosacid = CompoundT(MolecSet([hydrogen3, phosphorus1, oxygen4]))
    ammonorth = CompoundT(MolecSet([nitrogen2, hydrogen8, mbdenum1, oxygen4]))
    ammonphos = CompoundT(MolecSet([nitrogen3, hydrogen12, phosphorus1, oxygen40, mbdenum12]))
    ammonnitr = CompoundT(MolecSet([nitrogen2, hydrogen4, oxygen3]))

    reaction1 = ReactionT([propane, oxygen], [water, carbdioxide])
    reaction2 = ReactionT([phosacid, ammonorth, nitracid], [ammonphos, ammonnitr, water])

    assert reaction1.get_rhs_coeff() == [4, 3], "Test Case Failed"
    assert reaction2.get_rhs_coeff() == [1, 21, 12], "Test Case Failed"
    with raises(ValueError) as excinfo:
        reaction3 = ReactionT([water, nitrdioxide], [nitracid])
        reaction3.get_rhs_coeff()
        assert "Test Case Failed" in str(excinfo.value)
