from langchain_community.document_loaders import PyPDFLoader

def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    return loader.load()


# from datasets import load_dataset


# dataset = load_dataset(
#     "onyx-dot-app/EnterpriseRAG-Bench",
#     "documents",
#     split="test[:20000]"
# )
# documents = dataset






