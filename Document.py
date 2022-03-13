class Document(object):

    def __init__(self, docID, weight):
        self.docID = docID
        self.weight = weight

    def __repr__(self):
        return "[" + str(self.docID) + ", " + str(self.weight) + "]"

    def __str__(self):
        return str(self.docID)

    def __eq__(self, otherDoc):
        if isinstance(otherDoc, Document):
            return self.weight == otherDoc.weight

        return False

    def __ne__(self, otherDoc):
        if isinstance(otherDoc, Document):
            return self.weight != otherDoc.weight

        return False

    def __le__(self, otherDoc):
        if isinstance(otherDoc, Document):
            return self.weight <= otherDoc.weight

        return False

    def __ge__(self, otherDoc):
        if isinstance(otherDoc, Document):
            return self.weight >= otherDoc.weight

        return False 

    def __lt__(self, otherDoc):
        if isinstance(otherDoc, Document):
            return self.weight < otherDoc.weight

        return False

    def __gt__(self, otherDoc):
        if isinstance(otherDoc, Document):
            return self.weight > otherDoc.weight

        return False
