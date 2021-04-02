from PIL import Image
from PyPDF2 import PdfFileMerger
import os
import natsort
from cachetools import cached, LRUCache


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
            print(f"{i} file done")
            imageProp(file).save(f'{file[:-4]}.pdf', 'PDF')
            xPdf.append(f'{file[:-4]}.pdf')
            os.remove(f'{file[:-4]}.pdf')
            i += 1
                
    print(f"\n\n720: {i}", f"\nNot 720: {ii-i}", f'\nTotal: {ii}')
    # Width == 720 will be convert else not

def main():
    outputDir, inputDir = 'outSigPdf', 'inputDiractory'
    if os.path.exists(inputDir) and os.path.exists(outputDir):
        fullPdf = PdfFileMerger()
        files(inputDir, fullPdf)
        fullPdf.write(f'{outputDir}/JpgtoPDFConvert.pdf')
        print(f"Jpg to PDF done check outSigPdf")
    else: 
        folderCheck(inputDir, outputDir)

if __name__ == '__main__':
    import time
    start = time.perf_counter()

    main()

    print("Time Taken: ", time.perf_counter() - start)
