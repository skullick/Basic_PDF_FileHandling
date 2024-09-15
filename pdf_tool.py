import pypdf
import os
import PIL
def merge_pdfs(pdf_list, output_path):
    pdf_writer = pypdf.PdfWriter()
    for pdf in pdf_list:
        pdf_reader = pypdf.PdfReader(pdf)
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])
    with open(output_path, 'wb') as out:
        pdf_writer.write(out)
    print(f"Merged PDF saved to {output_path}")


def split_pdfs(pdf_path, output_dir=None):
    if output_dir is None:
        output_dir = os.getcwd()
    
    pdf_reader = pypdf.PdfReader(pdf_path)
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer = pypdf.PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[page_num])
        
        output_path = f"{output_dir}/page_{page_num + 1}.pdf"
        with open(output_path, 'wb') as out:
            pdf_writer.write(out)
        
        print(f"Saved {output_path}")

def extract_text(pdf_path, output_path):
    pdf_reader = pypdf.PdfReader(pdf_path)
    full_text = ''
    for page in pdf_reader.pages:
        full_text += page.extract_text(extraction_mode='plain') + '\n'
    
    with open(output_path, 'w') as out:
        out.write(full_text)

    print(f"Extracted text is saved as {output_path}")

def extract_image(pdf_path, output_dir=None):
    if output_dir is None:
        output_dir = os.getcwd()

    pdf_reader = pypdf.PdfReader(pdf_path)
    for num, page in enumerate(pdf_reader.pages):
        for image in page.images:
            output_path = f"{output_dir}/{image.name}_{num + 1}"
            with open(output_path, 'wb') as out:
                out.write(image.data)

            print(f"Saved {output_path}")


def encrypt_pdf(pdf_path, output_path, password):
    pdf_reader = pypdf.PdfReader(pdf_path)
    pdf_writer = pypdf.PdfWriter()
    for page in pdf_reader.pages:
        pdf_writer.add_page(page)
    
    pdf_writer.encrypt(password)

    with open(output_path, 'wb') as out:
        pdf_writer.write(out)
    
    print(f"Encrypted PDF file is saved as {output_path}")

def decrypt_pdf(pdf_path, output_path, password):
    pdf_reader = pypdf.PdfReader(pdf_path)
    pdf_writer = pypdf.PdfWriter()

    try:
        pdf_reader.decrypt(password)
    except:
        print("Wrong password!")
    else:
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)
        
        with open(output_path, 'wb') as out:
            pdf_writer.write(out)
        
        print(f"Decrypted PDF file is saved as {output_path}")

def rearrange_pdf(pdf_path, output_path, order):
    pdf_reader = pypdf.PdfReader(pdf_path)
    pdf_writer = pypdf.PdfWriter()

    for idx in order:
        pdf_writer.add_page(pdf_reader.pages[idx - 1])
    
    with open(output_path, 'wb') as out:
        pdf_writer.write(out)

    print(f"Rearranged PDF file saved as {output_path}")

def rotate_pdf(pdf_path, output_path, angle):
    pdf_reader = pypdf.PdfReader(pdf_path)
    pdf_writer = pypdf.PdfWriter()

    for page in pdf_reader.pages:
        page.rotate(angle)
        pdf_writer.add_page(page)

    with open(output_path, 'wb') as out:
        pdf_writer.write(out)
    
    print(f"Rotated PDF file is saved as {output_path}")

def get_metadata(pdf_path):
    pdf_reader = pypdf.PdfReader(pdf_path)

    metadata = pdf_reader.metadata

    print(f"Metadata of {pdf_path} :")

    for key, value in metadata.items():
        print(f'{key}: {value}')

def set_metadata(pdf_path, output_path, **kwargs):
    pdf_reader = pypdf.PdfReader(pdf_path)
    pdf_writer = pypdf.PdfWriter()

    for page in pdf_reader.pages:
        pdf_writer.add_page(page)


    metadata = {f"/{key.capitalize()}": value for key, value in kwargs.items() }
    pdf_writer.add_metadata(metadata)

    with open(output_path, 'wb') as out:
        pdf_writer.write(out)

    print(f"PDF file with updated metadata is saved as {output_path}")

def compress_pdf(pdf_path, output_path):
    pdf_reader = pypdf.PdfReader(pdf_path)
    pdf_writer = pypdf.PdfWriter()

    for page in pdf_reader.pages:
        pdf_writer.add_page(page)
        page.compress_content_streams()

    with open(output_path, "wb") as out:
        pdf_writer.write(out)

    print(f"Compressed PDF file is saved as {output_path}")


        

### Test the above functions ###

# merge_pdfs(['Page+1.pdf','Page+2.pdf'], 'Merged.pdf')

#split_pdfs("Merged.pdf", "split_example")

#extract_text('Merged.pdf','Extracted.txt')

#rearrange_pdf('Merged.pdf', 'Rearranged.pdf', [3,2,1])

# rotate_pdf("Merged.pdf", "Rotated.pdf", 90)

#get_metadata('Page+1.pdf')

#set_metadata('Page+1.pdf', 'myPage1.pdf', author='Tien Nguyen', modDate="2024-13-09")

#get_metadata('myPage1.pdf')

compress_pdf("Merged.pdf", "Compressed.pdf")