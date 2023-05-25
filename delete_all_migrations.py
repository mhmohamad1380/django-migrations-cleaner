import os
import glob


dpath = "."

sub_paths = glob.glob(dpath + "/*")

for path in sub_paths:
    migrations_path = "/migrations/*[!__init__]*.py"
    files = glob.glob(path + migrations_path)
    for file in files:
        try:
            os.remove(file)
        except:
            pass
