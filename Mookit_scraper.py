from bs4 import BeautifulSoup
import re
import csv


with open("ESC201A.html", "r", encoding="utf8") as html_file:
    soup=BeautifulSoup(html_file, "lxml")

count=0
for lectures in soup.find_all("div", class_="lectureInfoBoxText"):
    count=count+1
# print(count)

n=input("Input the number of latest lectures to view: ")
if(int(n)>count):
    print("Number of lectures entered outnumbers the total lectures")
    exit()

csv_file=open("Mookit_scraper.csv", "w")
csv_writer=csv.writer(csv_file)
csv_writer.writerow(["Week", "Lecture name"])

lecs=0

for match in soup.find_all("div", class_=["weekWrapper","lectureInfoBoxText"]):
    txt=match.text.strip()
    x=re.split("\n", txt)
    # print(x)
    
    if re.findall("^Week", x[0]):
         week=x[0]
    else:
        if count-lecs>int(n): 
            lecs=lecs+1
            # print(week+" "+str(lecs)+" "+str(count))
            continue
        else:
            lecture=x[0]
            print(week+" "+lecture)
            lecs=lecs+1
            csv_writer.writerow([week, lecture])
    
