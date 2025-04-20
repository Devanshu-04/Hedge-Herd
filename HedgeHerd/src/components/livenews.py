import requests 


class newsHandler:  # Class to handle news data
    def __init__(self, key):  # Constructor to initialize the class
        self.key = key  # API key
        self.data = {}  # Dictionary to store news data

    def checkCat(self, cat):  # Method to check if the category is already in the data
        if cat in self.data:
            return True
        return False

    def getNews(self, cat):
        url = "https://finnhub.io/api/v1/news"
        p = {"category": cat, "token": self.key}
        r = requests.get(url, params=p)
        if r.status_code == 200:
            j = r.json()
            x = 1
            for a in j:
                a["id"] = x
                x += 1
            return j
        else:
            print("Error:", r.status_code)
            return None

    def save(self, cat, news):
        self.data[cat] = news
        print("Saved", len(news), "items for", cat)

    def findNews(self, id):
        for c, n in self.data.items():
            for a in n:
                if a["id"] == id:
                    return a
        return None

    def show(self, n):
        print("\nAll news")  # Print the news data
        for a in n[:5]:
            print("ID:", a['id'], "|", a['headline'], "|", a['source'])
            print("Link:", a['url'])

    def debugAll(self):
        print("\nDebugging all news")
        for c, n in self.data.items():
            print(c.upper())
            for a in n:
                print(">>", a["id"], "-", a["headline"])


class app:
    def __init__(self, k):
        self.n = newsHandler(k)

    def fetch(self, cat):
        if cat == "" or cat is None:
            print("Category is missing!")
            return
        if self.n.checkCat(cat):
            print("From local:", cat)
            n = self.n.data[cat]
        else:
            print("API call for:", cat)
            n = self.n.getNews(cat)
            if n is not None:
                self.n.save(cat, n)
            else:
                print("No data!")
                return
        self.n.show(n)

    def byId(self, id):
        a = self.n.findNews(id)
        if a:
            print("\nHere is the news:")
            print("ID:", a['id'], "->", a['headline'])
            print("Source:", a['source'])
            print("Link:", a['url'])
        else:
            print("No news for ID:", id)

'''
#Remove or comment out the following lines to prevent automatic execution:
k = "ct1nmb9r01qoprggpfk0ct1nmb9r01qoprggpfkg"
apifch = app(k)

print("\nFiltered General News")
apifch.fetch("general")

print("\nFiltered Stocks News")
apifch.fetch("stocks")

print("\nFetched News")
apifch.byId(3)
apifch.byId(50)
'''