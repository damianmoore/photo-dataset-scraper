#!/usr/bin/env python
import argparse
from collections import defaultdict
import csv
import hashlib
import multiprocessing
import os
import urllib

import flickrapi
from skimage import io

from settings import FLICKR_API_KEY, FLICKR_API_SECRET


MISSING_IMAGE_SHA1 = '6a92790b1c2a301c6e7ddef645dca1f53ea97ac2'
IMAGES_PER_TAG = 2000
IMAGES_PER_PAGE = 500

dirname = os.path.abspath(os.path.dirname(__file__))
training_dirname = os.path.join(dirname, 'data')


def download_image(args_tuple):
    "For use with multiprocessing map. Returns filename on fail."
    try:
        url, filename = args_tuple
        if not os.path.exists(filename):
            urllib.urlretrieve(url, filename)
        with open(filename) as f:
            assert hashlib.sha1(f.read()).hexdigest() != MISSING_IMAGE_SHA1
        io.imread(filename)  # Test read the image
        return True
    except KeyboardInterrupt:
        raise Exception()  # multiprocessing doesn't catch keyboard exceptions
    except:
        return False


def get_tags_from_csv():
    tags = []
    with open('tags.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            tags.append(row[0])
    return tags


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Download images from Flickr searches to labelled directory')
    parser.add_argument(
        '-i', '--images', type=int, default=-1,
        help="number of images to use (-1 for all [default])",
    )
    parser.add_argument(
        '-w', '--workers', type=int, default=-1,
        help="num workers used to download images. -x uses (all - x) cores [-1 default]."
    )
    parser.add_argument(
        '-l', '--labels', type=int, default=99999,
        help="if set to a positive value, only sample images from the first number of labels."
    )

    args = parser.parse_args()

    flickr = flickrapi.FlickrAPI(FLICKR_API_KEY, FLICKR_API_SECRET, format='parsed-json')

    urls = []
    page = 1
    tags = defaultdict(int)

    try:
        os.mkdir(training_dirname)
    except OSError:
        pass

    for tag in get_tags_from_csv()[:args.labels]:
        while True:
            photos = flickr.photos.search(sort='interestingness-desc', per_page=IMAGES_PER_PAGE, page=page, content_type=1, text=tag)['photos']['photo']

            for photo in photos:
                try:
                    os.mkdir(os.path.join(training_dirname, tag))
                except OSError:
                    pass
                url = 'https://farm{}.staticflickr.com/{}/{}_{}.jpg'.format(photo.get('farm'), photo.get('server'), photo.get('id'), photo.get('secret'))
                urls.append((url, os.path.join(training_dirname, tag, '{}.jpg'.format(photo.get('id')))))

                if len(urls) >= IMAGES_PER_TAG:
                    break

            if len(urls) >= IMAGES_PER_TAG:
                break
            page += 1

        num_workers = args.workers
        if num_workers <= 0:
            num_workers = multiprocessing.cpu_count() + num_workers

        print('Downloading {} images tagged as \'{}\' using {} workers...'.format(len(urls), tag, num_workers))
        pool = multiprocessing.Pool(processes=num_workers)
        map_args = urls
        results = pool.map(download_image, map_args)

        urls = []
        page = 1
