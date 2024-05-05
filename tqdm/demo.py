from tqdm import tqdm
from time import sleep


# This is a simple example of how to use tqdm
# to show a progress bar while processing items
# for more information, check the documentation https://tqdm.github.io/
items = range(100)

for i in tqdm(items, desc='Processing items'):
    sleep(0.1)
