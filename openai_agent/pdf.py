import os

from llama_index import (
    StorageContext,
    VectorStoreIndex,
    load_index_from_storage
)

from llama_index.readers import PDFReader

def get_index(data, index_name):
    index = None
    if not os.path.exists(index_name):
        print("building index", index_name)
        index = VectorStoreIndex.from_documents(data, show_progress=True)
        index.storage_context.persist(persist_dir=index_name)
    else:
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_name)
        )

    return index


pdf_path = os.path.join(".data","Daft Punk.pdf")
daft_pdf = PDFReader().load_data(file=pdf_path)

daft_index = get_index(daft_pdf, "daft_punk")
daft_engine = daft_index.as_query_engine()