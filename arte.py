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

    parser=argparse.ArgumentParser(description=
     """
     Launch the download of Arte Videos
     """
    ,formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('url', help="")

    parser.add_argument('-f', "--txt_file",
                        help="filename of files with the ARTE links",
                        default='arte.txt')

    parser.add_argument('-df', "--dest_folder",
                        help="destination folder", type=str,
                        default=os.path.join(os.path.expanduser('~'), 'Videos'))

    parser.add_argument('-q', "--quality",
                        help="""
                        quality of the videos in pixels, either:
                        384x216, 640x360, 768x432, 1280x720
                        """,
                        type=str, default='640x360')
    parser.add_argument('-LQ', '--low_quality', action="store_true")

    parser.add_argument("--languages",\
                        help="""
                        default language of the videos
                        in the order of preferences,
                        e.g. for a french speaker prefering french only
                        when original language was french otherwise vostfr,
                        pick: ['VO-STF', 'VF-STF']""",
                        nargs='+',
                        type=str,
                        default=['VO-STF', 'VOF', 'VOF-STF', 'VF-STF'])

    parser.add_argument('--cleanup', action="store_true",
                        help="do only the cleanup of residual movie files")
    parser.add_argument('-ncu', '--no_cleanup', action="store_true",
                        help="prevent cleanup of residual movie files")
    parser.add_argument('--debug', action="store_true",
                        help="prevent downloading")

    args = parser.parse_args()

    if args.low_quality:
        args.quality = '384x216'

    # if 'RC-' in link:
        # title, Links = extract_infos(link+'/?page=%i' % i,
                                     # debug=('debug' in sys.argv[-1]))
        # print(Links)

    # else:

    title, Links = extract_infos(link,
                                 debug=args.debug)
        


    python -m yt_dlp -a list.txt

    # with open('list.txt', 'w') as f:
        # for l in Links:
            # f.write(l+'\n')


