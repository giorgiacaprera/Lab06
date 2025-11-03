from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:
        """
            Funzione che legge tutte le automobili nel database
            :return: una lista con tutte le automobili presenti oppure None
        """

        # TODO
        try:
            query = 'SELECT * FROM automobile'
            result = self.db.esegui_query(query)
            automobili = [Automobile(*row) for row in result]
            return automobili
        except Exception as e:
            print(f'Errore durante la lettura delle automobili: {e}')
            return None

    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        # TODO
        try:
            query = ('SELECT * FROM automobile '
                     'WHERE modello LIKE %s')
            result = self.db.esegui_query(query, (f'%{modello}%',))
            automobili = [Automobile(*row) for row in result]
            return automobili
        except Exception as e:
            print(f'Errore durante la ricerca del modello: {e}')
            return None

