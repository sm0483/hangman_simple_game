# connecting website and structuring html
from bs4 import BeautifulSoup
import requests
data=requests.get("https://www.hangmanwords.com/words").text
soup=BeautifulSoup(data,"lxml")
words=soup.find_all("li")
#writing to file
file=open("/home/user/Desktop/hungman/data.text","r+")
ls=[]
for word in words:
    #print(word.text)
    ls.append(word.text)
    if word.text=="zombie":
        break
print(ls) 

for word in ls:
    file.write(f"{word}\n")
file.close()    

