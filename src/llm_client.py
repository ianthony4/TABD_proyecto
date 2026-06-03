class MockMedGemmaClient:
    """
    Cliente simulado para interactuar con la API del LLM (Google MedGemma a futuro).
    Preparado como pieza de rompecabezas.
    """
    
    def generate_answer(self, question: str, context: str) -> str:
        """
        Genera una respuesta invocando al LLM (MedGemma) pasándole el contexto y la pregunta.

        Args:
            question (str): La pregunta original.
            context (str): El contexto recuperado por el MVP.

        Returns:
            str: Respuesta generada por el LLM.
        """
        print("[LLM Client] Llamando al modelo (MedGemma)...")
        
        # =========================================================
        # 🧩 ROMPECABEZAS: Código real de integración con MedGemma
        # =========================================================
        # import os
        # import requests
        # medgemma_api_key = os.getenv("MEDGEMMA_API_KEY", "TU_API_KEY_AQUI")
        # prompt = f"Contexto:\\n{context}\\n\\nPregunta: {question}\\nRespuesta:"
        # headers = {'Authorization': f'Bearer {medgemma_api_key}'}
        # payload = {'prompt': prompt, 'max_tokens': 500}
        # response = requests.post("https://api.medgemma.ejemplo.com/generate", json=payload, headers=headers)
        # if response.status_code == 200:
        #     return response.json().get('response', '')
        # =========================================================
        
        # Simulación mientras no se tenga el API real
        context_preview = context[:50].replace('\n', ' ')
        if len(context) > 50:
            context_preview += "..."
            
        return f"Respuesta simulada de MedGemma basada en: [{context_preview}]"
