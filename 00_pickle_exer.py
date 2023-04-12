#request for getting the url
#pickle for convertin a url into a file and then load it 
import requests
import pickle
r=requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
# print(r)
l1=r.split("\n")
# print(l1)         #LIST

l2=[item.split(",") for item in l1 if len(item)!=0]
# print(l2)             #LIST OF LISTS

with open("014_iris.pickle.pkl","wb") as f:
    pickle.dump(l2,f)
with open("014_iris.pickle.pkl","rb") as f:
    print(pickle.load(f))
    




