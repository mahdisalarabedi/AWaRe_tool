from io import BytesIO
from openai import OpenAI
import PyPDF2   # or `pip install pypdf`

client = OpenAI()

def create_file_from_selected_pages(client, file_path, pages_to_keep, out_path="selected.pdf"):
    """
    file_path: path to the original PDF
    pages_to_keep: list of page numbers (0-based index) you want to keep
    out_path: path where the filtered PDF will be saved locally
    """
    # Read and filter PDF
    pdf_writer = PyPDF2.PdfWriter()
    with open(file_path, "rb") as infile:
        reader = PyPDF2.PdfReader(infile)
        for page_num in range(0,pages_to_keep):
            if page_num < len(reader.pages):
                pdf_writer.add_page(reader.pages[page_num])

    # Save to disk so you can inspect it
    with open(out_path, "wb") as f_out:
        pdf_writer.write(f_out)

    print(f"Filtered PDF saved to {out_path}")

    # Re-open the saved file and upload to OpenAI
    with open(out_path, "rb") as f_in:
        result = client.files.create(
            file=(out_path, f_in, "application/pdf"),
            purpose="assistants"
        )

    print("File uploaded with id:", result.id)
    return result.id

# Replace with your own file path or URL

#file_id=create_file_from_selected_pages(client,"AWaRe.pdf", 293, out_path="selected.pdf")

#vector_store = client.vector_stores.create(
#    name="Antibiotic_RAG"

#print(vector_store.id)

#result = client.vector_stores.files.create(
#    vector_store_id=vector_store.id,
#    file_id=file_id
#)
#print(result)

result = client.vector_stores.files.list(
    vector_store_id='vs_68a2e40cdd6c8191b8eabb5906bda8e7'
)
print(result)