import torch

from fed_options import args_parser
from dataset import get_dataset


def train():
    pass


def test():
    pass


def main(args):
    get_dataset(args)



if __name__ == '__main__':
    args = args_parser()
    print(args)
    torch.manual_seed(args.seed)
    main(args)