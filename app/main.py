# from fastapi import FastAPI
# from scalar_fastapi import get_scalar_api_reference

# import chromadb
# import ollama

# from app.config import llm_settings

# app = FastAPI()

# client = chromadb.PersistentClient(path="app/db")
# collection = client.get_or_create_collection("docs")


# @app.get("/")
# def root():
#     return {"Info": "Server is running...."}


# @app.post("/query")
# def query(q: str):
#     results = collection.query(query_texts=[q], n_results=1)
#     context = results["documents"][0][0] if results["documents"] else ""

#     answer = ollama.generate(
#         model=llm_settings.MODEL_NAME,
#         prompt=f"Context\n\n{context}\n\nQuestion: {q}\n\nAnswer clearly and concisely",
#     )

#     return {"answer": answer["response"]}


# @app.post("/add")
# def add_knowledge(text: str):
#     try:
#         from uuid import uuid4

#         doc_id = str(uuid4())
#         collection.add(documents=[text], ids=[doc_id])

#         return {
#             "status": "success",
#             "message": "Content added to knowledge base",
#             "id": doc_id,
#         }
#     except Exception as e:
#         return {"status": "error", "message": str(e)}


# @app.get("/health")
# def health():
#     return {"status": "ok"}


# @app.get("/scalar", include_in_schema=False)
# def scalar():
#     return get_scalar_api_reference(openapi_url=app.openapi_url)
