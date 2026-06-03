from abc import ABC, abstractmethod

class BaseRetriever(ABC):
    """
    Clase abstracta que define la interfaz para los componentes de recuperación de información.
    Garantiza que tanto MVP A (RAG Vectorial) como MVP B (Tree Reasoning) tengan la misma firma.
    """

    @abstractmethod
    def index(self, pdf_path: str) -> None:
        """
        Lee y procesa un documento PDF para indexarlo en la base de datos o estructura correspondiente.

        Args:
            pdf_path (str): Ruta absoluta o relativa al archivo PDF.
        """
        pass

    @abstractmethod
    def query(self, question: str) -> str:
        """
        Dado una pregunta, recupera el contexto más relevante del documento indexado.

        Args:
            question (str): Pregunta formulada por el usuario.

        Returns:
            str: Contexto recuperado concatenado.
        """
        pass
