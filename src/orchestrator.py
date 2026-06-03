import pandas as pd
from typing import Optional
from src.interfaces.retriever_interface import BaseRetriever
from src.llm_client import MockMedGemmaClient

class ExperimentOrchestrator:
    """
    Controlador central del experimento.
    Se encarga de inyectar el MVP deseado, leer las preguntas del Ground Truth,
    ejecutar la prueba de extremo a extremo y guardar los resultados.
    """

    def __init__(self, retriever: BaseRetriever):
        """
        Inicializa el orquestador inyectando el retriever a evaluar (MVP A o MVP B).

        Args:
            retriever (BaseRetriever): Instancia que implementa la lógica de recuperación.
        """
        self.retriever = retriever
        self.llm_client = MockMedGemmaClient()

    def run_experiment(self, pdf_path: str, dataset_path: str, output_path: str) -> None:
        """
        Ejecuta el pipeline completo de evaluación.

        Args:
            pdf_path (str): Ruta al PDF del MINSA a indexar.
            dataset_path (str): Ruta al archivo CSV con las preguntas ground_truth.
            output_path (str): Ruta donde se guardará el CSV de resultados.
        """
        print("\n=== INICIANDO EXPERIMENTO ===")
        
        # 1. Indexar Documento
        print("\n--- Fase 1: Indexación ---")
        self.retriever.index(pdf_path)
        
        # 2. Cargar Dataset
        print("\n--- Fase 2: Ejecución de Preguntas ---")
        try:
            df = pd.read_csv(dataset_path)
            print(f"Cargadas {len(df)} preguntas del dataset '{dataset_path}'.")
        except FileNotFoundError:
            print(f"Error: No se encontró el dataset en {dataset_path}")
            return
            
        results = []

        # 3. Iterar sobre preguntas
        for index, row in df.iterrows():
            question_id = row.get("id", index)
            question = row.get("question", "")
            expected_answer = row.get("expected_answer", "")
            
            print(f"\nProcesando Pregunta ID {question_id}: {question}")
            
            # 3.1 Recuperar contexto
            context = self.retriever.query(question)
            
            # 3.2 Generar respuesta con LLM (Mock)
            generated_answer = self.llm_client.generate_answer(question, context)
            print(f"Respuesta generada: {generated_answer}")
            
            # 3.3 Guardar resultado parcial
            results.append({
                "id": question_id,
                "question": question,
                "expected_answer": expected_answer,
                "generated_answer": generated_answer,
                "retrieved_context": context
            })
            
        # 4. Guardar resultados
        print("\n--- Fase 3: Exportación de Resultados ---")
        results_df = pd.DataFrame(results)
        results_df.to_csv(output_path, index=False)
        print(f"Resultados exportados exitosamente a '{output_path}'.")
        print("=== EXPERIMENTO FINALIZADO ===\n")
