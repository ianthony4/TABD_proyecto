import pandas as pd

class Evaluator:
    """
    Clase para calcular métricas de evaluación del modelo (Ej: Exact Match, ROUGE).
    Actualmente contiene implementaciones base para expandirse posteriormente.
    """

    @staticmethod
    def calculate_exact_match(results_path: str) -> float:
        """
        Calcula el porcentaje de respuestas que coinciden exactamente con el expected_answer.
        (Métrica estricta, normalmente se prefiere usar similitud de embeddings o ROUGE).

        Args:
            results_path (str): Ruta al archivo de resultados CSV.

        Returns:
            float: Porcentaje de acierto (0.0 a 1.0).
        """
        df = pd.read_csv(results_path)
        
        if len(df) == 0:
            return 0.0
            
        matches = 0
        for _, row in df.iterrows():
            expected = str(row.get('expected_answer', '')).strip().lower()
            generated = str(row.get('generated_answer', '')).strip().lower()
            
            if expected and expected == generated:
                matches += 1
                
        return matches / len(df)
