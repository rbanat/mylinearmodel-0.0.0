"""
    Un module avec des fonctions de manipulation de fichiers et de dataframe.
"""


def is_num(string):
    """
        Vérifie si la variable string est numérique.
    """
    if string == '':
        return False
    return 48 <= ord(string[0]) & ord(string[0]) <= 57


def file_to_data(fichier, sep):
    """
        Retourne le jeu de données associé au fichier file.
    """
    with open(fichier, "r") as file_r:
        data = []
        for elt in file_r:
            temp = elt[:-1].split(sep)
            data += [temp]

    row = len(data)
    col = len(data[0])
    for i in range (0,row):
        for j in range (0,col):
            temp = data[i][j]
            if is_num(temp) :
                data[i][j] = float(temp)

    return data


def columns_name(data):
    """
        Retourne le nom des variables du jeu de données.
    """
    return data[0]


def get_index(data, list_name):
    """
        Retourne les indices des variables contenus dans la list_name.
    """
    if isinstance(list_name, str) :
        i = 0
        columns = columns_name(data)
        for elt in columns:
            if list_name == elt:
                return i
            i += 1
        return "Error : The variable is not in the data !"

    list_index = []
    len_list_name = len(list_name)
    for k in range (0,len_list_name):
        list_index += [get_index(data, list_name[k])]
    return list_index


def del_columns(data, list_name):
    """
        Supprime les variables contenu dans list_name du jeu de données initial.
    """
    if list_name == []:
        return "Error : The list must not be empty !"

    list_index = get_index(data, list_name)
    row = len(data)
    col = len(data[0])
    data_copy = [[] for k in range (0,row)]

    if isinstance(list_index, int) :
        for i in range (0,row):
            data_copy[i] = data[i][0:list_index] + data[i][list_index+1:]
        return data_copy

    for i in range (0,row):
        for j in range (0,col):
            if j not in list_index:
                data_copy[i] += [data[i][j]]

    return data_copy


def get_columns(data, list_name):
    """
        Retourne le jeu données avec seulement les variables de la liste list_name.
    """
    if list_name == []:
        return "Error : The list must not be empty !"

    list_index = get_index(data, list_name)
    row = len(data)
    data_copy = [[] for k in range (0,row)]

    if isinstance(list_index, int) :
        for i in range (0,row):
            data_copy[i] += [data[i][list_index]]
        return data_copy

    for i in range (0,row):
        for elt in list_index:
            data_copy[i] += [data[i][elt]]

    return data_copy


def split(data, y_var, percent):
    """
        Divise le jeu de données en un sous-ensemble train et un sous-ensemble test.
    """
    row = len(data)
    row_split = round(len(data)*percent)
    xtrain = data[0:row_split]
    xtest = data[row_split:]
    ytrain = [[0] for k in range (0,row_split)]
    ytest = [[0] for k in range (0,row-row_split)]

    index = get_index(data, y_var)
    for i in range (0,row_split):
        ytrain[i][0] = xtrain[i][index]
        del xtrain[i][index]

    for i in range (0,row-row_split):
        ytest[i][0] = xtest[i][index]
        del xtest[i][index]

    return (xtrain, ytrain, xtest, ytest)
