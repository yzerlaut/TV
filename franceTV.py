import sys, os
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

"""
iterate over all pages of a given video with:

    -  .../?page=0 
    -  .../?page=1
    -  .../?page=2

"""

def extract_infos(link, 
                  force_string='',
                  debug=False):

    titles = link.split('/')[-3:-1]
    if debug:
        print(titles)

    root_site = link[:31]
    if debug:
        print(root_site)

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
            if force_string in l:
                links.append(l)

        if (titles[0] in l):
            title = titles[0]
        else:
            title = titles[1]


    return title, links

def find_season_episodes(url):
    """ TO BE DONE """

    Links = []
    title, links = extract_infos(link+'/?page=%i' % i,
                                 debug=('debug' in sys.argv[-1]))
    print(links)
    

if __name__=='__main__':
    

    import argparse
    parser=argparse.ArgumentParser(description= """
        python franceTV.py URL --pages # to loop over the different pages
    """,
                                   formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("url")
    
    parser.add_argument('-s', "--string", 
                        help="force a string to be present in the downloaded urls",
                        type=str, default='')
    parser.add_argument("-p", "--pages", help="loop over pages",
                        action="store_true")
    parser.add_argument("-n", "--nPages", type=int, default=10)
    parser.add_argument("-d", "--debug",  action="store_true")
    args = parser.parse_args()

    link = sys.argv[1]

    if args.pages:
        # iterate over multiple pages
        Links = []
        for i in range(args.nPages):
            title, links = extract_infos(args.url+'/?page=%i' % i,
                                         force_string=args.string,
                                         debug=args.debug)
            Links += links
            print()
            print(i)
            print()
            print(links)

    else:

        title, Links = extract_infos(link,
                                     debug=args.debug)
        
    with open('list.txt', 'w') as f:
        for l in Links:
            f.write(l+'\n')
