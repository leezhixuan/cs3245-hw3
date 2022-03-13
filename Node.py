class Node(object):
    """
    Node is a class that stores a docID and a skip pointer to the next index to "skip" to.
    """

    def __init__(self, docID, termFrequency, termWeight, vectorLength):
        self.docID = docID
        self.termFrequency = termFrequency
        self.termWeight = termWeight
        self.vectorLength = vectorLength

    
    def getTermFrequency(self):
        return self.termFrequency


    def getTermWeight(self):
        return self.termWeight


    def getVectorLength(self):
        return self.vectorLength


    def __str__(self):
        return str(self.docID)


    def __repr__(self):
        return "(" + str(self.docID) + ", " + str(self.termFrequency) + ", " + str(self.normWeight) + ")"


    def getDocID(self):
        return self.docID
