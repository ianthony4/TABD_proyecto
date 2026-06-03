import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
from typing import List

class VectorEmbedder:
    """
    Clase encargada de generar embeddings y manejar la conexión local con ChromaDB.
    """

    def __init__(self, collection_name: str = "mvp_a_collection"):
        """
        Inicializa el modelo de embeddings y la base de datos ChromaDB local.

        Args:
            collection_name (str): Nombre de la colección en ChromaDB.
        """
        # Inicializar modelo de SentenceTransformers
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Inicializar ChromaDB en memoria (se destruye al finalizar)
        self.client = chromadb.Client(Settings(is_persistent=False))
        
        # Crear o recuperar colección (usamos cosine distance)
        self.collection = self.client.get_or_create_collection(
            name=collection_name, 
            metadata={"hnsw:space": "cosine"}
        )

    def add_chunks(self, chunks: List[str]) -> None:
        """
        Convierte una lista de chunks en embeddings y los guarda en ChromaDB.

        Args:
            chunks (List[str]): Lista de textos a indexar.
        """
        if not chunks:
            return
            
        embeddings = self.model.encode(chunks).tolist()
        
        # Generar IDs simples
        ids = [f"chunk_{i}" for i in range(len(chunks))]
        
        self.collection.add(
            embeddings=embeddings,
            documents=chunks,
            ids=ids
        )

    def search(self, query: str, top_k: int = 3) -> List[str]:
        """
        Realiza una búsqueda vectorial a partir de una pregunta para encontrar los chunks más relevantes.

        Args:
            query (str): Pregunta de búsqueda.
            top_k (int): Cantidad de chunks relevantes a devolver.

        Returns:
            List[str]: Lista de los contextos (documentos) recuperados.
        """
        query_embedding = self.model.encode([query]).tolist()
        
        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=top_k
        )
        
        if not results['documents']:
            return []
            
        return results['documents'][0]
