import pdfplumber
from typing import List

class DocumentChunker:
    """
    Clase encargada de leer un PDF y dividir su texto en fragmentos (chunks) superpuestos.
    """

    def __init__(self, chunk_size: int = 1000, overlap: int = 200):
        """
        Inicializa el chunker con los parámetros de tamaño y superposición.

        Args:
            chunk_size (int): Cantidad máxima de caracteres por chunk.
            overlap (int): Cantidad de caracteres que se superponen entre chunks adyacentes.
        """
        self.chunk_size = chunk_size
        self.overlap = overlap

    def extract_text(self, pdf_path: str) -> str:
        """
        Extrae todo el texto de un PDF dado.

        Args:
            pdf_path (str): Ruta al PDF.

        Returns:
            str: Texto completo extraído del documento.
        """
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text

    def chunk_text(self, text: str) -> List[str]:
        """
        Divide un texto completo en chunks con base en chunk_size y overlap.

        Args:
            text (str): El texto a dividir.

        Returns:
            List[str]: Lista de fragmentos de texto.
        """
        chunks = []
        start = 0
        text_length = len(text)

        while start < text_length:
            end = min(start + self.chunk_size, text_length)
            chunks.append(text[start:end])
            if end == text_length:
                break
            # Avanza menos del tamaño total del chunk para crear superposición
            start += (self.chunk_size - self.overlap)
        
        return chunks

    def process_pdf(self, pdf_path: str) -> List[str]:
        """
        Extrae y divide el texto de un PDF en una sola operación.

        Args:
            pdf_path (str): Ruta al PDF.

        Returns:
            List[str]: Lista de fragmentos de texto procesados.
        """
        text = self.extract_text(pdf_path)
        return self.chunk_text(text)
