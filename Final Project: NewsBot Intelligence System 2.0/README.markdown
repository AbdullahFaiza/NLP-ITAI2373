# NewsBot Intelligence System 2.0

## Overview
NewsBot 2.0 is an advanced Natural Language Processing (NLP) platform designed for analyzing, summarizing, and generating insights from multilingual news articles. Developed as the final project for ITAI 2373 - Natural Language Processing, this system builds upon the midterm NewsBot by integrating sophisticated NLP techniques, including transformer fine-tuning, topic modeling, multilingual processing, and conversational interfaces. Implemented in `notebooks/NewsBot_2_0_Final_Project_FaizaAbdullah.ipynb`, it processes a dataset of 39 articles (English, Spanish, French) to deliver actionable intelligence for media organizations, analysts, and businesses.

### Key Features
- **Multilingual Analysis**: Translates articles using M2M100 (`facebook/m2m100_418M`), achieving 100% success for 39 articles (`translated_articles.csv`).
- **Content Enhancement**: Generates summaries (BART) and insights (e.g., neutral: 53.85%, negative_media: 46.15%) in `enhanced_articles.csv`.
- **Trend Prediction**: Identifies trends via `TrendPredictor`, visualized in `trend_prediction.png`.
- **Conversational Interface**: Supports queries (e.g., "Latest climate change news") using semantic search (`sentence-transformers`).
- **Fine-tuning**: Fine-tunes `distilbert-base-uncased` with Wandb logging, producing `finetuned_articles.csv`.
- **Validation**: Achieves 100% success in translation, summarization, and enhancement (`validation_results.png`).

### Project Structure
```
ITAI2373-NewsBot-Final/
├── README.md
├── requirements.txt
├── config/
│   ├── settings.py
│   └── api_keys_template.txt
├── src/
│   ├── data_processing/
│   │   ├── text_preprocessor.py
│   │   ├── feature_extractor.py
│   │   └── data_validator.py
│   ├── analysis/
│   │   ├── classifier.py
│   │   ├── sentiment_analyzer.py
│   │   ├── ner_extractor.py
│   │   └── topic_modeler.py
│   ├── language_models/
│   │   ├── summarizer.py
│   │   ├── generator.py
│   │   └── embeddings.py
│   ├── multilingual/
│   │   ├── translator.py
│   │   ├── language_detector.py
│   │   └── cross_lingual_analyzer.py
│   ├── conversation/
│   │   ├── query_processor.py
│   │   ├── intent_classifier.py
│   │   └── response_generator.py
│   └── utils/
│       ├── visualization.py           # Scripts for generating plots like trend_prediction.png
│       ├── evaluation.py
│       └── export.py
├── notebooks/
│   └── NewsBot_2_0_Final_Project_FaizaAbdullah.ipynb
├── tests/
│   ├── test_preprocessing.py
│   ├── test_classification.py
│   ├── test_topic_modeling.py
│   └── test_integration.py
├── data/
│   ├── raw/
│   ├── processed/
│   ├── models/
│   └── results/
├── docs/
│   ├── technical_documentation.md
│   ├── user_guide.md
│   ├── api_reference.md
│   └── deployment_instructions.md
├── reports/
│   ├── executive_summary.doc
│   ├── technical_report.doc
│   ├── reflective_journal.doc
│   ├── presentation_slides.pptx      # Slide deck for project presentation
│   ├── presentation_slides.pdf       # PDF version of slides
│   └── presentation_video.mp4        # Video walkthrough of the system
├── snapshot/
│   └── repository_snapshot.png       # Snapshot of the repository structure
```

## Installation
1. **Clone Repository**:
   ```bash
   git clone https://github.com/<your-username>/ITAI2373-NewsBot-Final.git
   cd ITAI2373-NewsBot-Final
   ```
2. **Set Up Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure Wandb API**:
   - Add your Wandb API key to `config/api_keys_template.txt` or set:
     ```bash
     export WANDB_API_KEY='caf3b27fcb1507b0a0cfcd31a9dab2ec98670ad5'
     ```
5. **Download NLTK Data**:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('punkt_tab')
   nltk.download('stopwords')
   ```
6. **Prepare Dataset**:
   - Place `cleaned_articles.csv` (39 articles with `clean_content`) in `data/`.

## Usage
1. **Run Notebook**:
   - Open `notebooks/NewsBot_2_0_Final_Project_FaizaAbdullah.ipynb` in Jupyter or Colab.
   - Run all cells (Ctrl+F9 in Colab) to process articles and generate outputs:
     - `data/translated_articles.csv`
     - `data/enhanced_articles.csv`
     - `data/finetuned_articles.csv`
     - `data/trend_predictions.csv`
     - `outputs/trend_prediction.png`
     - `outputs/validation_results.png`
2. **Example Query**:
   ```python
   agent = ConversationalAgent()
   df = pd.read_csv('data/cleaned_articles.csv')
   results = agent.process_query("Latest climate change news", df)
   print(results.head())
   ```
3. **View Logs**:
   - Check `outputs/logs.txt` for debugging (e.g., `Sample insights`, `Trend prediction error`).

## Challenges Overcome
- **Enhancement Error**: Fixed 0% success rate in Cell 5 by ensuring valid `insight_category` in Cell 3.
- **Fine-tuning Issue**: Resolved `evaluation_strategy` error in Cell 6 by using `eval_strategy`.
- **Trend Prediction**: Fixed `'str' object has no attribute 'get'` in Cell 7 with `json.loads`.
- **Git Compatibility**: Removed `metadata.widgets` to resolve notebook saving error.

## Contributing
Contributions are welcome! Please:
1. Fork the repository.
2. Create a branch (`git checkout -b feature-branch`).
3. Commit changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License
MIT License. See `LICENSE` for details.

## Contact
For issues or inquiries, contact Faiza Abdullah at [your-email@example.com].

## Repository Snapshot
A snapshot of the current repository structure is available in `snapshot/repository_snapshot.png`, providing a visual overview of the project organization.