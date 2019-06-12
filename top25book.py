import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_html(url):
    resp = requests.get(url).text
    return resp


def all_page():
    base_url = 'https://book.douban.com/top250?start='
    urllist = []
    #only gather the first 25
    for page in range(0, 25, 25):
        allurl = base_url + str(page)
        urllist.append(allurl)
    return  urllist

def html_parse():
    for url in all_page():
        # BeautifulSoup
        soup = BeautifulSoup(get_html(url), 'html.parser')

        # Book names
        alldiv = soup.find_all('div', class_='pl2')
        names = [a.find('a')['title'] for a in alldiv]

        # Author
        allp = soup.find_all('p', class_='pl')
        authors_list = [p.get_text() for p in allp]
        #authors_list is included author, publication etc. we extract autuor information
        authors = [x.split('/')[0] for x in authors_list]

        # Rating
        starspan = soup.find_all('span', class_='rating_nums')
        scores = [s.get_text() for s in starspan]

        #No. of Rating
        #NumberofRating = soup.find_all('span', class_="pl")
        NumberofRating = soup.find_all(lambda tag: tag.name == 'span' and tag.get('class') == ['pl'])
        NumofRatings_list = [n.get_text() for n in NumberofRating]

        ##Extract numbers from the List
        NumofRatings = list(map(lambda sub:int(''.join([ele for ele in sub if ele.isnumeric()])), NumofRatings_list))


        # Introduction
        sumspan = soup.find_all('span', class_='inq')
        quotes = [i.get_text() for i in sumspan]


        ###DataFrame, and export to csv file
        info_table = pd.DataFrame({
        "Name": names,
        "Author": authors,
        "Rating": scores,
        "No. of People Rated": NumofRatings,
        "Quote": quotes
        })
        column_order = ['Name', 'Author', 'Rating', 'No. of People Rated', 'Quote']
        info_table[column_order].to_csv('Top25 Books.csv', index=False, sep=',', header=True, encoding='utf-8-sig')

        ##write data into text file
        for name, author, rating, NumofRating, quote in zip(names, authors, scores, NumofRatings, quotes):
            name = 'Name: ' + str(name) + '\n'
            author = 'Author: ' + str(author) + '\n'
            rating = 'Rating: ' + str(rating) + '\n'
            NumofRating = 'No. of People Rated: ' + str(NumofRating) + '\n'
            quote = 'Quote: ' + str(quote) + '\n'
            data = name + author + rating + NumofRating + quote
            # save the data
            f.writelines(data + '****************************************' + '\n')


filename = 'Top25 Books.txt'
f = open(filename, 'w', encoding='utf-8')

html_parse()
f.close()
print('successful')
