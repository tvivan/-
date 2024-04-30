from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.readers.file import PDFReader
import os

def get_index(data,index_name):
    index = None
    if not os.path.exists(index_name):
        print("building index ",index_name)
        index = VectorStoreIndex.from_documents(data,show_progress=True)
        index.storage_context.persist(persist_dir=index_name)
    else:
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_name)
        )
    return index
cyr_pdf = PDFReader().load_data(file=r"C:\Users\tviva\Downloads\CYR\CYRЦУР 3.pdf")
cyr_index = get_index(cyr_pdf,"cyr_test")
cyr_engine = cyr_index.as_query_engine()
