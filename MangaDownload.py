import requests
import jpg_to_pdf
from bs4 import BeautifulSoup
from PIL import Image
import time



# class MangSeeImage:
#     chapter, page = str(0).zfill(4), str(1).zfill(3)
#     def url(self, url: str):
#         self.url = url

#     def __init__(self, number: int) -> None:
#         imageUrl = self.url

def linkGen(chapter: int, page: int):
    return f'https://temp.compsci88.com/manga/Solo-Leveling/{str(chapter).zfill(4)}-{str(page).zfill(3)}.png'


def download(chapter: int):
    page = 1
    im1 = Image.open()
    width, height = im1.size
    # if imageHight < tmpver:
    if width == 720:
        # newImageList.append(imagelist[i])
        im2 = im1.convert("RGB")
        # pdf.add_page()
        # pdf.image(im2.save("__temp.pdf", 'PDF'), 0, 0, 0, 0, "PDF")
        im2.save(f'data/pdfconvPIL{imgnum}.pdf', 'PDF')
        # PILimg.append(im2)
        print(f'Added {imgnum} {imagelist[i][5:]}')




def main():
    pass
    # while True:
    #     try:
    #         chapter = int(input("Which Cha: "))
    #         print("Hello Santo", ("1" * 10), type(chapter))
    #         break
    #     except ValueError:
    #         print("Insurt Number")
    # ii = 'https://temp.compsci88.com/manga/Solo-Leveling/0146-007.png'
    # y = requests.get('https://temp.compsci88.com/manga/Solo-Leveling/0146-007.png')
    # print(y.status_code)
    # x = requests.get('https://temp.compsci88.com/manga/Solo-Leveling/0146-006.png')
    # print(x.status_code)
    
    
    
if __name__=="__main__":
    main()