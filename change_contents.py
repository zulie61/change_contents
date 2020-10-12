import os
import os.path
import xml.dom.minidom
path="**path**"  # C:\\Users\\Admin\\Desktop\\a_liang_photo\\ann
files=os.listdir(path)
#print(files[0])

for xmlFile in files:
    f = open(path+"\\"+xmlFile,"r")
    
    contents = f.read()
    if "liang" in contents:
        contents = contents.replace("**name1**","**name2**") # name1 -> name2
        
    with open(path+"\\"+xmlFile,"w") as f:
        f.write(contents)



