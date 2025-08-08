# Configuration settings for NewsBot 2.0
import os

# Ensure output directories exist
os.makedirs("data", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# Configuration dictionary
CONFIG = {
    "paths": {
        "input_data": "data/cleaned_articles.csv",
        "translated_data": "data/translated_articles.csv",
        "summaries_data": "data/summaries.csv",
        "enhanced_data": "data/enhanced_articles.csv",
        "finetuned_data": "data/finetuned_articles.csv",
        "trend_data": "data/trend_predictions.csv",
        "bias_data": "data/biased_articles.csv",
        "few_shot_data": "data/few_shot_articles.csv",
        "query_plot": "outputs/query_matches.png",
        "validation_plot": "outputs/validation_results.png",
        "log_file": "outputs/logs.txt"
    },
    "models": {
        "translation": "facebook/m2m100_418M",
        "summarization": "facebook/bart-large-cnn",
        "sentiment": "distilbert/distilbert-base-uncased-finetuned-sst-2-english",
        "embedding": "sentence-transformers/all-MiniLM-L6-v2",
        "intent": "distilbert/distilbert-base-uncased-finetuned-sst-2-english"
    },
    "hyperparameters": {
        "num_topics": 5,  # LDA topics
        "num_train_epochs": 3,  # Fine-tuning epochs
        "batch_size": 8,  # Fine-tuning batch size
        "timeout_seconds": 60  # Summarization timeout
    },
    "wandb": {
        "project_name": "newsbot2_finetuning"
    }
}

# API key placeholder (load from api_keys_template.txt or environment)
WANDB_API_KEY = os.getenv("WANDB_API_KEY", None)

# Logging configuration
LOGGING_CONFIG = {
    "filename": CONFIG["paths"]["log_file"],
    "level": "INFO",
    "format": "%(asctime)s - %(levelname)s - %(message)s"
}