class Node(object):
    """
    Node is a class that stores a docID and a skip pointer to the next index to "skip" to.
    """

    def __init__(self, docID, termFrequency, vectorLength):
        self.docID = docID
        self.termFrequency = termFrequency
        self.vectorLength = vectorLength


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
        return "(" + str(self.docID) + ", " + str(self.termFrequency) + ", " + str(self.normWeight) + ")"


    def getDocID(self):
        return self.docID
