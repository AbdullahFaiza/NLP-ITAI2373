# API Reference: NewsBot Intelligence System 2.0

## Overview
This document details the API for NewsBot 2.0, implemented in `notebooks/NewsBot_2_0_Final_Project_FaizaAbdullah.ipynb`. It covers classes and functions used in the NLP pipeline.

## Classes

### TextPreprocessor (Cell 1)
- **Purpose**: Cleans and tokenizes text.
- **Methods**:
  - `clean_text(text: str) -> str`
    - **Parameters**: `text` (raw text).
    - **Returns**: Cleaned text (lowercase, no HTML/punctuation).
    - **Example**: `clean_text("Hello <b>World!</b>") -> "hello world"`.
  - `tokenize_text(text: str) -> list`
    - **Parameters**: `text` (cleaned text).
    - **Returns**: List of tokens.
    - **Example**: `tokenize_text("hello world") -> ["hello", "world"]`.

### ConversationalAgent (Cell 2)
- **Purpose**: Processes natural language queries.
- **Methods**:
  - `process_query(query: str, df: pd.DataFrame) -> pd.DataFrame`
    - **Parameters**: `query` (user query), `df` (articles with `clean_content`).
    - **Returns**: Top-5 matching articles.
    - **Example**:
      ```python
      agent = ConversationalAgent()
      results = agent.process_query("climate change news", df)
      ```

### ContentEnhancementEngine (Cell 3)
- **Purpose**: Generates summaries and insights.
- **Methods**:
  - `enhance_content(df: pd.DataFrame) -> pd.DataFrame`
    - **Parameters**: `df` (articles with `translated_content`).
    - **Returns**: DataFrame with `summary`, `insights` (e.g., `{'insight_category': 'neutral'}`).
    - **Notes**: Fixed 0% enhancement issue.

### SystemOrchestrator (Cell 4)
- **Purpose**: Coordinates pipeline components.
- **Methods**:
  - `orchestrate(df: pd.DataFrame, query: str = None) -> pd.DataFrame`
    - **Parameters**: `df` (input articles), `query` (optional query).
    - **Returns**: Processed DataFrame with translations, summaries, query results.

### TrendPredictor (Cell 7)
- **Purpose**: Analyzes trends.
- **Methods**:
  - `predict_trends(df_enhanced: pd.DataFrame) -> pd.DataFrame`
    - **Parameters**: `df_enhanced` (articles with `insights`).
    - **Returns**: DataFrame with `category`, `trend_score`, `article_count`.
    - **Notes**: Fixed parsing error with `json.loads`.

### BiasDetector (Cell 8)
- **Purpose**: Detects bias.
- **Methods**:
  - `detect_bias(df: pd.DataFrame) -> pd.DataFrame`
    - **Parameters**: `df` (articles with `translated_content`).
    - **Returns**: DataFrame with `bias_score`, `fact_check_result`.

## Functions
- `validate_pipeline(df_translated: pd.DataFrame, df_enhanced: pd.DataFrame, df_summaries: pd.DataFrame, query_results: pd.DataFrame) -> dict` (Cell 5)
  - **Parameters**: DataFrames from Cells 2–4.
  - **Returns**: Metrics (e.g., `{'Translation': 1.0}`).
  - **Example**:
    ```python
    metrics = validate_pipeline(df_translated, df_enhanced, df_summaries, query_results)
    ```

- `finetune_transformer(df_translated: pd.DataFrame = None, model_name: str = "distilbert-base-uncased", wandb_api_key: str = None) -> pd.DataFrame` (Cell 6)
  - **Parameters**: `df_translated`, `model_name`, `wandb_api_key`.
  - **Returns**: DataFrame with `finetuned_category`.
  - **Notes**: Fixed `eval_strategy` error.

## Usage Notes
- **Dependencies**: See `requirements.txt`.
- **Configuration**: Adjust `CONFIG` in Cell 1 for paths, models.
- **Error Handling**: Check `outputs/logs.txt` for debugging.