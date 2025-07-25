from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import LlamaCpp
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from IPython.display import Markdown, display

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
persist_directory = "../data/chroma_db"
vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

llm = LlamaCpp(
    model_path="../models/mistral-7b-v0.1.Q2_K.gguf",
    temperature=0.75,
    max_tokens=2000,
    top_p=1,
    callback_manager=callback_manager,
    verbose=True,
    n_ctx=2048,  # Increased context window
)

retriever = vectordb.as_retriever(search_kwargs={"k": 3})

# Template and chain
template = """
You are a helpful assistant. Use ONLY the information provided in the context below to answer the user's question.
Do NOT use any prior knowledge or make up information. If the answer is not in the context, respond with "I don't know based on the provided context."

Context:
{context}

Question:
{question}

Answer:
"""

prompt = ChatPromptTemplate.from_template(template)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

def get_responsef(message):
    response = chain.invoke(message)
    return response
