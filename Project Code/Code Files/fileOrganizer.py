from extension import EXT
from Timeandate import DATESANDTIMES
from size import SIZEORGANIZER
import os


class fileOrganizer:
    def __init__(self):
        self.Dir_PATH = r'C:\Users\Kunal Sharma\Desktop\Project Test Folder 1'
        self.Src_PATH = r'C:\Users\Kunal Sharma\Desktop\Project Test Folder 1'+'\\'

    def extension(self, v):
        EXT(v)

    def DATES(self, v):
        DATESANDTIMES(v)

    def SIZE(self, v):
        SIZEORGANIZER(v)


def Dictionary(A, B):
    d = {1: "ORGANISE BY Extension\n",
         2: "ORGANISE BY DATE\n",
         3: "ORGANISE BY SIZE\n"}
    if len(A) == 1 or len(A) == 0:
        return
    if not os.path.exists(A):
        return
    inputChoice(A, B)
    print(d[B])


def inputChoice(A, B):
    obj = fileOrganizer()
    if B == 1:
        obj.extension(A)
    if B == 2:
        obj.DATES(A)
    if B == 3:
        obj.SIZE(A)
    if B > 3:
        print("your selection is not valid")
