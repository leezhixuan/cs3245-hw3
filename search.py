#!/usr/bin/python3
import re
import nltk
import sys
import getopt
import pickle
import math
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
            allResult = []
            for query in queryFile:
                queryVector = getQueryVector(query, dictFile, postings_file)
            outputResult = "\n".join(allResult)  # to output all result onto a new line.
            resultFile.write(outputResult)


def retrievePostingsList(file, pointer):
    """
    Given a pointer to determine the location in disk, 
    retrieves the postings list from that location.
    """
    if pointer == -1: # for non-existent terms
        return []

    with open(file, 'rb') as f:
        f.seek(pointer)
        postingsList = pickle.load(f)

    return postingsList


def getQueryVector(query, dictFile, postingsFile):
    tfidf_scores = []
    ltc_scores = []
    query = query.split(" ")
    queryTerms = set(query)
    for term in queryTerms:
        tfidf_scores.append(get_tf_idf(term, query, dictFile, postingsFile))  # get tf_idf weights according to queryTerms
    for score in tfidf_scores:
        ltc_scores.append(normalise(score, tfidf_scores))
    return ltc_scores


def get_tf_idf(term, query, dictFile, postingsFile):
    """
    gets the tf-idf weight of the term
    """
    tf = 0
    for word in query:
        if term == word:
            tf += 1
    tf_wt = 1 + math.log10(tf)  # get logarithmic tf

    pointer = dictFile.getTermPointer(term)
    postings = retrievePostingsList(postingsFile, pointer)
    docFreq = len(postings)
    corpusPointer = dictFile.getPointerToCorpusDocIDs()
    totalDocs = len(retrievePostingsList(postingsFile, corpusPointer))
    idf = math.log10(totalDocs/docFreq)     # get idf

    return tf_wt * idf


def normalise(tf_idf, scores):
    """
    returns normalised score
    """
    total = 0
    for score in scores:
        total += score**2
    result = math.sqrt(total)

    return 1/result * tf_idf


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
