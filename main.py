import os
import pandas as pd
from src.mvp_a_vectorial.vector_controller import VectorRAGController
from src.orchestrator import ExperimentOrchestrator

def main():
    """
    Punto de entrada principal.
    Crea archivos de prueba (si no existen), inicializa el orquestador con MVP A y ejecuta el estudio.
    """
    # Rutas
    data_dir = "data"
    pdfs_dir = os.path.join(data_dir, "pdfs")
    pdf_path = os.path.join(pdfs_dir, "documento_minsa_dummy.pdf")
    dataset_path = os.path.join(data_dir, "ground_truth.csv")
    output_path = os.path.join(data_dir, "results.csv")

    # Crear directorios si no existen por si acaso
    os.makedirs(pdfs_dir, exist_ok=True)

    # Crear datos dummy si no existen
    if not os.path.exists(dataset_path):
        print(f"Creando dataset dummy en {dataset_path}...")
        df_dummy = pd.DataFrame({
            "id": [1, 2],
            "question": ["¿Cuáles son los síntomas principales?", "¿Cuál es el tratamiento recomendado?"],
            "expected_answer": ["Fiebre y dolor.", "Reposo y paracetamol."]
        })
        df_dummy.to_csv(dataset_path, index=False)

    if not os.path.exists(pdf_path):
        print(f"ATENCIÓN: Falta el archivo {pdf_path}.")
        print("Por favor, coloca un archivo PDF real en esa ruta para que el Chunker pueda procesarlo.")
        print("Creando un PDF vacío de simulación fallará con pdfplumber si no es un PDF válido.")
        print("Te recomendamos colocar un PDF y volver a ejecutar.\n")
        # No intentamos crear un PDF válido manualmente aquí por simplicidad

    # 1. Inicializar el retriever elegido (MVP A)
    print("Inicializando MVP A (RAG Vectorial)...")
    # Nota: Si el PDF no existe fallará en el pdfplumber, pero el código está estructurado.
    mvp_a = VectorRAGController(chunk_size=500, overlap=100, top_k=2)

    # 2. Inicializar el orquestador pasándole el MVP
    orchestrator = ExperimentOrchestrator(retriever=mvp_a)

    # 3. Ejecutar experimento si el PDF existe
    if os.path.exists(pdf_path):
        orchestrator.run_experiment(
            pdf_path=pdf_path,
            dataset_path=dataset_path,
            output_path=output_path
        )
    else:
        print("Ejecución detenida: Falta archivo PDF de prueba.")

if __name__ == "__main__":
    main()
