#importing files from Folders
import os
doc=os.listdir("Family")
print(len(os.listdir("Family")))
for a in doc:
    a="Family/"+a
    f=open(a)
    #print(f.read())
    #os.path.join("Articles/",a)
    #print(a)
doc_fine=[]
for a in doc and i in range(4):
    doc_fine.append[i]=f.read("Family/"+a)
print(doc_fine[0])
    
