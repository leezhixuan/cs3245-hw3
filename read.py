import pickle

with open("dictionary.txt", "rb") as f:
    data = pickle.load(f)
    print(data)


with open ("postings.txt", "rb") as f:
    f.seek(25791616) # west
    # f.seek(15760068)
    postingsList = pickle.load(f)
    print(postingsList)