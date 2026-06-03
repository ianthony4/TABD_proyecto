from src.interfaces.retriever_interface import BaseRetriever
from src.mvp_a_vectorial.chunker import DocumentChunker
from src.mvp_a_vectorial.embedder import VectorEmbedder

class VectorRAGController(BaseRetriever):
    """
    Controlador que implementa MVP A (RAG Vectorial tradicional).
    Conecta la lógica de división de texto (Chunker) y almacenamiento vectorial (Embedder).
    """

    def __init__(self, chunk_size: int = 1000, overlap: int = 200, top_k: int = 3):
        """
        Inicializa los componentes de chunking y base de datos vectorial.

        Args:
            chunk_size (int): Tamaño de caracteres por chunk.
            overlap (int): Superposición de caracteres entre chunks.
            top_k (int): Cantidad de fragmentos a recuperar en la búsqueda.
        """
        self.chunker = DocumentChunker(chunk_size=chunk_size, overlap=overlap)
        self.embedder = VectorEmbedder()
        self.top_k = top_k
        self.is_indexed = False

    def index(self, pdf_path: str) -> None:
        """
        Implementa la interfaz BaseRetriever. Lee, divide y almacena los embeddings de un PDF.

        Args:
            pdf_path (str): Ruta al PDF.
        """
        print(f"[MVP A] Indexando documento: {pdf_path}")
        chunks = self.chunker.process_pdf(pdf_path)
        print(f"[MVP A] Extraídos {len(chunks)} chunks. Generando embeddings...")
        self.embedder.add_chunks(chunks)
        self.is_indexed = True
        print("[MVP A] Indexación completada en ChromaDB local.")

    def query(self, question: str) -> str:
        """
        Implementa la interfaz BaseRetriever. Busca y retorna el contexto relevante.

        Args:
            question (str): Pregunta del usuario.

        Returns:
            str: Texto concatenado con la información más relevante recuperada.
        """
        if not self.is_indexed:
            raise RuntimeError("Debes indexar un documento antes de realizar consultas.")
            
        print(f"[MVP A] Recuperando contexto para la pregunta: '{question}'")
        retrieved_chunks = self.embedder.search(question, top_k=self.top_k)
        
        # Concatenar los chunks recuperados
        context = "\n\n".join(retrieved_chunks)
        return context
