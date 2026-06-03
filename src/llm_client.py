class MockMedGemmaClient:
    """
    Cliente simulado para interactuar con la API del LLM (Google MedGemma a futuro).
    """
    
    def generate_answer(self, question: str, context: str) -> str:
        """
        Simula una petición HTTP al LLM pasándole el contexto recuperado y la pregunta.

        Args:
            question (str): La pregunta original.
            context (str): El contexto recuperado por el MVP.

        Returns:
            str: Respuesta simulada generada por el LLM.
        """
        print("[LLM Mock] Simulando petición al modelo...")
        
        # Tomamos solo los primeros 50 caracteres del contexto para el log/respuesta simulada
        context_preview = context[:50].replace('\n', ' ')
        if len(context) > 50:
            context_preview += "..."
            
        return f"Respuesta generada basada en: [{context_preview}]"
