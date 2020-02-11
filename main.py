
from automates.AutomateDF import AutomateDF
""" Les tests de la classe AutomateDF"""
print("Les tests de la classe AutomateDF:")
def test_AutomateDF(mot="ab"):
    Automate = AutomateDF(mot)
    Automate.ajouter_etat("0")
    Automate.ajouter_etat("1", True)
    Automate.init = "0"
    Automate.ajouter_transition("0", "a", "1")
    Automate.ajouter_transition("0", "b", "0")
    Automate.ajouter_transition("1", "a", "1")
    Automate.ajouter_transition("1", "b", "1")
    print(Automate)
    return Automate
# tester les erreurs
def test_AutomateDFs_erreurs(Automate):
    Automate.ajouter_etat("0")
    Automate.dst_etat("0", "b")
    Automate.dst_etat("42", "b")
    Automate.ajouter_transition("0", "c", "w")
    Automate.ajouter_transition("0", "a", "w")
    Automate.ajouter_transition("0", "a", "0")

"""Tests de l'algorithme mot valide"""
def test_motValide():
    # initialiser l'Automate
    Automate = AutomateDF("ab")
    Automate.ajouter_etat("1")
    Automate.ajouter_etat("2")
    Automate.ajouter_etat("3")
    Automate.ajouter_etat("4", True)
    Automate.init = "0"
    Automate.ajouter_transition("0", "a", "1")
    Automate.ajouter_transition("0", "b", "0")
    Automate.ajouter_transition("1", "a", "2")
    Automate.ajouter_transition("1", "b", "0")
    Automate.ajouter_transition("2", "a", "2")
    Automate.ajouter_transition("2", "b", "3")
    Automate.ajouter_transition("3", "a", "4")
    Automate.ajouter_transition("3", "b", "0")
    Automate.ajouter_transition("4", "a", "4")
    Automate.ajouter_transition("4", "b", "4")
    print(Automate)
    # Tester si des mots est valider en utilisant motValid
    Automate.motValide("aaba")
    Automate.motValide( "abaa")
    Automate.motValide( "bababa")
    Automate.motValide( "aabaabaa", True)
    Automate.motValide( "bbababaabba", True)

if __name__ == '__main__':
    Automate= test_AutomateDF()
    test_AutomateDFs_erreurs(Automate)
    test_motValide()



