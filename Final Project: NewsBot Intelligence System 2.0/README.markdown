# NewsBot Intelligence System 2.0

## ITAI 2373 - NLP Final Project

**Submittef By**: Faiza Abdullah

**Date**: August 7, 2025 

**Course**: ITAI 2373 Natural Language Processing (NLP)  

**GitHub Repository**: https://github.com/AbdullahFaiza/NLP-ITAI2373/edit/main/Final%20Project%3A%20NewsBot%20Intelligence%20System%202.0/README.markdown
  

---
## Overview
NewsBot 2.0 is an advanced Natural Language Processing (NLP) platform designed for analyzing, summarizing, and generating insights from multilingual news articles. Developed as the final project for ITAI 2373 - Natural Language Processing, this system builds upon the midterm NewsBot by integrating sophisticated NLP techniques, including transformer fine-tuning, topic modeling, multilingual processing, and conversational interfaces. Implemented in `NewsBot_2_0_Final_Project_FaizaAbdullah.ipynb`, it processes a dataset of 39 articles (English, Spanish, French) to deliver actionable intelligence for media organizations, analysts, and businesses.

### Key Features
- **Multilingual Analysis**: Translates articles using M2M100 (`facebook/m2m100_418M`), achieving 100% success for 39 articles (`translated_articles.csv`).
- **Content Enhancement**: Generates summaries (BART) and insights (e.g., neutral: 53.85%, negative_media: 46.15%) in `enhanced_articles.csv`.
- **Trend Prediction**: Identifies trends via `TrendPredictor`, visualized in `trend_prediction.png`.
- **Conversational Interface**: Supports queries (e.g., "Latest climate change news") using semantic search (`sentence-transformers`).
- **Fine-tuning**: Fine-tunes `distilbert-base-uncased` with Wandb logging, producing `finetuned_articles.csv`.
- **Validation**: Achieves 100% success in translation, summarization, and enhancement (`validation_results.png`).

### Project Structure
```
ITAI2373/
Final Project: NewsBot Intelligence System 2.0/
├── README.md                                          # Comprehensive project overview
├── requirements.txt                                   # All dependencies with versions
├── config/
│   ├── settings.py                                    # Configuration management
│   └── api_keys_template.txt                          # API key template (no real keys!)
├── src/
│   ├── data_processing/
│   │   ├── text_preprocessor.py                        # Enhanced from midterm
│   │   ├── feature_extractor.py                        # TF-IDF, embeddings, custom features
│   │   └── data_validator.py                           # Data quality checks
│   ├── analysis/
│   │   ├── classifier.py                               # Enhanced classification system
│   │   ├── sentiment_analyzer.py                        # Advanced sentiment analysis
│   │   ├── ner_extractor.py                              # Named entity recognition
│   │   └── topic_modeler.py                              # LDA/NMF implementation
│   ├── language_models/
│   │   ├── summarizer.py                                 # Text summarization
│   │   ├── generator.py                                    # Content generation
│   │   └── embeddings.py                                 # Semantic embeddings
│   ├── multilingual/
│   │   ├── translator.py                                 # Translation services
│   │   ├── language_detector.py                           # Language identification
│   │   └── cross_lingual_analyzer.py                     # Cross-language analysis
│   ├── conversation/
│   │   ├── query_processor.py                           # Natural language query handling
│   │   ├── intent_classifier.py                           # Intent detection
│   │   └── response_generator.py                        # Response generation
├── NewsBot_2_0_Final_Project_FaizaAbdullah.ipynb      # Main Jupyter notebook with all analyses
├── Docs/
│   ├── technical_documentation.md                     # Detailed technical specs
│   ├── user_guide.md                                  # End-user instructions
│   ├── api_reference.md                               # API documentation
│   └── deployment_instructions.md                     # Production deployment
├── Reports/
│   ├── FP_TechnicalDoc_Faiza_Abdullah_ITAI2373.pdf      # Detailed technical analysis
│   ├── FP_ExecutiveSummary_Faiza_Abdullah_ITAI2373.pdf   # Business-focused overview
│   ├── FP_ReflectionJournal_Faiza_Abdullah_ITAI2373.pdf
│   ├── presentation_slides.pptx                           # Slide deck for project presentation
│   ├── presentation_slides.pdf                            # PDF version of slides
│   └── presentation_video.mp4                             # Video walkthrough of the system
├── Visualization/
│   └── Article Category Distribution.png                  # Output visualizations (e.g., word clouds, bar charts etc.)
│   └── Bonus - Bias Detection Distribution.png                                  
│   └── Bonus - Trend Prediction by Insight Category.png
│   └── Entity Relation Knowledge Graph.png
│   └── Insight Category Distribution.png
│   └── Language Distribution of Articles.png
│   └── Pipeline Validation Success Rate.png
│   └── Sentiments Trends Over Time.png
│   └── Top Query Matches.png
│   └── Top Similar Articles by Cosine.png
│   └── Topic 0 using Word Cloud.png
│   └── Topic 1 using Word Cloud.png
│   └── Topic 2 using Word Cloud.png
│   └── Topic 3 using Word Cloud.png
└── └── Topic 4 using Word Cloud.png

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

---

## Contact

For questions or collaboration opportunities, contact:  
- **Faiza Abdullah**: faiza.abdullah79@icloud.com
