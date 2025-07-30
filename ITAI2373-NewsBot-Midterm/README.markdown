# NewsBot Intelligence System

## ITAI 2373 - NLP Midterm Group Project

**Team Members**: Faiza Abdullah, Sha’Rise Griggs  
**Date**: July 29, 2025  
**Course**: ITAI 2373 Natural Language Processing (NLP)  
**GitHub Repository**: https://github.com/AbdullahFaiza/NLP-ITAI2373/ITAI2373-NewsBot-Midterm
  

---

## Project Overview

The **NewsBot Intelligence System** is an end-to-end Natural Language Processing (NLP) pipeline designed to process, categorize, and analyze news articles from the BBC News dataset. Built as part of the ITAI 2373 midterm project, this system integrates techniques from Modules 1–8, including text preprocessing, TF-IDF feature extraction, named entity recognition (NER), sentiment analysis, POS tagging, and topic modeling with Latent Dirichlet Allocation (LDA). The system addresses real-world applications such as media monitoring, business intelligence, and content management, with a Research Extension enhancing classification through topic modeling.

### Key Features
- **Text Preprocessing**: Cleans and tokenizes news articles using NLTK and SpaCy (Module 2).
- **Text Classification**: Categorizes articles into business, tech, politics, sports, entertainment, or health using RandomForest with TF-IDF features (Modules 3, 7).
- **Named Entity Recognition**: Extracts entities (e.g., people, organizations) with SpaCy (Module 8).
- **Sentiment Analysis**: Analyzes article sentiment using TextBlob (Module 6).
- **Topic Modeling**: Enhances classification with LDA topic distributions, evaluated with c_v coherence (Research Extension).
- **Visualizations**: Includes word clouds, confusion matrices, and topic distribution plots for interpretability (Modules 3, 7).
- **Business Insights**: Generates actionable insights for media monitoring, market research, and crisis management (Module 1).

### Learning Objectives
- Integrate NLP techniques from Modules 1–8 into a cohesive system.
- Design a robust text processing pipeline from raw input to insights.
- Compare machine learning algorithms (e.g., RandomForest) for classification.
- Extract structured information (entities, sentiment, topics) from unstructured text.
- Translate NLP results into business value for real-world applications.
- Collaborate effectively using GitHub and document technical results clearly.

---

## Repository Structure

```
NLP-ITAI2373/
├── Dataset/
│   └── BBC News Train.csv                                           # BBC News dataset for training and analysis
├── Original Notebook/
│   └── Midterm_NewsBot_Intelligence_System_student.ipynb            # Preliminary Notebook provided by Professor
├── Visualization/
│   └── Average Sentiment Score.png                                  # Output visualizations (e.g., word clouds, topic plots)
│   └── Average Topic Distribution across Articles.png
│   └── Category Distribution.png
│   └── Confusion Matrix-Naive Bayes.png
│   └── Distribution of News Categories.png
│   └── Distribution of Text Length.png
│   └── Named Entity Analysis.png
│   └── Overall Sentiment Distribution.png
│   └── POS Tag Proportions by News Category.png
│   └── Sentiment Analysis by Category.png
│   └── Sentiment Label Distribution by Category.png
│   └── Sentiment Polarity Trend over Time.png
│   └── Syntactic Complexity across Categories.png
│   └── TF-IDF Term Importance Across Categories.png
│   └── Top Dependency Relations.png
│   └── Top Terms.png
│   └── TOP TF-IDF Terms by Category.png
├── Midterm_NewsBot_Intelligence_System_FSMK_FaizaAbdullah.ipynb     # Main Jupyter notebook with all analyses
├── NewsBot_Reflection_Faiza&Sharise_ITA2373.pdf                     # Reflection on contributions and learnings
├── README.md                                                        # Project overview and instructions
└── requirements.txt                                                 # Python dependencies for reproducibility

```

---

## Setup and Installation

### Prerequisites
- Python 3.8+
- Jupyter Notebook
- Git

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AbdullahFaiza/NLP-ITAI2373.git
   cd NLP-ITAI2373
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download SpaCy model:
   ```bash
   python -m spacy download en_core_web_sm
   ```
4. Install NLTK data:
   ```python
   import nltk
   nltk.download(['punkt', 'stopwords', 'wordnet', 'vader_lexicon', 'averaged_perceptron_tagger', 'averaged_perceptron_tagger_eng'])
   ```

### Running the Notebook
1. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
2. Open `Midterm_NewsBot_Intelligence_System_FSMK_FaizaAbdullah.ipynb` and run all cells.
3. Ensure `BBC News Train.csv` is in the `Dataset/` folder or use the sample dataset provided in the notebook.

---

## Usage

The Jupyter notebook (`Midterm_NewsBot_Intelligence_System_FSMK_FaizaAbdullah.ipynb`) contains:
- **Data Loading**: Loads the BBC News dataset or a fallback 5-article sample.
- **Preprocessing**: Cleans text using NLTK tokenization and SpaCy lemmatization.
- **Classification**: Implements a RandomForest classifier with TF-IDF features and compares it to an enhanced LDA-based model.
- **NER and Sentiment**: Extracts entities and sentiment scores for business insights.
- **Topic Modeling**: Applies LDA to uncover thematic trends, with coherence evaluation and qualitative analysis.
- **Visualizations**: Generates word clouds, confusion matrices, and topic distribution plots.

To run specific analyses, execute individual cells or modify parameters (e.g., number of LDA topics) in the Research Extension section.

---

## Contributions

- **Faiza Abdullah**: Led project development, implemented the core `NewsBotIntelligenceSystem` class, integrated TF-IDF classification, NER, sentiment analysis, and LDA. Resolved technical issues (e.g., `numpy`/`gensim` incompatibility) and wrote comprehensive documentation.
- **Sha’Rise Griggs**: Contributed to the Research Extension, implementing LDA topic modeling, Emotional Intelligence, and Temporal Sentiment analysis. Assisted with qualitative evaluations and visualizations.

*Note*: Due to collaboration challenges, the project was completed primarily by Faiza and Sha’Rise.

---

## Results

- **Baseline Classifier (TF-IDF + RandomForest)**: Achieved high accuracy and F1-score on the BBC News dataset (exact metrics depend on dataset size).
- **Enhanced Classifier (TF-IDF + LDA)**: Improved performance for ambiguous articles by incorporating topic distributions.
- **Topic Modeling**: Identified meaningful topics (e.g., economy, technology) with a c_v coherence score in the typical range (0.3–0.7).
- **Visualizations**: Word clouds highlight key terms per category, confusion matrices show classification errors, and topic distribution plots reveal thematic trends.
- **Business Insights**: Enables media monitoring (e.g., categorizing news), market research (e.g., sentiment trends), and crisis management (e.g., flagging negative articles).

---

## Future Enhancements

- **Transformer Models**: Integrate BERT or BERTopic for improved topic modeling and classification.
- **Multi-Label Classification**: Support articles with multiple categories (e.g., tech and business).
- **Real-Time Analysis**: Incorporate social media data from platforms like X for trend detection.
- **Bias Mitigation**: Apply adversarial training to reduce dataset biases.

---

## Acknowledgments

- **Professor Patricia Mcmanus**: For guidance and feedback throughout the project.
- **References**:
  - Blei, D. M., et al. (2003). *Latent Dirichlet Allocation*. Journal of Machine Learning Research.
  - Scikit-learn documentation: *LatentDirichletAllocation* (scikit-learn.org).
  - SpaCy documentation: *Named Entity Recognition* (spacy.io).
  - TextBlob documentation: *Sentiment Analysis* (textblob.readthedocs.io).

---

## Contact

For questions or collaboration opportunities, contact:  
- **Faiza Abdullah**: faiza,abdullah79@icloud.com
