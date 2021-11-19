import os
import json
from collections import defaultdict
from tqdm import tqdm


def read_dir(data_dir):
    clients = []
    groups = []
    data = defaultdict(lambda: None)

    files = os.listdir(data_dir)
    files = [f for f in files if f.endswith('.json')]
    for f in tqdm(files):
        file_path = os.path.join(data_dir, f)
        with open(file_path, 'r') as inf:
            cdata = json.load(inf)
        clients.extend(cdata['users'])
        if 'hierarchies' in cdata:
            groups.extend(cdata['hierarchies'])
        data.update(cdata['user_data'])

    clients = list(sorted(data.keys()))
    return clients, groups, data


def dataset_source(name):
    leaf_dataset = [
        'femnist',
        'sent140',
        'shakespeare',
        'celeba',
        'reddit',
        'synthetic',
    ]

    torchvision_dataset = [
        'mnist',
        'cifar10',
    ]

    if name in leaf_dataset:
        return 'leaf'
    elif name in torchvision_dataset:
        return 'torchvision'
    else:
        return ''



