import os, io
from google.cloud import vision
import pandas as pd
import warnings
import fitz
warnings.filterwarnings("ignore")
# from autocorrection import corrector

def fun_text_extract(path):

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"ServiceAccountToken.json"

    client = vision.ImageAnnotatorClient()  

    types_of_encoding = ["utf8", "cp1252"]

    images = []
    doc = fitz.open(path)
    total_pages = doc.page_count


    for page_num in range(total_pages) :
        page = doc.load_page(page_num)
        pix = page.get_pixmap()
        pix.save('./pages/page' + str(page_num) + '.jpg' , output='png')
        # convert to a PIL image
        # images.append(Image.frombytes("RGBA", [pix.width, pix.height], pix.samples))



    # images = convert_from_path(path, 500, poppler_path=r'C:\\poppler-0.68.0')

    # for i in range(len(images)):
    #     # Save pages as images in the pdf
    #     images[i].save('./pages/page' + str(i) + '.jpg', 'JPEG')

    opFile = open('opFile.txt', 'w', encoding=types_of_encoding[0])

    opFile = open('opFile.txt', 'a', encoding=types_of_encoding[0])

    for i in range(total_pages):
        file_name = f'./pages/page{i}.jpg'
        image_path = f'{file_name}'

        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        # construct an iamge instance
        image = vision.Image(content=content)
        # annotate Image Response
        response = client.text_detection(image=image)  # returns TextAnnotation
        df = pd.DataFrame(columns=['locale', 'description'])


        texts = response.text_annotations

        for text in texts:
            df = df.append(
                dict(
                    locale=text.locale,
                    description=text.description

                ),
                ignore_index=True
            )

            # opFile.write(text.description)

        opFile.write(df['description'][0])
        os.remove(file_name)
    opFile.close()