from pdf2docx import Converter

def main():
    #  Request the path of the PDF file you want to convert
    pdf_file_path = input(' Enter the path of the PDF file you want to convert (ex: "/home/novalagung/Desktop/my text.txt"): ')

    #  Remove quotation marks if any
    pdf_file_path = pdf_file_path.strip('"')

    #  Specifies the output name for the DOCX file
    output_file_path = input("Enter the name of the output file:")
    final_path = output_file_path + '.docx'

    #  Creating a converter object
    cv = Converter(pdf_file_path)

    #  Convert to DOCX file
    cv.convert(final_path, start=0, end=None)  # Mulai dari halaman 0 hingga akhir

    #  Close the resources
    cv.close()

    print(" Conversion complete! The output file has been saved in:", final_path)

#  Ensure the main function is executed when the script is executed
if __name__ == "__main__":
    main()
