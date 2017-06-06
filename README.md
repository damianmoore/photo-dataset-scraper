# photo-dataset-scraper

Tools to create a labelled dataset of photos for deep learning image classification.

First install the Python required packages:

    pip install -r requirements.txt

You'll need a Flickr API key and secret that should be entered in `settings.py`.

Get the most "intersting" photos from Flickr and obtain the tags that were assigned to them. We'll keep track of how many times each tag was used and create a spreadsheet `tags.csv` of them all ordered by frequency.

    ./collect_tags.py
