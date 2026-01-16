import argparse
from PIL import Image

import h5py

parser = argparse.ArgumentParser()
parser = parse.add_argument('--path')

def make_image():


if __name__ == '__main__':
    args = parser.parse_args()
    path = args.path

    with h5py.File(path, 'r') as f:
	img = make_image(dset) 
