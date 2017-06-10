import sys
import PyPDF2
import subprocess


def run(file_name, page):
    command = "java -jar pdfbox-app-2.0.2.jar ExtractText {file_name} out\\{page}-extracted.txt -startPage {page} -endPage {page}"
    return subprocess.check_output(command.format(page=page, file_name=file_name), shell=True)


def number_of_pages(file_name):
    with open(file_name, "rb") as pdf_file:
        return PyPDF2.PdfFileReader(pdf_file).numPages

if __name__ == "__main__":
    file_name = sys.argv[1] if len(sys.argv) == 2 else "cpdf.pdf"
    pages = number_of_pages(file_name)

    for page in range(1, pages + 1):
        run(file_name, page)
        print('Completed {}'.format(page))
