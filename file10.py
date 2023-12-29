f=open("fruit.txt","r")
words=f.readlines()
for word in words:
    word=word.strip()
    if len(word)>=10:
        print(word.strip())

 
 
f.close()


