"""
collect fillable form data from all pdf files in the input directory,

"""
import sys
import os
import re
from pdfminer.pdfparser import PDFParser
# from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdftypes import resolve1





def get_fields(file_path):
    """
    extract all field data from a pdf file
    """

    parser = PDFParser(file_path)
    doc = PDFDocument(parser)
    # parser = PDFParser(file_path)
    # doc = PDFDocument()
    # parser.set_document(doc)
    # doc.set_parser(parser)
    # doc.initialize()

    return resolve1(doc.catalog['AcroForm'])['Fields']


def get_record_value_string(dir_name, file_name):
    """
    get a response form values as a string, separated by ','
    """
    fp = open(os.path.join(dir_name, file_name), 'rb')
    fields = get_fields(fp)

    # initialize value list  with file_name
    record_values = [file_name]
    for i in fields:
        field = resolve1(i)
        name, value = field.get('T'), field.get('V')
        record_values.append(",%s" % str(value).replace(",", "_"))

    fp.close()
    # convert to string
    return ''.join(record_values)


def get_record_header_string(dir_name, file_name):
    """
    get field headers, return as a string
    """
    fp = open(os.path.join(dir_name, file_name), 'rb')
    fields = get_fields(fp)

    record_fields = []
    for i in fields:
        field = resolve1(i)
        name, value = field.get('T'), field.get('V')
        record_fields.append(",%s" % name)

    fp.close()
    # convert to string
    return ''.join(record_fields)


###### main program starts here ######

# get only pdf files
regx = re.compile("\\.pdf$", re.IGNORECASE)

# input directory,
abspath = os.path.abspath(__file__)
input_dir_path = os.path.dirname(abspath)

output_path = os.path.join(input_dir_path, "output.odt")

# get all pdf files in directory
filenames = list(filter(regx.search, os.listdir(input_dir_path)))
output_file = open(output_path, "w")

# write header to output
output_file.write("{}\n".format(get_record_header_string(input_dir_path, filenames[0])))

# fill in form data from files
# for f in filenames:
#    output_file.write("%s\n" % get_record_value_string(input_dir_path, f))

output_file.close()
