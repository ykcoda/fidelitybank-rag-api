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

    def add_document(self, ids: list[str], documents: list[str]):
        self.collection.add(ids=ids, documents=documents)
        print(f"New documents added to {self.collection_name} collection")

    def query_collection(self, q: str, n_results: int = 1):
        return self.collection.query(query_texts=[q], n_results=n_results)

    def get_collections(self):
        return self.collection.get()


def main():
    vector_db = VectorDB(collection_name="fbl_documents", path="db")

    # vector_db.add_document(
    #     ["car1", "plane1", "boat1", "bus1"],
    #     [
    #         "Car runs on land",
    #         "Plane flies in the sly",
    #         "Boat travels on water",
    #         "Bus is public trasport on road",
    #     ],
    # )
    query = input("Type your query: ")
    results = vector_db.query_collection(query, n_results=2)
    pprint(results)

    print("###" * 15)
    pprint(f"Available collection: {vector_db.get_collections()}")


if __name__ == "__main__":
    main()
