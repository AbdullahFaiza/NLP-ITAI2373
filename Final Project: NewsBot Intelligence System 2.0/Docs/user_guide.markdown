# User Guide: NewsBot Intelligence System 2.0

## Introduction
NewsBot 2.0 is a user-friendly NLP platform for analyzing news articles in multiple languages. This guide explains how to use the system to query news, view trends, and access insights, implemented in notebook `NewsBot_2_0_Final_Project_FaizaAbdullah.ipynb`.

## Getting Started
1. **Access the System**:
   - Open the notebook in Google Colab (https://colab.research.google.com/).
   - Upload `NewsBot_2_0_Final_Project_FaizaAbdullah.ipynb`.
2. **Upload Dataset**:
   - Place `cleaned_articles.csv` (39 articles) in `/content/data/`.
3. **Run the Notebook**:
   - Click *Runtime > Run all* (Ctrl+F9).
   - Wait ~20–30 minutes (CPU) or ~10–15 minutes (GPU).
   - Outputs appear in `/content/data/` and `/content/outputs/`.

## Using NewsBot 2.0
### Querying News
- **How**: In Cell 2, modify the query (e.g., `"Latest climate change news"`).
- **Example**:
  ```python
  agent = ConversationalAgent()
  df = pd.read_csv('data/cleaned_articles.csv')
  results = agent.process_query("tech news 2025", df)
  print(results.head())
  ```
- **Output**: Top-5 articles matching the query, saved as `query_matches.png`.

### Viewing Trends
- **How**: Cell 7 generates trend predictions.
- **Output**: 
  - `trend_predictions.csv`: Shows categories (e.g., neutral: 53.85%, negative_media: 46.15%).
  - `trend_prediction.png`: Visualizes trends.
- **Access**: Download from `/content/outputs/`.

### Accessing Insights
- **How**: Cell 3 produces summaries and insights.
- **Output**: `enhanced_articles.csv` with `summary` and `insights` (e.g., `{'insight_category': 'neutral'}`).
- **View**: Open `enhanced_articles.csv` in Excel or a text editor.

### Validation Results
- **How**: Cell 5 validates pipeline performance.
- **Output**: `validation_results.png` shows 100% success for translation, summarization, enhancement.
- **Access**: Download from `/content/outputs/`.

## Troubleshooting
- **No Outputs**: Re-run Cells 1–9 and check `outputs/logs.txt` for errors.
- **Git Error**: If saving fails, contact the administrator to run the `metadata.widgets` cleaning script.
- **Slow Processing**: Switch to GPU in Colab (*Runtime > Change runtime type > GPU*).
- **Contact**: Faiza Abdullah at faiza.abdullah79"icloud.com.

## System Outputs
- **Data Files**: `translated_articles.csv`, `enhanced_articles.csv`, `finetuned_articles.csv`, `trend_predictions.csv`.
- **Visualizations**: `query_matches.png`, `trend_prediction.png`, `validation_results.png`.
- **Logs**: `outputs/logs.txt` (e.g., `Sample insights`).
