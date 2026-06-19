import requests

query=input("Enter the topic you want to search news about: ") 
api="2227a813ffc34fcfa449da04bd84511e"
url=f"https://newsapi.org/v2/everything?q={query}&from=2026-05-19&sortBy=publishedAt&apiKey={api}"


print(url)
c=requests.get(url)
data=c.json()
articles=data['articles']

for i, a in enumerate(articles):
    print(f"Article {i+1}:")
    print(a['title'])
    print(a['description'])
    print(a['url'])
    print("\n\n\n")