import csv
import json
import os

from channels import Channel, Group
from django.conf import settings


def notify_ui(type, data, channel_name=None):
    content = {
        'text': json.dumps({
            type: data
            # TODO: Include timestamp/counter to prevent out of order transmission causing state inconsistencies
        })
    }

    if channel_name:
        Channel(channel_name).send(content, immediately=True)
    else:
        Group('ui').send(content, immediately=True)


def get_datasets():
    datasets = []
    for root, dirs, files in os.walk(settings.DATASET_DIR):
        for name in dirs:
            if name not in ['bottlenecks', 'inception', 'training_summaries']:
                labels = get_labels(name)
                datasets.append({
                    'name': name,
                    'labels': labels,
                    'intended_num_images': len(labels) * 2000,
                    'num_images': sum([label['num_images'] for label in labels]),
                    'num_bottlenecks': sum([label['num_bottlenecks'] for label in labels]),
                })
        break
    return datasets


def get_labels(dataset):
    labels = []
    path = os.path.join(settings.DATASET_DIR, dataset, 'labels.csv')
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            label = row[0]
            images = get_images(dataset, label)
            bottlenecks = get_bottlenecks(dataset, label)
            labels.append({
                'name': label,
                'intended_num_images': 2000,
                'num_images': len(images),
                'num_bottlenecks': len(set(images).intersection(bottlenecks)),
            })
    return labels


def get_images(dataset, label):
    path = os.path.normpath(os.path.join(settings.DATASET_DIR, dataset, 'data', label))
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            return files
    return []


def get_bottlenecks(dataset, label):
    path = os.path.normpath(os.path.join(settings.DATASET_DIR, 'bottlenecks', label))
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            return [os.path.splitext(file)[0] for file in files]
    return []
