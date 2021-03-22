from PyPDF2 import PdfFileMerger, PdfFileReader
import os, time

mergedObject = PdfFileMerger()
arr = os.listdir('.')
print("Found {} files in the folder. Will only merge PDFs".format(len(arr)))

for fi in arr:
    if fi.endswith('.pdf'):
        print(">> Merging file : {}".format(fi))
        mergedObject.append(PdfFileReader(fi,strict=False),import_bookmarks=False)

print("Creating PDF")

mergedObject.write("MergePDFoutput.pdf")

print("All files processed. Closing in 5 seconds.")

time.sleep(5)


