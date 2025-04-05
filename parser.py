from bs4 import BeautifulSoup
import requests
soup = BeautifulSoup()

# with open("https://news.ycombinator.com/") as file:
#     file = file.read()
# file = requests.get("https://news.ycombinator.com/")
# webpage = file.text 

# soup = BeautifulSoup(webpage , 'html.parser')
# print(soup)
# text = soup.select("tr td.title a ")[0].get('href')


# data =[item.get_text() for item in soup.find_all(name = 'span', class_='titleline')] 

# upvote = [int(score.get_text().split()[0]) for score in soup.find_all(name = 'span' , class_='score')]
# max_score = max(upvote)
# index_of_maxscore = upvote.index(max_score)
# print(upvote.index(max_score))
# print(data[index_of_maxscore])
# for index, i in enumerate(range(len(upvote))):
#     print(data[i].get_text())
#     print(upvote[i].get_text().split()[0])
#     highest_score.append()
#     print(data[i].find('a').get('href'))
# for i in data:
#     text = data[i].get_text()
#     print(text)

    
# article_text = soup.find(name = 'a', class_= "titleline")
# print(article_text.get_text())
# score = soup.find( name ='span' , class_= "score")

data = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

data = data.text
soup = BeautifulSoup(data , 'html.parser')

movies = soup.select('h2 strong' )

movie_list =[]
for i in range(len(movies)):
    
    movie_list.append(movies[i].get_text())

count = len(movies) -1

while count >=0:
    with open("movies.txt" ,'a') as file:
        file.write(f"{movie_list[count]}\n")
    
    count -=1