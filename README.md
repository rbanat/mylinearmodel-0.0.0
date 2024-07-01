<font size=7> $\color{maroon}{Présentation \space générale}$ </font>

Le nom du package est **mylinearmodel**.

Ce package s'inscrit dans un projet de l'UE Python supervisé par Baptiste Gregorutti. Ce projet vise à appliquer les outils vus pendant le cours de "Modèles Linéaires"" dirigé par Charlotte Dion. 

<font size=3> $\color{orange}{Contraintes \space imposées :}$ </font>

- Les librairies **sklearn** et **statsmodels** sont proscrites. 
- les libraires **NumPy** et **Pandas** sont autorisées mais des points de bonus seront données si les outils implémentés ne les utilisent pas ou peu.
- Des tests unitaires devront être écrits exécutés avec **pytest**.
- La qualité du code devra être évaluée avec **pylint** et il faudra avoir une note au moins supérieure à 7/10.

Au sein de ce package, seule la librairie **matplotlib** a été utilisée. Des tests unitaires basiques ont été écrits pour chaque fonction. Chaque fichier .py a eu une note supérieur à 7/10 avec **pylint** avec la commande :
        
        pylint *.py */*.py */*/*.py --max-line-length=150

Les contraintes ont donc été respectées.

<font size=7> $\color{maroon}{Commandes}$ </font>

Décompresser le fichier **mylinearmodel-0.0.0.tar.gz**
    
        tar -xvzf mylinearmodel-0.0.0.tar.gz

Puis, se placer dans le dossier **mylinearmodel**

        cd mylinearmodel-0.0.0
    
Enfin, installer le package **mylinearmodel**
    
        python3 setup.py install


Pour lancer les tests unitaires

        pytest test

<font size=7> $\color{maroon}{Contenu \space du \space package}$ </font>

- Deux fichiers **setup.py** et **setup.cfg** : essentiels pour configurer et installer proprement le package **mylinearmodel**
- Ce fichier **README.md** : permet à l'utilisateur de comprendre le fonctionnement du package **mylinearmodel**
- Un fichier **fuel2001.txt** : jeu de données inclu dans le package permettant de tester toutes les fonctionnalités du package 
- Un package **mylinearmodel**
- Un package **test**

<font size=5> $\color{brown}{\hspace{3em} Le \space package \space \bf{mylinearmodel}}$ </font>

Ce package regroupe les différentes classe **LinearModel**, **OrdinaryLeastSquares** et **Ridge** respectueusement dans les fichiers lm.py, ols.py et ridge.py ainsi que le sous-package **myutils**.

Un fichier main.py est mis à disposition de l'utilisateur pour tester toutes les fonctionnalités du package avec la commande

        python3 mylinearmodel/main.py

<font size=4> $\color{orange}{1. \space La \space classe \space LinearModel}$ </font>

<font size=3> $\color{orange}{\hspace{3em} Les \space attributs}$ </font>
      
**fit_intercept** : *défaut=True*, nous révèle si le modèle admet une constante ou non

**type** : *défaut='Ridge'*, représente le type de modèle linéaire

**beta **: *défaut=0*, représente l'estimateur du modèle linéaire
      
**penalty** : *défaut=0*, représenta la constante de régularisation du modèle linéaire

**intercept** : *défaut=0*, représente la constante du modèle linéaire 
    
    
<font size=3> $\color{orange}{\hspace{3em} Les \space méthodes}$ </font> 
      
**__init__** : définit les attributs fit_intercept, type, beta, penalty, intercept

**get_coeffs** : prend en argument un object LinearModel et retourne l'attribut beta du modèle

**get_intercept** : prend en argument un object LinearModel et retourne l'attribut intercept du modèle

**predict** : prend en argument une matrice xtest et retourne la prédiction faite à partir de la matrice xtest

**get_residuals** : prend en argument deux matrices xtrain et ytrain et retourne les résidus du modèle

**ssr** : prend en argument deux matrices xtrain et ytrain et retourne la somme des carrés résiduels du modèle

**sst** : prend en argument une matrice ytrain et retourne la somme des carrés totale du modèle

**sse** : prend en argument deux matrices xtrain et ytrain et retourne la somme des carrés estimés du modèle

**determination_coefficient** : prend en argument deux matrices xtrain et ytrain et retourne le coefficient de détermination associé au modèle

**adjusted_determination_coefficient** : prend en argument deux matrices xtrain et ytrain et retourne le coefficient de détermination ajusté associé au modèle

**fisher_test** : prend en argument deux matrices xtrain et ytrain et retourne la F-statistique du modèle

**student_test** : prend en argument deux matrices xtrain et ytrain et une string var et retourne la t-statistique associé au modèle et à var
       
**plot_prediction** : prend en argument deux matrices xdata et ydata et retourne le graphe des mesures predites en fonction des mesures réelles
       
**summary** : prend en argument deux matrices xtrain et ytrain et retourne un résumé de toutes les données associées au modèle
             
<font size=4> $\color{orange}{2. \space La \space classe \space OrdinaryLeastSquares}$ </font> 

<font size=3> $\color{orange}{\hspace{3em} Les \space attributs}$ </font> 
             
**reprend tous les attributs de la classe LinearModel**
    
    
<font size=3> $\color{orange}{\hspace{3em} Les \space méthodes}$ </font>
             
**toutes les méthodes de la classe LinearModel**

**fit** : prend en argument deux matrices xtrain et ytrain, calcule l'intercept et l'estimateur des moindres carrés associé au model et retourne le model avec ses attributs changés
              
              
<font size=4> $\color{orange}{3. \space La \space classe \space Ridge}$ </font>

<font size=3> $\color{orange}{\hspace{3em} Les \space attributs}$ </font> 
             
**reprend tous les attributs de la classe LinearModel**
    
<font size=3> $\color{orange}{\hspace{3em} Les \space méthodes}$ </font>
             
**toutes les méthodes de la classe LinearModel**

**fit** : prend en argument deux matrices xtrain et ytrain, calcule l'intercept et l'estimateur de ridge associé au model et retourne le model avec ses attributs changés

<font size=5> $\color{brown}{\hspace{3em} Le \space package \space \bf{myutils}}$ </font>

Ce dossier implétement des outils nécessaires au bon fonctionnement du package. Il permet en particulier de créer des fonctions imitant certaines fonction des libraires pandas, et statsmodel. 

<font size=4> $\color{orange}{La \space classe \space Matrix \space du \space module \space matrix.py}$ </font>
        
<font size=3> $\color{orange}{\hspace{3em} Les \space attributs}$ </font> 

**data** : représente les données de la matrice
    
<font size=3> $\color{orange}{\hspace{3em} Les \space méthodes}$ </font>

**__init__ **: définit l'attribut data

**get_nb_row **: prend en argument un object Matrix et retourne son nombre de ligne

**get_nb_col** : prend en argument un object Matrix et retourne son nombre de colonne

**get_size** : prend en argument un object Matrix et retourne sa taille

**zeros** : prend en argument un couple (row, col) et retourne une matrice de taille (row, col) dont les termes sont tous nuls
                  
**ones** : prend en argument un couple (row, col) et retourne une matrice de taille (row, col) dont les termes sont tous égaux à 1
                  
**eye** : prend en argument un entier len_id et retourne la matrice identité de taille 1
                  
**copy** : prend en argument un object Matrix et retourne une copie de la matrice
                  
**is_square** : prend en argument un object Matrix et retourne si la matrice est carrée ou non
                  
**transpose** : prend en argument un object Matrix et renvoie sa transposée
                  
**sub_matrix_square** : prend en argument un object Matrix et deux indices i et j et retourne la sous-matrice d'indice i et j
                  
**cofactor** : prend en argument un object Matrix , et deux indices i et j et retourne le cofacteur d'indice i et j
                  
**determinant** : prend en argument un object Matrix et renvoie son determinant
                  
**comatrix** : prend en argument un object Matrix et retourne sa comatrice
                  
**inverse** : prend en argument un object Matrix et renvoie son inverse
                  
**add** : prend en argument deux objects Matrix et rtourne le somme
                  
**product** : prend en argument deux objects Matrix et retourne leur produit 

<font size=4> $\color{orange}{Le \space module \space mystats.py}$ </font>
        
**median** : prend en argument une liste et renvoie sa médiane

**first_quarter** : prend en argument une liste et renvoie son premier quartile

**third_quarter** : prend en argument une liste et renvoie son troisième quartile

**factorielle** : imite la fonction factorielle

**gamma** : imite la fonciton gamma
             
**beta** : imite la fonction beta
             
**dunif** : imite la densité d'une loi uniforme
             
**dnorm** : imite la densité d'une loi normale
             
**dkhi2** : imite la densité d'une loi khi-deux
             
**dstud** : imite la densité d'une loi de student
             
**dfish** : imite la densité d'une loi de fisher

**simulation_uniform** : simule une loi uniforme
             
**simulation_normale** : simule une loi normale
             
**simulation_khi2** : simule une loi khi-deux
             
**simulation_student** : simule une loi de student
             
**simulation_fisher** : simule une loi de fisher
             
**area** : prend en argument deux listes x et y, et retourne l'aire en dessous de la courbe y en fonction de x
             
**pnorm** : prend en argument une statistique de test d'une loi normale et retourne la p-valeur associée à cette statistique
             
**pkhi2** : prend en argument une statistique de test d'une loi khi-deux et retourne la p-valeur associée à cette statistique

**pstud** : prend en argument une statistique de test d'une loi de student et retourne la p-valeur associée à cette statistique
             
**pfish** : prend en argument une statistique de test d'une loi de fisher et retourne la p-valeur associée à cette statistique
             
**qfish** : prend en argument une F-statistique et retourne le quantile associé à cette statistique
                
<font size=4> $\color{orange}{Le \space module \space mypandas.py}$ </font>

**is_num** : prend en argument une string et retourne si son premier terme est numérique ou non

**file_to_data** : prend en argument un fichier .txt et retourne ses données sous forme de liste

**columns_name** : prend en argument des données, et retourne le nom des colonnes de ces données

**get_index** : prend en argument des données et une liste de string et retourne la liste d'indice associée à la liste de string

**del_columns** : prend en argument des données et une liste de string et supprime les colonnes contenue dans la liste de string

**get_columns** : prend en argument des données et une liste de string et retourne les données réduites dont les colonnes sont réduites à la liste de string

**split** : prend en argument un jeu de données, une string et une pourcentage et retourne le jeu de données en 4 sous jeu de données


<font size=5> $\color{brown}{Le \space package \space \bf{test}}$ </font>

Ce package testent les outils implémentés dans le dossier **mylinearmodel**. Des tests unitaires basiques ont été écrits pour chaque fonction. 

Pour tester les fonctions, taper la commande sur le terminale :

        pytest test
    
Cette commande permet de tester toutes les fonctions commençant par test_ contenues dans le dossier test/ et test/test_myutils/.
