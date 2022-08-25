import io,os
from google.cloud import vision
import aspose.words as aw
import shutil
import sys

def detect_document(path,json):
    #     parent_path = 'C:\\Users\\india\\Desktop\\druidot'
    #     os.chdir(parent_path)
    """Detects document features in an image."""
    #     from google.cloud import vision
    #     import io,os
    print("detect document working")
    total_word = ''
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = json
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.document_text_detection(image=image)

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            #             print('\nBlock confidence: {}\n'.format(block.confidence))

            for paragraph in block.paragraphs:
                #                 print(paragraph)

                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    total_word = total_word + ' ' + word_text
        print('{} '.format(
                            total_word))

    #                     for symbol in word.symbols:
    #                         print('\tSymbol: {} (confidence: {})'.format(
    #                             symbol.text, symbol.confidence))
    return total_word
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))


def function(json_path,pdf_folder_path):
    print("working")
    n = 0
    parent_path = os.getcwd()
    os.chdir(parent_path)

    os.mkdir('Output_image')
    # adding the json file to output_image
    os.chdir(parent_path)
    src_dir = os.getcwd()

    dest_dir = parent_path +r'\Output_image'
    # gets the current working dir
    print(src_dir)
    dest_file = src_dir + "neon-opus-355812-023accafc659.json"
    shutil.move(json_path +r'\neon-opus-355812-023accafc659.json',parent_path +r'\Output_image')
    # neon-opus-355812-023accafc659
    # print(os.listdir())
    # the file 'test.txt' is moved from
    # src to dest with a new name

    os.chdir(dest_dir)
    print(os.listdir())  # list of files in dest

    os.chdir(parent_path)
    os.chdir(pdf_folder_path)
    pdf_dir = os.getcwd()
    list_of_pdfs = os.listdir('.')
    # os.chdir(parent_path)
    for pdf in list_of_pdfs:
        doc = aw.Document(pdf)
        for page in range(0, doc.page_count):
            n += 1
            extractedPage = doc.extract_pages(page, 1)
            #         save the image file in output folder
            os.chdir(parent_path)
            os.chdir('Output_image')
            extractedPage.save(f"Output_{page + n}.jpg")
        os.chdir(parent_path)
        os.chdir(pdf_dir)
    os.chdir(parent_path)

    os.chdir(parent_path)
    pdf_folder = os.listdir(pdf_folder_path)
    os.chdir(parent_path)
    os.chdir('Output_image')
    os.listdir()
    for i in range(len(pdf_folder)):

        a = detect_document('Output_{}.jpg'.format(i + 1),parent_path+r'\Output_image\neon-opus-355812-023accafc659.json')
        os.remove('Output_{}.jpg'.format(i + 1))
        #     print(type(a))
        try:
            f = open('file_{}.txt'.format(i + 1), 'w', encoding='utf-8')
            f.write(a)
        except Exception as e:
            print("Errorrrrrrrrr:", str(e))
        finally:
            f.close()


    src_dir = os.getcwd()
    dest_dir = json_path +r'\neon-opus-355812-023accafc659.json'
    # gets the current working dir
    print(src_dir)
    dest_file = src_dir + "neon-opus-355812-023accafc659.json"
    shutil.move('neon-opus-355812-023accafc659.json',dest_dir )

    os.chdir(parent_path)


# funtion(parent_path , json_file path,pdf_folder_path)
# parent_path -> path of the directory which contain the python file
# json_file_path -> path of the directory which contain json file



# for i in range(2):
# a = r"C:\Users\india\Desktop\druidot"
# function(r'C:\Users\india\Desktop\druidot',r'C:\Users\india\Desktop\pythonProject',r'C:\Users\india\Desktop\pdf')
# r'C:\Users\india\Desktop\druidot' r'C:\Users\india\Desktop\pythonProject' r'C:\Users\india\Desktop\pdf'
# a = sys.argv[1]
# C:\Users\india\Desktop\pythonProject C:\Users\india\Desktop\pdf
# b = sys.argv[1]
# c = sys.argv[2]

from tkinter import *

root = Tk()

def getvals():
    print("Submitting form")

    print(json.get(), pdf_folder_name.get())
    # json  = json.get()
    # file_path = pdf_folder_name.get()
    function(json.get(),pdf_folder_name.get())
    # with open("records.txt", "a") as f:
    #     f.write(f"{json.get(), pdf_folder_name.get()}")



root.geometry("644x344")
#Heading
Label(root, text="Welcome ", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

#Text for our form
json = Label(root, text="Json Path")
pdf_folder_name = Label(root, text="File Path")


#Pack text for our form
json.grid(row=1, column=2)
pdf_folder_name.grid(row=2, column=2)


# Tkinter variable for storing entries
json = StringVar()
pdf_folder_name = StringVar()

#Entries for our form
json = Entry(root, textvariable=json)
pdf_folder_name = Entry(root, textvariable=pdf_folder_name)


# Packing the Entries
json.grid(row=1, column=3)
pdf_folder_name.grid(row=2, column=3)



#Button & packing it and assigning it a command
Button(text="Submit", command=getvals).grid(row=7, column=3)



root.mainloop()