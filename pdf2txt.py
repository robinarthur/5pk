
# coding: utf-8

# In[1]:

from wand.image import Image
from PIL import Image as PI
from datetime import datetime
import pyocr
import pyocr.builders
import io
import sys


# In[2]:

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


# In[3]:

#prepare dataset files
books_list = []
authors_list = []


# In[ ]:



