import pickle

with open("dictionary.txt", "rb") as f:
    data = pickle.load(f)
    print(data)


with open ("postings.txt", "rb") as f:
    f.seek(14963957) # want
    postingsList = pickle.load(f)
    print(postingsList)