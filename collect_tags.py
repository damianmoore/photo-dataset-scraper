#!/usr/bin/env python
import argparse
from collections import defaultdict
import csv
import os

import flickrapi

from settings import FLICKR_API_KEY, FLICKR_API_SECRET


dirname = os.path.abspath(os.path.dirname(__file__))
training_dirname = os.path.join(dirname, 'data')

IMAGES_TO_COLLECT = 2000
IMAGES_PER_PAGE = 500


def make_csv(tags):
    with open('tags.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        for item in sorted(tags, key=tags.__getitem__, reverse=True):
            if tags[item] > 1:
                print('{} - {}'.format(item.encode('utf-8'), tags[item]))
                writer.writerow([item.encode('utf-8'), tags[item]])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Download a list of tags that are popular on Flickr')
    parser.add_argument(
        '-w', '--workers', type=int, default=-1,
        help="num workers used to download images. -x uses (all - x) cores [-1 default]."
    )

    args = parser.parse_args()

    flickr = flickrapi.FlickrAPI(FLICKR_API_KEY, FLICKR_API_SECRET, format='parsed-json')

    num_images = 0
    page = 1
    tags = defaultdict(int)

    while True:
        photos = flickr.photos.search(sort='interestingness-desc', per_page=IMAGES_PER_PAGE, page=page, content_type=1)['photos']['photo']

        for photo in photos:
            print(num_images)

            try:
                info = flickr.photos.getInfo(photo_id=photo.get('id'))
                num_images += 1
                for tag in info['photo']['tags']['tag']:
                    tags[tag['raw'].lower()] += 1

            except KeyboardInterrupt:
                print('\n{} tags\n'.format(len(tags)))
                make_csv(tags)
                exit(0)

            if num_images >= IMAGES_TO_COLLECT:
                break

        if num_images >= IMAGES_TO_COLLECT:
            break

        page += 1

    print('\n{} tags\n'.format(len(tags)))
    make_csv(tags)
