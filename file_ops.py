import tarfile

def create_targz(infile):
    with tarfile.open("{}.tar.gz".format(infile), "w:gz") as tar:
        tar.add(infile)

def extract_targz(infile):
    with tarfile.open(infile, "r:gz") as tar:
        tar.extractall()
