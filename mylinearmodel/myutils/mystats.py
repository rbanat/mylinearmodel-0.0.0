"""
    Un module avec des fonctions retournant des élements de statistiques.
"""


PI = 3.141592653589793
EXP = 2.718281828459045


def median(liste):
    """
        Retourne la médiane d'une liste.
    """
    liste_bis = sorted(liste)
    len_liste = len(liste_bis)
    if len_liste % 2 == 0:
        return (liste_bis[len_liste//2-1]+liste_bis[len_liste//2])/2
    return liste_bis[len_liste//2]


def first_quarter(liste):
    """
        Retourne le premier quartile d'une liste.
    """
    liste_bis = sorted(liste)
    len_liste = len(liste_bis)
    if (len_liste+3) % 4 == 0:
        return liste_bis[(len_liste+3)//4-1]
    return (liste_bis[(len_liste+3)//4-1]+liste_bis[(len_liste+3)//4]*3)/4


def third_quarter(liste):
    """
        Retourne le troisième quartile d'une liste.
    """
    liste_bis = sorted(liste)
    len_liste = len(liste_bis)
    if (3*len_liste+1) % 4 == 0:
        return liste_bis[(3*len_liste+1)//4-1]
    return (liste_bis[(3*len_liste+1)//4-1]*3+liste_bis[(3*len_liste+1)//4])/4


def factorielle(number):
    """
        Fonction factorielle.
    """
    if number in [0, 1]:
        return 1
    return number*factorielle(number-1)


def gamma(number):
    """
        Fonction gamma.
    """
    if number == 1:
        return 1
    if number == 1/2:
        return PI**(1/2)
    return (number-1)*gamma(number-1)


def beta(number_one, number_two):
    """
        Fonction beta.
    """
    return gamma(number_one)*gamma(number_two)/gamma(number_one+number_two)


def dunif(xobs, low, high):
    """
        Retourne la densité d'une loi uniforme.
    """
    if (xobs < low) or (xobs > high):
        return 0
    return 1/(high-low)


def dnorm(xobs, moy, var):
    """
        Retourne la densité d'une loi normale.
    """
    density = (1/(var*2*PI))**(1/2)
    exposant = -(1/(2*var))*((xobs-moy)**2)
    density *= (EXP**exposant)
    return density


def dkhi2(xobs, deg_lib):
    """
        Retourne la densité d'une loi du khi-deux.
    """
    if xobs <= 0:
        return 0

    density = xobs**(deg_lib/2 - 1)*EXP**(-xobs/2)
    density /= (2**(deg_lib/2)*gamma(deg_lib/2))
    return density


def dstud(xobs, deg_lib):
    """
        Retourne la densité d'une loi de student.
    """
    density = 1/((deg_lib*PI)**(1/2))
    density *= (1+((xobs**2)/deg_lib))**(-(deg_lib+1)/2)
    density *= gamma((deg_lib+1)/2)
    density /= gamma(deg_lib/2)
    return density


def dfish(xobs, df1, df2):
    """
        Retourne la densité d'une loi de fisher.
    """
    if xobs <= 0:
        return 0
    density = ((df1*xobs)**df1) * (df2**df2)
    density /= ((df1*xobs + df2)**(df1+df2))
    density = density**(1/2)
    density /= (xobs*beta(df1/2, df2/2))
    return density


def simulation_uniform(nb_sim, low, high):
    """
        Simule une loi uniforme.
    """
    pas = (high-low)/nb_sim
    xobs = [low + k*pas for k in range (0,nb_sim+1)]
    sim = []
    for elt in xobs:
        sim += [dunif(elt, low, high)]
    return xobs, sim


def simulation_normale(nb_sim, moy, var):
    """
        Simule une loi normale.
    """
    pas = 1000/nb_sim
    xobs = [-500 + moy + k*pas for k in range (0,nb_sim+1)]
    sim = []
    for elt in xobs:
        sim += [dnorm(elt, moy, var)]
    return xobs, sim


def simulation_khi2(nb_sim, deg_lib):
    """
        Simule une loi du khi-deux.
    """
    pas = 1000/nb_sim
    xobs = [k*pas for k in range (0,nb_sim+1)]
    sim = []
    for elt in xobs:
        sim += [dkhi2(elt, deg_lib)]
    return xobs, sim


def simulation_student(nb_sim, deg_lib):
    """
        Simule une loi de student.
    """
    pas = 1000/nb_sim
    xobs = [-500 + k*pas for k in range (0,nb_sim+1)]
    sim = []
    for elt in xobs:
        sim += [dstud(elt, deg_lib)]
    return xobs, sim


def simulation_fisher(nb_sim, df1, df2):
    """
        Simule une loi fisher.
    """
    pas = 100/nb_sim
    xobs = [k*pas for k in range (1,nb_sim+1)]
    sim = []
    for elt in xobs:
        sim += [dfish(elt, df1, df2)]
    return xobs, sim


def area(xdata,ydata):
    """
        Retourne l'aire d'une courbe.
    """
    aire = 0
    lim = len(xdata)-1
    for i in range (0,lim):
        aire += (xdata[i+1]-xdata[i])*ydata[i+1] - (xdata[i+1]-xdata[i])*(ydata[i+1]-ydata[i])/2
    return aire


def pnorm(stat, moy, var):
    """
        Retourne la p-valeur associée à une loi normale.
    """
    xnorm, ynorm = simulation_normale(100000, moy, var)
    len_sim = len(xnorm)
    for i in range (0,len_sim):
        if xnorm[i] >= stat:
            aire = area(xnorm[i:], ynorm[i:])
            return 2*aire
    return 2*area(xnorm[i:], ynorm[i:])


def pkhi2(stat, deg_lib):
    """
        Retourne la p-valeur associée à une loi du khi-deux.
    """
    xkhi2, ykhi2 = simulation_khi2(100000, deg_lib)
    len_sim = len(xkhi2)
    for i in range (0,len_sim):
        if xkhi2[i] >= stat:
            aire = area(xkhi2[i:], ykhi2[i:])
            return aire
    return area(xkhi2[i:], ykhi2[i:])

def pstud(stat, deg_lib):
    """
        Retourne la p-valeur associée à une loi de student.
    """
    if stat>0:
        return pstud(-stat,deg_lib)

    xstud, ystud = simulation_student(100000, deg_lib)
    len_sim = len(xstud)
    for i in range (0,len_sim):
        if xstud[i] > stat:
            aire = area(xstud[:i], ystud[:i])
            return 2*aire
    return 2*area(xstud[:i], ystud[:i])


def pfish(stat, df1, df2):
    """
        Retourne la p-valeur associée à une loi de fisher.
    """
    xfish, yfish = simulation_fisher(100000, df1, df2)
    len_sim = len(xfish)
    for i in range (0,len_sim):
        if xfish[i] >= stat:
            aire = 1 - area(xfish[:i], yfish[:i])
            return aire
    return 1 - area(xfish[:i], yfish[:i])


def qfish(df1, df2, alpha):
    """
        Retourne le quantile d'ordre alpha d'une loi de fisher.
    """
    xfish, yfish = simulation_fisher(100000, df1, df2)
    len_sim = len(xfish)
    for i in range (0,len_sim):
        aire = area(xfish[:i+1], yfish[:i+1])
        if aire >= alpha:
            return xfish[i]
    return xfish[i]
