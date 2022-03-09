class Node(object):
    """
    Node is a class that stores a docID and a skip pointer to the next index to "skip" to.
    """

    def __init__(self, docID):
        self.docID = docID
        self.skipPointer = 0 # target index = skipPointer + currentIndex
        self.termFrequency = 0


    def addSkipPointer(self, value):
        """
        Adds a skip pointer to the Node
        """
        self.skipPointer = value


    def hasSkip(self):
        """
        Checks if the Node contains a skip pointer.
        """
        return self.skipPointer != 0


    def addTermFrequency(self, termFrequency):
        """
        Adds term frequency of a term in the document.
        """
        self.termFrequency = termFrequency 

    
    def getTermFrequency(self):
        return self.termFrequency


    def __str__(self):
        return str(self.docID)


    def __repr__(self):
        return "(" + str(self.docID) + ", " + str(self.termFrequency) + ", " + str(self.skipPointer) + ")"


    def getDocID(self):
        return self.docID
