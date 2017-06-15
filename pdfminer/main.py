import os
import re
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdftypes import resolve1
from fdfgen import forge_fdf



def get_fields(file_obj):
    """
    document it later
    :param file_obj:
    :return:
    """

    parser = PDFParser(file_obj)
    doc = PDFDocument(parser)

    return resolve1(doc.catalog['AcroForm'])['Fields']


def get_fields_as_list(dir_name, file_name):
    """
    document it later
    :param dir_name:
    :param file_name:
    :return:
    """

    file_path = os.path.join(dir_name, file_name)
    file_obj = open(file_path, 'rb')
    fields = get_fields(file_obj)

    field_names_as_list = [resolve1(i).get('T') for i in fields]


def Field_to_ignore(text):
    # TODO change these fields accordingly
    supported_fields = ['text box']
    if text.lower() in supported_fields:
        return False
    else:
        return True

def FillForm(list):
    #TODO finish this function
    fields_filled = []
    # for i in list:
    #     if not Field_to_ignore(i):
    
    # for testing only
    fields = [('Given Name Text Box', 'Bhavesh'), ('Family Name Text Box', 'Praveen')]
    fdf = forge_fdf("", fields)
    fdf_file = open('/home/ichigo/Desktop/test_outputs/data.fdf', 'wb')
    fdf_file.write(fdf)
    fdf_file.close()

def test():
    # fields_list = get_fields_as_list('/home/ichigo/Desktop/', 'pdfform.pdf')
    FillForm([])
test()




