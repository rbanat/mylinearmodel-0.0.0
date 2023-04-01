"""
    Un module qui teste les fonction du module my_stats.
"""


from myutils import mystats


liste1 = [1, 11, 15, 19, 20, 24, 28, 34, 37, 47, 50, 61, 68]
liste2 = [1, 11, 15, 19, 20, 24, 28, 34, 37, 47, 50, 61]

PI = 3.141592653589793
EXP = 2.718281828459045


def test_median():
    """
        Teste la fonction median.
    """
    assert mystats.median(liste1) == 28
    assert mystats.median(liste2) == 26


def test_first_quarter():
    """
        Teste la fonction first_quarter.
    """
    assert mystats.first_quarter(liste1) == 19
    assert mystats.first_quarter(liste2) == 18


def test_third_quarter():
    """
        Teste la fonction third_quarter.
    """
    assert mystats.third_quarter(liste1) == 47
    assert mystats.third_quarter(liste2) == 39.5


def test_factorielle():
    """
        Teste la fonction factorielle.
    """
    assert mystats.factorielle(0) == 1
    assert mystats.factorielle(1) == 1
    assert mystats.factorielle(4) == 24


def test_gamma():
    """
        Teste la fonction gamma.
    """
    assert mystats.gamma(1) == 1
    assert mystats.gamma(1/2) == PI**(1/2)


def test_beta():
    """
        Teste la fonction beta.
    """
    assert mystats.beta(1,1) == 1
    assert mystats.beta(1,1/2) == 2


def test_dunif():
    """
        Teste la fonction dunif.
    """
    assert mystats.dunif(-5, 0, 1) == 0
    assert mystats.dunif(1/2, 0, 1) == 1
    assert mystats.dunif(10, 0, 1) == 0


def test_dnorm():
    """
        Teste la fonction dnorm.
    """
    assert mystats.dnorm(0, 0, 1) == (1/(2*PI))**(1/2)
    assert mystats.dnorm(1, 0, 1) == (1/(2*PI*EXP))**(1/2)
    assert mystats.dnorm(-1, 0, 1) == (1/(2*PI*EXP))**(1/2)


def test_dkhi2():
    """
        Teste la fonction dkhi2.
    """
    assert mystats.dkhi2(0, 10) == 0
    assert mystats.dkhi2(-10, 40) == 0
    assert mystats.dkhi2(1, 2) == (EXP**(-1/2))/2


def test_dstud():
    """
        Teste la fonction dstud.
    """
    assert mystats.dstud(0, 1) == 1/PI
    assert mystats.dstud(-1, 1) == 1/(2*PI)
    assert mystats.dstud(1, 1) == 1/(2*PI)


def test_dfish():
    """
        Teste la fonction dfish.
    """
    assert mystats.dfish(1, 2, 2) == 1/4
    assert mystats.dfish(2, 2, 2) == (4**3/6**4)**(1/2)/2
    assert mystats.dfish(-10, 2, 2) == 0


def test_area():
    """
        Teste la fonction area.
    """
    assert mystats.area([0,1], [0,1]) == 1/2
    assert mystats.area([0,1], [0,-1]) == -1/2
    assert mystats.area([0,1,2], [0,1,0]) == 1


def test_pnorm():
    """
        Teste la fonction pnorm.
    """
    assert round(mystats.pnorm(0, 0, 1), 2) == 1.0
    assert round(mystats.pnorm(2.1, 0, 1), 2) == 0.04


def test_pkhi2():
    """
        Teste la fonction pkhi2.
    """
    assert round(mystats.pkhi2(12, 5), 2) == 0.03


def test_pstud():
    """
        Teste la fonction pstud.
    """
    assert round(mystats.pstud(0, 10), 2) == 1.0
    assert round(mystats.pstud(1.5, 10), 2) == 0.16


def test_pfish():
    """
        Teste la fonction pfish.
    """
    assert round(mystats.pfish(3.5, 4, 26), 2) == 0.02


def test_qfish():
    """
        Teste la fonction qfish.
    """
    assert round(mystats.qfish(4, 26, 0.95), 2) == 2.74
