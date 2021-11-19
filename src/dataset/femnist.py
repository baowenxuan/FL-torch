import os

from .utils import read_dir


def femnist(args):
    """
    FEMNIST dataset in Leaf Project
    :param root:
    :param partition:
    :return:
    train_sets: dictionary of torch.utils.Dataset
    test_sets:
    """
    leaf_root = args.leaf_root

    # train_dir = os.path.join(leaf_root, 'data/femnist/data/train')
    # test_dir = os.path.join(leaf_root, 'data/femnist/data/test')
    #
    # train_data = read_dir(train_dir)


def femnist_(leaf_root, set_='train'):
    data_dir = os.path.join(leaf_root, 'data/femnist/data', set_)
    print(123)
    clients, groups, data = read_dir(data_dir)
    for client in clients:
        print(data[client])
        break