from bs4 import BeautifulSoup
import requests

soup = BeautifulSoup()

# with open("https://news.ycombinator.com/") as file:
#     file = file.read()
file = requests.get("https://news.ycombinator.com/")
webpage = file.text 

soup = BeautifulSoup(webpage , 'html.parser')
# text = soup.select("tr td.title a ")[0].get('href')

text = soup.find(name = 'span', class_='titleline')
print(text)
    
# article_text = soup.find(name = 'a', class_= "titleline")
# print(article_text.get_text())
# score = soup.find( name ='span' , class_= "score")
