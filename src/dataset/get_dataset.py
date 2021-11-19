import os
import importlib
from .utils import read_dir, dataset_source
from .femnist import femnist


def get_dataset(args):
    """
    Quick interface to get dataset.
    :param args:
    :return:
    """
    # first extract useful args
    n = args.num_honest
    name = args.dataset
    leaf_root = args.leaf_root
    partition = args.partition

    source = dataset_source(name)

    femnist(args)

    # if source == 'leaf':
    #     train_sets, test_sets = get_leaf_dataset(name=name, leaf_root=leaf_root)
    # elif source == 'torchvision':
    #     train_sets, test_sets = get_torchvision_dataset(1, 1)
    # elif name == 'cifar10':
    #     pass
    # else:
    #     pass
    #
    # dataset_file = "%s.py" % name
    # if not os.path.exists(dataset_file):
    #     print("Please specify a valid model")
    # mod = importlib.import_module(dataset_file)
    # print(mod)

    # if not os.path.exists(model_file):
    #     print("Please specify a valid model")
    # model_path = "%s.%s" % (dataset, model_name)
    # # build net
    # mod = importlib.import_module(model_path)
    # build_net_op = getattr(mod, "build_net")  # 获得mod这个对象的build_net方法
    # net = build_net_op(num_classes)

    # print(train_sets[2][train_sets[0][0]])


def get_leaf_dataset(name, leaf_root):
    """
    Get dataset from leaf project
    :param name:
    :param leaf_root:
    :return:
    """
    path = os.path.join(leaf_root, 'data', name, 'data')
    train_dir = os.path.join(path, 'train')
    test_dir = os.path.join(path, 'test')

    train_sets = read_dir(train_dir)
    test_sets = read_dir(test_dir)

    # clients, groups, data
    return train_sets, test_sets


def get_torchvision_dataset(name, vision_root):
    pass

    # mnist, fmnist, cifar-10
