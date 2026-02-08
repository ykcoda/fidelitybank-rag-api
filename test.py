import chromadb
from pprint import pprint


class VectorDB:
    def __init__(
        self, collection_name: str, host: str = "", port: int = 0, path: str = ""
    ):

        # self.client = chromadb.HttpClient(host=host, port=port)
        self.client = chromadb.PersistentClient(path=path)
        self.collection_name = collection_name
        self.collection = self.client.get_or_create_collection(self.collection_name)

    def add_document(self, ids: list[str], documents: list[str], metadatas):
        self.collection.add(ids=ids, documents=documents, metadatas=metadatas)
        print(f"documents added to {self.collection_name} collection")

    def get_document(self, id: str):
        document = self.collection.get(ids=id)
        pprint(document)

    def query_collection(self, q: str, n_results: int = 1):
        return self.collection.query(query_texts=[q], n_results=n_results)

    def get_collections(self):
        return self.collection.get()

    def update_document(self, id: str, document: str):
        self.collection.update(ids=[id], documents=[document])
        print(f"document with id# '{id}' has been updated.")

    def delete_document(self, id):
        self.collection.delete(ids=id)
        print(f"document with id# '{id}' has been deleted.")

    def filter_by_metadata(self, key: str, transport_type: str):
        results = self.collection.get(where={f"{key}": f"{transport_type}"})
        pprint(results)


def main():
    vector_db = VectorDB(collection_name="fbl_documents", path="db")

    #################ADD#####################################
    # vector_db.add_document(
    #     ["car1", "plane1", "boat1", "bus1"],
    #     [
    #         "Bus carries passengers on road",
    #         "Plane flies across countries",
    #         "Boat travels on water",
    #         "Bicycle runs without fuel",
    #     ],
    #     [
    #         {"type": "public_transport", "fuel": "diesel"},
    #         {"type": "air_transport", "fuel": "jet"},
    #         {"type": "water_transport", "fuel": "diesel"},
    #         {"type": "personal_transport", "fuel": "manual"},
    #     ],
    # )

    # query = input("Type your query: ")
    # results = vector_db.query_collection(query, n_results=2)
    # pprint(results)

    #################UPDATE#####################################
    # vector_db.update_document(
    #     "bus1", "Bus carries more than 40 passengers and runs on road"
    # )

    #################DELETE#####################################
    # vector_db.delete_document("boat1")
    #################GET A SINGLE DOCUMENT#####################################
    # vector_db.get_document("bus1")

    #################GET ALL DOCUMENTS#####################################
    # print("###" * 15)
    # data = vector_db.get_collections()
    # print("###" * 15)
    # pprint(data)
    # print("###" * 15)
    # print("Current Data: ")
    # for id, documents, metadata in zip(
    #     data["ids"], data["documents"], data["metadatas"]
    # ):
    #     print(f"\n{id}\n{documents}\n{metadata}")

    #################FILTER BY....#####################################
    vector_db.filter_by_metadata("fuel", "diesel")


if __name__ == "__main__":
    main()
