This is the README file for A0223846B and A0199384J's submission
Email(s): e0564887@u.nus.edu; e0406365@u.nus.edu


== Python Version ==

We're using Python Version 3.8.3 for this assignment.


== General Notes about this assignment ==
- Indexing -

We modified the SPIMI method of indexing terms in the corpus. Like in HW2, a temporary working directory is 
specially set up to store intermediate files during the SPIMI process. The maximum number of files that we 
process before making the calling SPIMIInvert() is 1024. For every document in the corpus, we make a call 
to generateTokenStreamWithVectorLength(). In this method, we keep a counter for every term encountered as well 
as stem and apply case-folding to every term. We also calculate their weights using 1 + log10(termFrequency), 
without idf. By determining the weights of each term in the document, we can calculate the vector length of 
the document. In the end, we will be able to output a tuple of 2 elements: the first being a tuple of term, docID, 
weight,lengthOfDocVector and the second being the length of the document.

After all the documents in the corpus have been processed. We make a call to binaryMerge() and it is in charge of 
merging all the existing "dictionary" and "postings" files that have been created into a single "dictionary" and 
"postings" file. 

Next, we convert all postings into Nodes objects to store information neatly. We store these Node objects 
into the "out_postings" file.

Finally, we load the TermDictionary up so that we can add a pointer that points to the dictionary which stores the 
length of all documents in the corpus. We then save the information in TermDictionary onto the disk. At this point, 
we delete the temporary file that was used to store postings, as well as the temporary directory used by the SPIMI process.

The final format of each postings list is:
[Node1, Node2, Node2, …], where each Node contains a docID, the term frequency in document <docID>, 
the term weight, and the vector length of document <docID>.

The dictionary in the TermDictionary object will be in the form of:
{term: [docFrequency, pointer], term2: [docFrequency, pointer], ..., "d0cum3ntL3ngth": pointer}

- Searching -

We preprocess terms in queries the same way we preprocess words in the corpus (only stemming and case-folding) so that we
will be able to search effectively. In CosineScores(), we also calculate score of each document based on lnc.ltc 
(in terms of SMART notation of ddd.qqq). As such, weights of query terms are determined using (1 + log10(tf)) * idf, with cosine normalisation.
For each query term, we add (QueryTermWeight * DocumentTermWeight) / docVectorLength to the score of every document in its postings list. 
At the end, every document would have obtained a score. The higher the score, the more relevant that particular document is to the query.

In order to rank and output the top 10 most relevant documents to the query, we utilise the heapq library as well as the Document class.
The Document class helps to facilitate ranking. As such, we convert every document-score pair into Document objects and pass the array
of Document objects into heapq.extract10(). Then, we filter away any document with a score = 0 that somehow managed to make it into the top 10.
Thereafter, we write the top 10 results (if any) into the output file, each on a new line.


== Files included with this submission ==

README.txt - (this), general information about the submission.

index.py - main running code, indexes documents in the corpus into a postings file via SPIMI, and creates
a dictionary file.

search.py - main running code, searches for postings of terms based on queries and outputs the top ten (or less)
results, ranked by lnc.ltc, to a file.

Node.py - Node is a class that stores a docID, the term frequency in document <docID>, the term weight, 
and the vector length of document <docID>.

SPIMI.py - implements SPIMI scalable index construction.

TermDictionary.py - the TermDictionary class, the main object type used to store term information: term,
its document frequency, and the pointer to fetch its postings in the postings file.

dictionary.txt - saved output of dictionary information of TermDictionary: contains terms, their document
frequency as well as their pointer. It also contains a special key, "d0cum3ntL3ngth", whose value is a pointer to 
a dictionary whose key-value pair is docID : docLength.

postings.txt - saved output of list of Nodes objects, as well as a dictionary whose key-pair value is docID : docLength.


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
