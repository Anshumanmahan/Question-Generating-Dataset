from bs4 import BeautifulSoup
import urllib.request
import sys
str = sys.argv[1] #my_url
print(str)
source = urllib.request.urlopen(str)
soup = BeautifulSoup(source,'html.parser')
x = soup.find_all(class_='module-content')
for para in soup.find("h1"):
    header = para.get_text()

for para in soup.find("p"):
    paragraph = para.get_text()

header = header.strip()
paragraph = paragraph.strip()
content = header + '\n' +paragraph
text_file = open("description.txt", "wt")
n = text_file.write(content)
text_file.close()