import requests
from bs4 import BeautifulSoup

URL = "https://www.imdb.com/search/title/?release_date=2018-01-01,2018-12-31&sort=num_votes,desc"

response = requests.get(URL)
web_site_html = response.text

soup = BeautifulSoup(web_site_html, "html.parser")

movie_websites = soup.prettify()

all_movies = soup.find_all(name="h3")

movies_list = []
for movie in all_movies:

    if all_movies[5] == movie:
        break
    movie_titles = movie.find('a')
    movies_list.append(movie_titles.getText())

run_times = soup.find_all(class_='runtime')
run_time_list = []
for run_time in run_times:
    time = run_time.getText()
    run_time_list.append(time)
    if run_times[5] == run_time:
        break

for i in range(len(movies_list)):
    print(f"{i+1}.{movies_list[i]}{run_time_list[i]} \n")
