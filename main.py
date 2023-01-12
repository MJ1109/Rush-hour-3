class Stack(object):
    """stack class. Waarin je items aan het einde van je stack kan zetten
    verwijderen"""
    def __init__(self):
        """ maakt een lege stack"""
        self.items = []

    def push(self, item):
        """zet items aan het einde van de stack"""
        return self.items.append(item)

    def pop(self):
        """ verwijderd items aan het einde van de stack"""
        return self.items.pop()

    def top(self):
        """ geeft het element aan de top van de stack zonder het te
        verwijderen"""
        return self.items[-1]

    def size(self):
        """ geeft het aantal elementen in de stack"""
        return len(self.items)

    def __repr__(self):
        return str(self.items)