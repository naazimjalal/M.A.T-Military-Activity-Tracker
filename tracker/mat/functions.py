import requests
from bs4 import BeautifulSoup
import re
 
 
def scrapeImgs(link, index):
    im = []
    im_url =  link
    im_page = requests.get(im_url)
    im_soup = BeautifulSoup(im_page.content, 'html.parser')
    imgs = im_soup.find_all('img',{"src":True})
    for img in imgs:
        im.append(img['src'])
    return im[index]

def linktotext(link, n):
    links = link
    links = links[n:]
    links = links.replace('_', ' ')
    links = links.replace('-', ' ')
    links = links.replace('/articleshow/', '')
    links = links.replace('.cms', '')    
    return links

def output():
  b = [[], [], []]
  url = "https://www.aljazeera.com/tag/military/"
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  text = soup.find(class_= "l-col l-col--8")#top-newslist clearfix
  for link in text.findAll('a', attrs={'href': re.compile("^/")}):
    href = link.get('href')
    fl = url+href
    fl = fl.replace('military//', 'military/')
    b[0].append(fl)
  for i in range(len(b[0])):
    b[1].append(linktotext(b[0][i], 52))
    A = "https://www.aljazeera.com"+ scrapeImgs(b[0][i], 0)
    b[2].append(A)
  return b

def data(link, id):
    key = id
    data = [[], []]
    url = link
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = soup.find(class_= key)#top-newslist clearfix
    ne = text.find_all(text=True)
    for link in text.findAll('a', attrs={'href': re.compile("^/")}):
        href = link.get('href')
        fl = url+href
        data[0].append(fl)
    for i in range(len(ne)):
        data[1].append(ne[i])
    return data
def crate():
    countries = ['pakistan', 'china', 'us']
    unfiltered = []
    for i in range(len(countries)):
            raw_data = data("https://timesofindia.indiatimes.com/world/"+countries[i], "list5 clearfix")
            unfiltered.append(raw_data)
    return unfiltered
def data1(link, id):
    key = id
    data = [[], []]
    url = link
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = soup.find(class_= key)#top-newslist clearfix
    ne = text.find_all('h4')
    for link in text.findAll('a'):
        href = link.get('href')
        if href not in data[0]:
            data[0].append(href)        
    for i in range(len(ne)):
        data[1].append(str(ne[i].text))
    return data 
def scrapeImgsr(link, index):
    im = []
    im_url =  link
    im_page = requests.get(im_url)
    im_soup = BeautifulSoup(im_page.content, 'html.parser')
    imgs = im_soup.find_all('img',{"src":True})
    for img in imgs:
        im.append(img['src'])
    return im[index]
def dataw(link, id):
    key = id
    data = [[], []]
    url = link
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = soup.find(class_= key)#top-newslist clearfix
    for link in text.findAll('a', attrs={'href': re.compile("^/")}):
        href = link.get('href')
        fl = url+href
        data[0].append(fl)
    return data

def newCrate():
    crate = [[], [], []]
    r = dataw("https://www.defenseworld.net/allnews", 'col-md-13 col-lg-13')
    #if "allnews" in r[0]:
    for i in range(len(r[0])):
        if "allnews" in r[0][i]:
            r[0][i] = r[0][i].replace('allnews/','')
            crate[0].append(r[0][i])
            jp = scrapeImgsr(r[0][i], 0)
            crate[1].append(jp)
            crate[2].append(linktotext(r[0][i], 40))
    return crate
def newCrater():
    crate = [[], [], []]
    r = dataw("https://www.scmp.com/topics/china-military", 'article-area')
    #if "allnews" in r[0]:
    for i in range(len(r[0])):
        if "topics/china-military/" in r[0][i]:
            r[0][i] = r[0][i].replace('topics/china-military/','')
            crate[0].append(r[0][i])
            jp = scrapeImgsr(r[0][i], 0)
            jp = jp.replace('64x64', '1200x800')
            crate[1].append(jp)
            crate[2].append(linktotext(r[0][i], 50))
    return crate
 