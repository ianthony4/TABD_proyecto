# Estudio Comparativo RAG Vectorial vs Tree Reasoning (PageIndex)

## 📌 Situación Actual del Proyecto (Para Agentes de IA y Desarrolladores)

Este proyecto es un entorno de pruebas automatizado (Test Harness) en Python para comparar dos enfoques de recuperación de información médica:
1. **MVP A (RAG Clásico con Embeddings):** 🟢 **100% Implementado**. Utiliza `pdfplumber`, `sentence-transformers` (all-MiniLM-L6-v2) y `ChromaDB` local para hacer búsqueda por similitud de cosenos.
2. **MVP B (Vectorless / Tree Reasoning):** 🟡 **Scaffolded (Pieza de Rompecabezas)**. El archivo `src/mvp_b_vectorless/tree_controller.py` está estructurado. Requiere conectar los endpoints y claves de la API real de PageIndex.
3. **Orquestador y Evaluador:** 🟢 **100% Implementados**. Iteran sobre un archivo `ground_truth.csv`, inyectan el contexto recuperado en el LLM y guardan los resultados en un `results.csv`.
4. **Generación con LLM:** 🟡 **Scaffolded (Pieza de Rompecabezas)**. El archivo `src/llm_client.py` contiene un mock. Requiere conectar la API de **Google MedGemma**.

## 🧩 ¿Qué falta? (To-Do para IAs futuras)

Si eres una IA analizando este proyecto o un nuevo desarrollador, estas son las "Piezas de Rompecabezas" que debes completar des-comentando y ajustando los bloques designados en el código:

- **[ ] Integrar MedGemma API:** En `src/llm_client.py`, modificar la función `generate_answer` para que haga el request POST HTTP con la API key de MedGemma a su endpoint oficial.
- **[ ] Integrar PageIndex API:** En `src/mvp_b_vectorless/tree_controller.py`, implementar la llamada POST en el método `index` para subir el PDF y otra en el método `query` para extraer el contexto del árbol de razonamiento.
- **[ ] Añadir Métricas Avanzadas:** Una vez que las respuestas sean procesadas por un LLM real, ampliar la clase estática en `src/evaluator.py` para calcular métricas como **ROUGE-L** o similitud semántica.

## 🤝 ¿Cómo puede ayudar el usuario (Investigador)?

Para que el sistema pase de una simulación a un entorno de pruebas clínico real, el investigador debe aportar:
1. **Credenciales (Tokens/Keys):** Proveer las API Keys necesarias tanto para MedGemma como para la API de PageIndex.
2. **Documentación:** Facilitar los manuales o endpoints técnicos de la API de PageIndex.
3. **Dataset Real:** Colocar el documento médico real en `data/pdfs/documento_minsa.pdf` y reemplazar las preguntas dummy de `data/ground_truth.csv` con el Cuestionario Médico validado.
