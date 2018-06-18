
import json
d=json.load(open("data.json",'r'))
import difflib
from difflib import get_close_matches

def func(v):
    v=v.lower()
    if v in d:
        return d[v]

    else:

        s=get_close_matches(v,d.keys())
        if len(s)>0:
            k=input("The word doesnot exist.Are you looking for "+s[0]+" ? Y/N :")
            if k=='Y':
                return d[s[0]]
            elif k=='N':
                return("thanq")
            else:
                print("We couldn't get you")
        else:
            return ("No word similar to this exists")

in1=input("Enter the word: ")

h=func(in1)
if type(h)==list :
        #print("bitch")
        l=len(h)

        i=0
        while i<l:
            print("%d"%(i+1)+".>"+str((h)[i]))
            i=i+1
else:

    print(h)
