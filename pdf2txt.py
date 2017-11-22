
# coding: utf-8
"""
The main goal of this function is to make pdf searchable. To solve this task it
is necessary to convert the pdf into text and store the text into the db. every
pdf should only have one destination -> the ticket id in the db maybe
"""


from wand.image import Image
from PIL import Image as PI
from datetime import datetime
import pyocr
import pyocr.builders
import io
import sys


#starttime for scripttiming
start_time = datetime.now()

tools = pyocr.get_available_tools()
#if len(tools) == 0:
#    print("No OCR tool found")
#    sys.exit(1)
tool = tools[0]
lang = tool.get_available_languages()[0]

#lists for the temporary image and the final text
req_image = []
final_text = []
PDF_FILE_NAME = "./5pk_deutsch_gedanken.pdf"

#open the pdf file using wand and convert it to jpeg
image_pdf = Image(filename='./Faust-Ein-Fragment.pdf', resolution=300)
image_jpeg = image_pdf.convert('png')

#every page was converted into seperate image blob, loop over to store them in the req_image
for img in image_jpeg.sequence:
    img_page = Image(image=img)
    req_image.append(img_page.make_blob('png'))

#run the ocr over the image blobs
for img in req_image:
    txt = tool.image_to_string(
        PI.open(io.BytesIO(img)),
        lang=lang,
        builder=pyocr.builders.TextBuilder()
    )
    final_text.append(txt)

print(datetime.now() - start_time)
#for debugging
print(final_text)
print(lang)


def pdf2text():
    """This function reads a PDF Document and process it to give the Text in it
    back. To solve this task there are a few steps necessary:

    1. - initialise the Tools needed
    2. - switch the Tool to the desired language
    3. - split every page of the pdf into several image blobs
    4. - after looping over it, they were stored for further processing in a
        variable
    5. - the bitwise readed image (page) would be processed into text with the
        help of pyocr and tesseract
    6. - final_text would be append in every round of the loop
    7. - all this (point 4-6) happend in the loop

    In the end final_text has all of text from the pdf
    """

    pass


def check_pdf_txt_quality():
    """this function is for developping only

    the readed text is known and stored in another text

    the functions should get the length of the original text and compare it with
    the final_text

    after that there should be a score, to show how exact the pdf2text function
    works. the score should be a value between 0-100 (percent) to show if any
    image preprocessing is needed before the imageblob 2 pdf processing starts
    """
    pass


def store_the_text():
    """
    This function should store the final text into the db.
    i think it needs the ticket id, to find the right destination
    """
    pass

def connect():
    """
    This function connects the script with the database.
    - mariadb mysql
    - ...
    """
    pass




#prepare dataset files
books_list = []
authors_list = []
