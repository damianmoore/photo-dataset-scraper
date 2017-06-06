# photo-dataset-scraper

Tools to create a labelled dataset of photos for deep learning image classification.


## Requirements

First install the Python required packages:

    pip install -r requirements.txt

You'll need a Flickr API key and secret that should be entered in `settings.py`.


## Identifying popular tags

We'll get the most "interesting" photos from Flickr and obtain the tags that were assigned to them. We keep track of how many times each tag was used and create a spreadsheet `tags.csv` of them all ordered by frequency.

    ./collect_tags.py

You'll want to refine this list of tags by deleting rows that are not suitable. Here are some types of tag I removed:

  * **Brands and models of camera** (don't really describe what's in the photo)
  * **Large geographic areas like countries and continents** (I think photos of these are too varied and overlap too much to be identifiable)
  * **Different languages** (you can do translation later on in UIs and search indexes - for now just use one language)
  * **Synonyms** (there's no need to collect duplicate data and have labels strongly competing with each other - we can store these to improve the search functionality when we build it later)
  * **Terms that are too broad**


## Downloading images

Next we download a set number of images for each of the tags in `tags.csv` and save them in labelled directories.

    ./download_tagged_images.py

**Warning:** You will be downloading lots of user-generated images that are very diverse. Because of this, there will undoubtably be some images that are unsuitable for children and unsuitable for work environments.


## Training

You may want to sort through and delete some of the collected images by hand to improve the accuracy of your training. I aim to build a web-based tool for doing this more quickly in future. You could also crowd-source this step using something like Amazon's Mechanical Turk.

Once you have built and refined your dataset you might want to use my simple wrapper for training an image classifier model: https://github.com/damianmoore/tensorflow-image-classifier
