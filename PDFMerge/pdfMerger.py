import PyPDF2
import sys

multiple_inputs = sys.argv[1:]

def pfd_combiner(name_list):
    merger = PyPDF2.PdfMerger()
    for pdf in name_list:
        merger.append(pdf)
    merger.write("universal_truth.pdf")


pfd_combiner(multiple_inputs)
