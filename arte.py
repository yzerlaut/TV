import sys, os
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def extract_infos(link, debug=False):

    title = link.split('/')[-1]
    if debug:
        print(title)

    # root_site = link[:31]
    # if debug:
        # print(root_site)

    req = Request(link)
    html_page = urlopen(req)

    soup = BeautifulSoup(html_page, 'html.parser')
    
    links = []
    for Link in soup.findAll('a'):
        l = Link.get('href')
        if debug:
            print(l)
        if (title in l):
            if ('arte.tv' not in l):
                l = 'https://www.arte.tv'+l
            if debug:
                print('   -> selecting:', l)
            links.append(l)

    return title, links

def find_season_episodes(url):
    """ TO BE DONE """

    Links = []
    title, links = extract_infos(link+'/?page=%i' % i,
                                 debug=('debug' in sys.argv[-1]))
    print(links)
    

if __name__=='__main__':
    
    """
    python arte.py <URL> 

    Need to deal with pages
    """
    link = sys.argv[1]

    # if 'RC-' in link:
        # title, Links = extract_infos(link+'/?page=%i' % i,
                                     # debug=('debug' in sys.argv[-1]))
        # print(Links)

    # else:

    title, Links = extract_infos(link,
                                 debug=('debug' in sys.argv[-1]))
        
    
    with open('list.txt', 'w') as f:
        for l in Links:
            f.write(l+'\n')


