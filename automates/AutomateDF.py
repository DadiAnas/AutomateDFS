class AutomateDF:
    """ Cette classe représente tout type d'AutomateDF fini déterministe."""
    def __init__(self, alphabet):
        """ initialisation de l'Automate fini.
            @param l'alphabet de de l'automate."""

        """ Liste de chaîne correspondant au nom de l'état.
        Les États sont toujours identifiés par leur nom."""
        self.etats = []
        """ Dictionnaire utilisant l’état src comme clé et le mappant à une liste de
             paire (dest_etat, symbol)."""
        self.transitions = {}
        """ La chaîne correspondant au nom de l'état initial."""
        self.init = None
        """ Une liste contenant le nom des états finaux."""
        self.finals = []
        """ Une chaîne contenant tous les symboles de l'alphabet."""
        self.alphabet = ""
        for s in alphabet:
            if s not in self.alphabet:
                self.alphabet += s

    def ajouter_etat(self, etat, final=False):
        """ Ajouter un nouvel état. Erreur d'impression si l'état existe déjà.
            @param etat    le nom du nouvel état.
            @param final    un booléen déterminant si l'état est
                 final"""
        if etat in self.etats:
            print("erreur : etat '" + etat + "' existe deja.")
            return
        self.transitions[etat] = []
        self.etats.append(etat)
        if final:
            self.finals.append(etat)

    def valid_symbol(self, symbol):
        """ Renvoie True si le symbole fait partie de l'alphabet,
             false sinon.
            @param symbol the symbol to be tested """
        if symbol not in self.alphabet: return False
        return True

    def dst_etat(self, src_etat, symbol):
        """ Rechercher la transition correspondant à la source spécifiée etat
             et symbole et renvoie la destination etat. Si la transition ne
             n'existe pas, retourne None.
            @param src_etat the source etat of the transition.
            @param symbol the symbol of the transition. """
        if src_etat not in self.etats:
            print("erreur : l'etat '" + src_etat + "' n'est pas un état existant.")
            return
        for (s, dst_etat) in self.transitions[src_etat]:
            if s == symbol:
                return dst_etat
        return None

    def ajouter_transition(self, src_etat, symbol, dst_etat):
        """ Ajouter une transition à la FA. Ecrire erreur si l'Automate a déjà un
             transition pour l’état source spécifié et le symbole.
            @param src_etat le nom de l'état source.
            @param symbol le symbole de la transition.
            @param dst_etat le nom de l'état de destination."""
        if not self.valid_symbol(symbol):
            print("erreur : le symbole '" + symbol + "' ne fait pas partie de l'alphabet.")
            return
        if src_etat not in self.etats:
            print("erreur : l'etat '" + src_etat + "' n'est pas un état existant.")
            return
        if dst_etat not in self.etats:
            print("erreur : l'etat '" + dst_etat + "' n'est pas un état existant.")
            return

        if self.dst_etat(src_etat, symbol) != None:
            print("erreur : la transition (" + src_etat + ", " + symbol + ", ...) déjà existante.")
            return

        self.transitions[src_etat].append((symbol, dst_etat))

    def __str__(self):
        """Nous allons aussi surcharger __str__  de manière à avoir possibilité d’afficher nos Automates :"""
        ret =""
        ret += "Alphabet : '" + self.alphabet + "'\n"
        ret += "Init : " + str(self.init) + "\n"
        ret += "Finals : " + str(self.finals) + "\n"
        ret += "Etats (%d):\n" % (len(self.etats))
        for etat in self.etats:
            ret += "       - (%s)" % (etat)
            if len(self.transitions[etat]) is 0:
                ret += ".\n"
            else:
                ret += ret + ":\n"
                for (sym, dest) in self.transitions[etat]:
                    ret += ret + "    --(%s)--> (%s)\n" % (sym, dest)
        return ret

    def motValide(self, word, verbose=False):
        """ Exécute et renvoie True si le mot est
             accepté.
            @param word     le mot à tester.
            @param verbose  si True, plus d’informations sont affichées sur le
                 exécution.
            @return Vrai si le mot est accepté, Faux dans le cas contraire."""
        if self.init == None:
            print("erreur: l'self n'a pas de symbole initial.")
            return False
        current_etat = self.init
        i = 0
        for symbol in word:
            if verbose: print("configuration : (" + current_etat + ", " + word[i:] + ")")
            if not self.valid_symbol(symbol):
                print("error : le symbole '" + symbol + "' ne fait pas partie de l'alphabet. Abord.")

            next_etat = self.dst_etat(current_etat, symbol)
            if next_etat is None:
                if verbose: print("aucune transition disponible pour (" + current_etat + ", " + symbol + ").")
                return False;
            current_etat = next_etat
            i = i + 1
        if current_etat in self.finals:
            if verbose: print("se terminant sur l'etat final '" + current_etat + "'.")
            return True
        if verbose: print("se terminant sur un état non acceptant '" + current_etat + "'")
        return False