This is the README file for A0223846B and A0199384J's submission
Email(s): e0564887@u.nus.edu; e0406365@u.nus.edu


== Python Version ==

We're using Python Version 3.8.3 for this assignment.


== General Notes about this assignment ==
- Indexing -

The final format of each posting list is:
[Node1, Node2, Node2, …], where each Node contains a docID, the term frequency, and the term weight.

The dictionary in the TermDictionary object will be in the form of:
{term1: [docFrequency, pointer], term2: [docFrequency, pointer], ..., "c0rpu5D1r3ct0ry": [all docIDs]}

- Searching -

We preprocess terms in queries the same way we process words in the corpus. We do so in the CosineScores()
function, where we also calculate the score of the terms in the query compared to the corpus documents,
based on lnc.ltc (in terms of SMART notation of ddd.qqq). This means we determined the log tf and idf with
cosine normalisation for queries, and log tf, cosine normalisation, with no idf for documents. For each term,
we obtained this score and then summed the entire score for each document. We use a maximum heap to rank
the documents after determining the score due to the favourable efficiency of the data structure. Thereafter,
we output the top ten documents (ranked based on score) into the output document.


== Files included with this submission ==

README.txt - (this), general information about the submission.

index.py - main running code, indexes documents in the corpus into a postings file via SPIMI, and creates
a dictionary file.

search.py - main running code, searches for postings of terms based on queries and outputs the top ten
results, ranked by lnc.ltc, to a file.

Node.py - Node is a class that stores a docID, the term frequency, and the term weight.

SPIMI.py - implements SPIMI scalable index construction.

TermDictionary.py - the TermDictionary class, the main object type used to store term information: term,
its document frequency, and the pointer to fetch its postings in the postings file.

dictionary.txt - saved output of dictionary information of TermDictionary: contains terms, their document
frequency as well as their pointer.

postings.txt - saved output of list of Nodes, where each Node contains a docID, the term frequency, the
term weight, and the vector length.


== Statement of individual work ==

Please put a "x" (without the double quotes) into the bracket of the appropriate statement.

[x] We, A0223846B and A0199384J, certify that we have followed the CS 3245 Information Retrieval class
guidelines for homework assignments.  In particular, we expressly vow that we have followed the Facebook
rule in discussing with others in doing the assignment and did not take notes (digital or printed) from
the discussions.

[ ] I/We, A0000000X, did not follow the class rules regarding homework
assignment, because of the following reason:

<Please fill in>

We suggest that we should be graded as follows:

<Please fill in>


== References ==

Introduction To Information Retrieval - Cambridge University Press (textbook)
https://docs.python.org/3/library/heapq.html
https://realpython.com/python-counter/
https://twiserandom.com/python/__eq__-__ne__-__lt__-__gt__-__ge__-__le__-in-python-a-tutorial/index.html
