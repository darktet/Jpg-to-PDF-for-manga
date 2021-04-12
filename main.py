from PIL import Image
from PyPDF2 import PdfFileMerger
import os
import natsort
from cachetools import cached, LRUCache
import sys
import time
import itertools
import threading


def load_animation(count: bool):

    load_str = "working on it please wait"
    ls_len = len(load_str)
    animation = "|/-\\"
    anicount = counttime = i = 0

    while count:
        time.sleep(0.075)
        load_str_list = list(load_str)
        x = ord(load_str_list[i])
        y = 0
        if x != 32 and x != 46:
            if x > 90:
                y = x-32
            else:
                y = x + 32
            load_str_list[i] = chr(y)
        res = ''
        for j in range(ls_len):
            res = res + load_str_list[j]
        sys.stdout.write("\r"+res + animation[anicount])
        sys.stdout.flush()
        load_str = res
        anicount = (anicount + 1) % 4
        i = (i + 1) % ls_len
        counttime = counttime + 1


def folderCheck(*dirName: str):
    for i in dirName:
        if not os.path.exists(i):
            os.makedirs(i)
    print(f"Directory created. Insert your images in inputDiractory")


@cached(cache=LRUCache(maxsize=2))
def imageProp(location: str):
    return Image.open(location).convert('RGB')


def arrangeFiles(dirName):
    return natsort.natsorted([f"{dirName}/{x}" for x in os.listdir(dirName)])


def files(dirNames: str, xPdf: PdfFileMerger):
    i = ii = 0
    for file in arrangeFiles(dirNames):
        ii += 1
        if imageProp(file).width == 720:
            # print(f"{i} file done")
            imageProp(file).save(f'{file[:-4]}.pdf', 'PDF')
            xPdf.append(f'{file[:-4]}.pdf')
            os.remove(f'{file[:-4]}.pdf')
            i += 1

    print(f"\n\n720: {i}", f"\nNot 720: {ii-i}", f'\nTotal: {ii}')
    # Width == 720 will be convert else not


def main():
    outputDir, inputDir = 'outSigPdf', 'inputDiractory'
    if os.path.exists(inputDir) and os.path.exists(outputDir):

        # load_animation(True)
        fullPdf = PdfFileMerger()
        files(inputDir, fullPdf)
        fullPdf.write(f'{outputDir}/JpgtoPDFConvert.pdf')
        # load_animation(False)
        print(f"Jpg to PDF done check outSigPdf")
    else:
        folderCheck(inputDir, outputDir)

# here is the animation


def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')


if __name__ == '__main__':
    start = time.perf_counter()

    done = False

    t = threading.Thread(target=animate)
    t.start()

    # long process here
    main()
    time.sleep(10)
    done = True

    print("Time Taken: ", time.perf_counter() - start)
