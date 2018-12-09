with open('password.txt') as fp, open('passwo.dat', 'w') as fw:
    """context manager"""
    fw.write(fp.read())