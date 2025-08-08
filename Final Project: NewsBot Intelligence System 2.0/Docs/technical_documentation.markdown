# Technical Documentation: NewsBot Intelligence System 2.0

## Overview
NewsBot 2.0 is an advanced Natural Language Processing (NLP) platform for analyzing multilingual news articles, implemented in notebook `NewsBot_2_0_Final_Project_FaizaAbdullah.ipynb`. It processes 39 articles (`data/cleaned_articles.csv`, 13 each in English, Spanish, French) to deliver insights, summaries, trends, and query responses. This document details the system architecture, implementation, and technical resolutions for the ITAI 2373 final project.

## System Architecture
NewsBot 2.0 comprises four modules:

- **Module A: Advanced Content Analysis Engine** (Cells 3, 7)
  - **Components**: Topic modeling (LDA), sentiment analysis (DistilBERT), insight generation.
  - **Outputs**: `enhanced_articles.csv`, `trend_predictions.csv`, `trend_prediction.png`.
- **Module B: Language Understanding and Generation** (Cells 3, 6, 9)
  - **Components**: Summarization (BART), fine-tuning (DistilBERT), few-shot learning.
  - **Outputs**: `summaries.csv`, `finetuned_articles.csv`, `few_shot_articles.csv`.
- **Module C: Multilingual Intelligence** (Cell 4)
  - **Components**: Translation (M2M100), language detection (`langdetect`).
  - **Outputs**: `translated_articles.csv`.
- **Module D: Conversational Interface** (Cell 2)
  - **Components**: Query processing (`sentence-transformers`).
  - **Outputs**: `query_matches.png`.

### Component Interactions
1. **Cell 1 (Setup)**: Initializes dependencies and `CONFIG` (paths, models).
2. **Cell 2**: `ConversationalAgent` processes queries using semantic search.
3. **Cell 3**: `ContentEnhancementEngine` generates summaries and insights (`insight_category`, e.g., neutral, negative_media).
4. **Cell 4**: `SystemOrchestrator` coordinates translation, summarization, and queries.
5. **Cell 5**: `validate_pipeline` reports 100% success for translation, summarization, enhancement.
6. **Cell 6**: `finetune_transformer` fine-tunes DistilBERT with Wandb logging.
7. **Cell 7**: `TrendPredictor` computes trends (neutral: 53.85%, negative_media: 46.15%).
8. **Cell 8**: `BiasDetector` performs mock bias scoring.
9. **Cell 9**: Applies few-shot learning for summarization.

Data flows: `cleaned_articles.csv` → `translated_articles.csv` → `enhanced_articles.csv` → `finetuned_articles.csv` → `trend_predictions.csv`.

## Implementation Details
- **Dataset**: 39 articles (`clean_content`, `en: 13, es: 13, fr: 13`).
- **Preprocessing**: `TextPreprocessor` (Cell 1) uses `nltk` for tokenization, stop word removal.
- **Models**:
  - Translation: `facebook/m2m100_418M`.
  - Summarization: `facebook/bart-large-cnn`.
  - Sentiment/Fine-tuning: `distilbert-base-uncased`.
  - Embeddings: `sentence-transformers/all-MiniLM-L6-v2`.
- **Validation**: Cell 5 reports metrics (Table 1).

**Table 1: Validation Metrics**
| Metric            | Success Rate (%) |
|-------------------|------------------|
| Translation       | 100.0            |
| Summarization     | 100.0            |
| Enhancement       | 100.0            |
| Query Processing  | 100.0            |

- **Logging**: `outputs/logs.txt` captures errors (e.g., `Sample insights`).
- **Compute**: ~20–30 minutes on CPU, ~10–15 minutes on GPU (Colab).

## Error Resolutions
- **Enhancement (0%)**: Fixed by ensuring valid `insight_category` in Cell 3.
- **Fine-tuning**: Replaced `evaluation_strategy` with `eval_strategy` in Cell 6 (`transformers>=4.28.0`).
- **Trend Prediction**: Fixed `'str' object has no attribute 'get'` in Cell 7 using `json.loads`.
- **Git Error**: Removed `metadata.widgets` with cleaning script, set `matplotlib.use('Agg')`.

## Scalability Considerations
- **Cloud Deployment**: AWS EC2 or Colab with GPU for faster processing.
- **Caching**: Store models in `data/models/` to avoid re-downloads.
- **Batch Processing**: Adjust `per_device_train_batch_size` (Cell 6) for larger datasets.
