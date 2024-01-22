import sys, os
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def extract_infos(link, debug=False):

    titles = link.split('/')[-3:-1]
    print(titles)
    root_site = link[:31]
    # print(root_site)

    req = Request(link)
    html_page = urlopen(req)

    soup = BeautifulSoup(html_page, 'html.parser')
    
    links = []
    for Link in soup.findAll('a'):
        l = Link.get('href')
        if debug:
            print(l)
        if ((titles[0] in l) or (titles[1] in l)) and ('.html' in l):
            if ('france.tv' not in l):
                l = 'https://www.france.tv'+l
            if debug:
                print('   -> selecting:', l)
            links.append(l)

        if (titles[0] in l):
            title = titles[0]
        else:
            title = titles[1]


    return title, links
    




if __name__=='__main__':
    
    link = sys.argv[1]

    title, links = extract_infos(link,
                                 debug=('debug' in sys.argv[-1]))

    with open('list.txt', 'w') as f:
        for l in links:
            f.write(l+'\n')


