import argparse


def args_parser():
    parser = argparse.ArgumentParser()

    # ======== Basic Information ========

    # ======== Random Seed ========

    parser.add_argument('--seed', type=int, default='0',
                        help='random seed')

    # ======== Directories ========

    parser.add_argument('--leaf_root', type=str, default='../../leaf',
                        help='root of leaf project')

    parser.add_argument('--vision_root', type=str, default='../../leaf',
                        help='root of leaf project')

    # ======== Dataset Settings ========

    parser.add_argument('--dataset', type=str, default='mnist',
                        help='name of the dataset')

    parser.add_argument('--partition', type=str, default='natural',
                        help='way to split data')

    # ======== System Settings ========

    parser.add_argument('--num_honest', type=int, default=100,
                        help='number of honest client, overwritten when partition = natural')

    # ======== Training Settings ========



    # ======== Attacker ========

    parser.add_argument('--num_byz', type=int, default=0,
                        help='number of Byzantine client')

    args = parser.parse_args()

    return args
