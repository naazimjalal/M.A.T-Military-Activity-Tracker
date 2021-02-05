import os.path
from functions import data1, scrapeImgs, newCrater, output, newCrate
d = newCrate()
d = str(d)
d = 'a = ', d
d = str(d)
d = d.replace('(', '', 10000000)
d = d.replace("'", "", 2)
d = d.replace(",", "", 1)
d = d.replace('"', "", 10000000)
d = d.replace("])", "]", 10000000)

b = data1("https://www.defensenews.com/home/", 'generic-results-list-main-wrapper')
b = str(b)
b = ' = ', b
b = str(b)
b = b.replace('(', '', 10000000)
b = b.replace("'", "", 2)
b = b.replace(",", "", 1)
b = b.replace('"', "", 10000000)
b = b.replace("])", "]", 10000000)

c = output() 
c = str(c)
c = ' = ', c
c = str(c)
c = c.replace('(', '', 10000000)
c = c.replace("'", "", 2)
c = c.replace(",", "", 1)
c = c.replace('"', "", 10000000)
c = c.replace("])", "]", 10000000)

img = []
for k in range(len(data1("https://www.defensenews.com/home/", 'generic-results-list-main-wrapper')[0])):
    if 'https' not in data1("https://www.defensenews.com/home/", 'generic-results-list-main-wrapper')[0][k]:
        data1("https://www.defensenews.com/home/", 'generic-results-list-main-wrapper')[0].pop(k)
        data1("https://www.defensenews.com/home/", 'generic-results-list-main-wrapper')[1].pop(k)
    rf = scrapeImgs(data1("https://www.defensenews.com/home/", 'generic-results-list-main-wrapper')[0][k], 1)
    img.append(rf)
for j in range(len(img)):
    if 'https' not in img[j]:
        img[j] = 'https://www.armytimes.com/'+img[j] 
img = str(img)
img = ' = ', img
img = str(img)
img = img.replace('(', '', 10000000)
img = img.replace("'", "", 2)
img = img.replace(",", "", 1)
img = img.replace('"', "", 10000000)
img = img.replace("])", "]", 10000000)


def begin():
    if os.path.isfile('backen.py'):
        print ("File exists")
        os.remove("backen.py")
        print("file removed")
    else:
        print ("File not found")
begin()
print("backend created")
file = open("backen.py","w") 
file.write(d)
file.write('\n\n')
file.write("b")
file.write(b)
file.write('\n\n')
file.write("c")
file.write(c)
file.write('\n\n')
file.write("img")
file.write(img)
file.close