from fpdf import FPDF
from PIL import Image
from PyPDF2 import PdfFileMerger, PdfFileReader
import os
import natsort

imagelist = []
pdflist = []

folder = "inputFolder"
folder2 = "data"
# name = ".pdf"
pdf = FPDF()
totalJpgSize = 0
savedFIleNumber = 0
merger = PdfFileMerger()

def checkFolder(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

def pdf2(fileNames):
    for filename in fileNames:
        merger.append(filename)
    

for dirpath, dirnames, filenames in os.walk(folder):
    for filename in [f for f in filenames if f.endswith(".jpg")]:
        full_path = os.path.join(dirpath, filename)
        imagelist.append(full_path)

for dirpath, dirnames, filenames in os.walk(folder2):
    for filename in [f for f in filenames if f.endswith(".pdf")]:
        full_path = os.path.join(dirpath, filename)
        pdflist.append(full_path)
    print(full_path)
imagelist = natsort.natsorted(imagelist)
pdflist = natsort.natsorted(pdflist)


def savedFIleNumber():
    savedFIleNumber += 1
    return savedFIleNumber


def getImageHight():
    imageHight = 0
    count = 1
    for i in range(0, len(imagelist)):
        im1 = Image.open(imagelist[i])
        width, height = im1.size
        if width == 720:
            imageHight += height
            count += 1

    return imageHight/count


def createNewEmptyImage(hight):
    dst = Image.new(
        'RGB', (720, hight))
    return dst


def jpgSave(src):
    src


def trim(im):
    box = (im.size)
    im.crop()


def addImageToEmptyImage(dst, im, pos):
    dst.paste(im, pos)


def main():
    # tmpver = getImageHight()*2
    # img = createNewEmptyImage(65499)
    pos = (0, 0)
    newImageList = []
    PILimg = []
    imgnum = 1
    # for i in range(0, len(imagelist)):
    #     im1 = Image.open(imagelist[i])
    #     width, height = im1.size
    #     # if imageHight < tmpver:
    #     if width == 720:
    #         # newImageList.append(imagelist[i])
    #         im2 = im1.convert("RGB")
    #         # pdf.add_page()
    #         # pdf.image(im2.save("__temp.pdf", 'PDF'), 0, 0, 0, 0, "PDF")
    #         im2.save(f'data/pdfconvPIL{imgnum}.pdf', 'PDF')
    #         # PILimg.append(im2)
    #         print(f'Added {imgnum} {imagelist[i][5:]}')
    #         imgnum+=1
            # pdf.add_page()
            # pdf.image(createNewEmptyImage(height), )
    # print('Started')
    # im1.save(f'data/pdfconv.pdf', save_all=True, append_images=PILimg)
    # pdf.write()
    # for i in range(0, len(pdflist)):
    pdf2(pdflist)
        # print(pdflist[i])

    merger.write("SigPdf/Merged_doc.pdf")
    print('Done')

    #             addImageToEmptyImage(tmpimg, im1, (0, imageHight))
    #             imageHight += height
    #             addImageToEmptyImage(tmpimg, im1, (0, imageHight))
    #     else:
    #         if width == 720:
    #             addImageToEmptyImage(tmpimg, im1, (0, imageHight))
    #             imageHight += height
    #             addImageToEmptyImage(tmpimg, im1, (0, imageHight))
    #         img = createNewEmptyImage(imageHight)
    #         print(imagelist[i])
    #         box = (0, 0, 720, imageHight)
    #         img = tmpimg.crop(box)
    #         img.save(f'data/testproj{imgnum}.pdf')
    #         pos = (0, 0)
    #         imgnum += 1
    #         imageHight = 0
    # box = (0, 0, 720, imageHight)
    # img = tmpimg.crop(box)
    # img.save(f'data/testproj{imgnum}.pdf', "PDF")



if __name__ == '__main__':
    main()
