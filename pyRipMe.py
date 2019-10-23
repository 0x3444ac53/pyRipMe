import argparse
from urllib.parse import urlparse
import requests
from shutil import copyfileobj
import os
from scraperMaps import aMap
from fileMaps import extensionMap

def main():
    args = getArgs()
    scraper = find_scraper(args.url)
    links = scraper.scraper(args.url)
    name = scraper.get_name(args.url)
    path = make_download_dir(args.path, name)
    download_album(links, path)

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url')
    parser.add_argument('--path')
    return parser.parse_args()

def find_scraper(url):
    site_root = urlparse(url).hostname
    print(f'Getting scraper for {site_root}')
    return aMap[site_root]

def make_download_dir(path, name):
    name = name.replace(" ", "_")
    os.mkdir(f'{path}{name}')
    return path+name

def download_album(links : list, path : str):
    padding = len(str(len(links)))
    for i in range(len(links)):
        link = links[i]
        r = requests.get(link, stream=True)
        if r.status_code != 200:
            print(f'Status Code {r.status_code} on {link}')
            continue
        print(f'got {link}')
        extension = extensionMap[r.headers['content-type']]
        filename = f'{path}/{str(i + 1).zfill(padding)}.{extension}'
        with open(filename, 'wb') as f:
            r.raw.decode_content = True
            copyfileobj(r.raw, f)
        print(f'wrote to {filename}')

if __name__ == '__main__':
    main()
