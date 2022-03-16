#!/usr/bin/python3
import nltk
import sys
import getopt
import pickle
import math
import heapq

from collections import Counter
from Document import Document
from TermDictionary import TermDictionary


def usage():
    print("usage: " + sys.argv[0] + " -d dictionary-file -p postings-file -q file-of-queries -o output-file-of-results")


def run_search(dict_file, postings_file, queries_file, results_file):
    """
    using the given dictionary file and postings file,
    perform searching on the given queries file and output the results to a file
    """
    print('running search on the queries...')

    dictFile = TermDictionary(dict_file)
    dictFile.load()  # load term information into dictFile from dict_file

    with open(queries_file, 'r') as queryFile:
        with open(results_file, 'w') as resultFile:
            
            for query in queryFile:
                result = cosineScores(query, dictFile, postings_file)
                resultFile.write(result + "\n")


def retrievePostingsList(file, pointer):
    """
    Given a pointer to determine the location in disk, 
    retrieves the postings list from that location.
    """
    if pointer == -1:  # for non-existent terms
        return []

    with open(file, 'rb') as f:
        f.seek(pointer)
        postingsList = pickle.load(f)

    return postingsList


# def getQueryVector(query, dictFile, postingsFile):
#     """
#     returns a vector of the ltc scores of each term
#     """
#     tfidf_scores = []
#     ltc_scores = []
#     queryTerms = []
#     stemmer = nltk.stem.porter.PorterStemmer()
#
#     query = nltk.tokenize.word_tokenize(query)
#     for term in query:
#         term = stemmer.stem(term.lower())
#         if term in queryTerms:
#             continue
#         else:
#             queryTerms.append(term)
#             tfidf_scores.append(get_tf_idf(term, query, dictFile, postingsFile))  # get tf_idf weights according to queryTerms
#     for score in tfidf_scores:
#         ltc_scores.append(normalise(score, tfidf_scores))
#
#     return ltc_scores
#
#
# def get_tf_idf(term, query, dictFile, postingsFile):
#     """
#     gets the tf-idf weight of the term
#     """
#     tf = 0
#     for word in query:
#         if term == word:
#             tf += 1
#     tf_wt = 1 + math.log10(tf)  # get logarithmic tf
#
#     pointer = dictFile.getTermPointer(term)
#     postings = retrievePostingsList(postingsFile, pointer)
#     docFreq = len(postings)
#     corpusPointer = dictFile.getPointerToCorpusDocIDs()
#     totalDocs = len(retrievePostingsList(postingsFile, corpusPointer))
#     idf = math.log10(totalDocs/docFreq)     # get idf
#
#     return tf_wt * idf
#
#
# def normalise(tf_idf, scores):
#     """
#     returns normalised score
#     """
#     total = 0
#     for score in scores:
#         total += score**2
#     result = math.sqrt(total)
#
#     return 1/result * tf_idf


def cosineScores(query, dictionary, postingsFile):
    """
    Implementation of CosineScore(q) from the textbook.
    """
    stemmer = nltk.stem.porter.PorterStemmer()
    totalNumberOfDocs = len(retrievePostingsList(postingsFile, dictionary.getPointerToDocLengths()))
    result = dict.fromkeys(retrievePostingsList(postingsFile, dictionary.getPointerToDocLengths()).keys(), 0) # in the form of {docID : 1, docID2 : 0.2, ...}

    queryTokens = [stemmer.stem(token.lower()) for token in query.split()]
    qTokenFrequency = Counter(queryTokens) # {"the": 2, "and" : 1}
    qToken_tfidfWeights = {term : computeTFIDF(term, frequency, dictionary, totalNumberOfDocs) for term, frequency in qTokenFrequency.items()}
    # print(qToken_tfidfWeights)
    queryLength = math.sqrt(sum([math.pow(weight, 2) for weight in qToken_tfidfWeights.values()]))
    qTokenNormalisedWeights = {term : weight/queryLength for term, weight in qToken_tfidfWeights.items()}

    for term in qTokenNormalisedWeights.keys():
        pointer = dictionary.getTermPointer(term)
        postings = retrievePostingsList(postingsFile, pointer) # in the form of (docID, TermFreq, skipPointer (to be discarded))

        for node in postings:
            docID = node.getDocID()
            termWeight = node.getTermWeight()
            docVectorLength = node.getVectorLength()
            result[docID] += qTokenNormalisedWeights[term] * (termWeight/ docVectorLength)
    
    # documents and their weights are now settled.

    documentObjects = generateDocumentObjects(result)

    output = heapq.nlargest(10, documentObjects)

    return " ".join([str(document) for document in output])


def computeTFIDF(term, frequency, dictionary, totalNumberOfDocs):
    df = dictionary.getTermDocFrequency(term)
    if (df == 0):
        return 0
    else:
        return (1 + math.log10(frequency)) * math.log10(totalNumberOfDocs/dictionary.getTermDocFrequency(term))


def generateDocumentObjects(result):
    output = []
    for docID, weight in result.items():
        output.append(Document(docID, weight))

    return output


dictionary_file = postings_file = file_of_queries = output_file_of_results = None

try:
    opts, args = getopt.getopt(sys.argv[1:], 'd:p:q:o:')
except getopt.GetoptError:
    usage()
    sys.exit(2)

for o, a in opts:
    if o == '-d':
        dictionary_file  = a
    elif o == '-p':
        postings_file = a
    elif o == '-q':
        file_of_queries = a
    elif o == '-o':
        file_of_output = a
    else:
        assert False, "unhandled option"

if dictionary_file == None or postings_file == None or file_of_queries == None or file_of_output == None :
    usage()
    sys.exit(2)

run_search(dictionary_file, postings_file, file_of_queries, file_of_output)
