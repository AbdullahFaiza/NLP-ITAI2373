# Deployment Instructions: NewsBot Intelligence System 2.0

## Overview
This guide details the steps to deploy NewsBot 2.0, implemented in the notebook `NewsBot_2_0_Final_Project_FaizaAbdullah.ipynb`, as a production-ready NLP platform. The system can be deployed on Google Colab for development or AWS EC2 for scalable production use. It processes multilingual news articles, delivering insights, trends, and query responses.

## Prerequisites
- **System**: Linux (Ubuntu 20.04 recommended) or Google Colab.
- **Python**: 3.8+.
- **Dependencies**: Listed in `requirements.txt`.
- **Wandb API Key**: Obtain from https://wandb.ai/ (default: `caf3b27fcb1507b0a0cfcd31a9dab2ec98670ad5`).
- **Dataset**: `data/cleaned_articles.csv` (39 articles with `clean_content`).
- **AWS Account** (optional for EC2 deployment).

## Deployment on Google Colab
1. **Access Colab**:
   - Open https://colab.research.google.com/.
   - Upload `NewsBot_2_0_Final_Project_FaizaAbdullah.ipynb`.
2. **Install Dependencies**:
   - Run Cell 1 to install packages:
     ```python
     !pip install -r requirements.txt
     ```
3. **Configure Wandb**:
   - Set API key in Cell 1 or environment:
     ```bash
     export WANDB_API_KEY='caf3b27fcb1507b0a0cfcd31a9dab2ec98670ad5'
     ```
4. **Upload Dataset**:
   - Place `cleaned_articles.csv` in `/content/data/`.
5. **Run Pipeline**:
   - Execute all cells (Ctrl+F9).
   - Outputs: `data/translated_articles.csv`, `data/finetuned_articles.csv`, `outputs/trend_prediction.png`.
6. **Fix Git Error** (if needed):
   - Run cleaning script to remove `metadata.widgets`:
     ```python
     import json
     def clean_notebook_metadata(notebook_path="NewsBot_2_0_Final_Project_FaizaAbdullah.ipynb", output_path="Working_cleaned.ipynb"):
         with open(notebook_path, 'r') as f:
             nb = json.load(f)
         if 'widgets' in nb.get('metadata', {}):
             del nb['metadata']['widgets']
         with open(output_path, 'w') as f:
             json.dump(nb, f, indent=2)
     clean_notebook_metadata()
     ```
7. **Access Outputs**:
   - Download results from `/content/data/` and `/content/outputs/`.

## Deployment on AWS EC2
1. **Launch EC2 Instance**:
   - Choose Ubuntu 20.04, t3.medium (4GB RAM, 2 vCPUs).
   - Allocate 30GB EBS storage.
   - Configure security group: Allow HTTP (port 80), SSH (port 22).
2. **Connect to Instance**:
   ```bash
   ssh -i <your-key.pem> ubuntu@<ec2-public-ip>
   ```
3. **Install Dependencies**:
   ```bash
   sudo apt update
   sudo apt install python3-pip python3-venv
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
4. **Install NLTK Data**:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('punkt_tab')
   nltk.download('stopwords')
   ```
5. **Upload Repository**:
   - Clone or upload `ITAI2373-NewsBot-Final`:
     ```bash
     git clone https://github.com/<your-username>/ITAI2373-NewsBot-Final.git
     cd ITAI2373-NewsBot-Final
     ```
6. **Configure Wandb**:
   - Add API key to `config/api_keys_template.txt` or:
     ```bash
     export WANDB_API_KEY='caf3b27fcb1507b0a0cfcd31a9dab2ec98670ad5'
     ```
7. **Upload Dataset**:
   - Copy `cleaned_articles.csv` to `data/` using SCP:
     ```bash
     scp -i <your-key.pem> cleaned_articles.csv ubuntu@<ec2-public-ip>:~/ITAI2373-NewsBot-Final/data/
     ```
8. **Run Notebook as Script**:
   - Convert notebook to Python script:
     ```bash
     jupyter nbconvert --to script notebooks/NewsBot_2_0_Final_Project_FaizaAbdullah.ipynb
     ```
   - Run:
     ```bash
     python NewsBot_2_0_Final_Project_FaizaAbdullah.py
     ```
9. **Access Outputs**:
   - Results in `data/` and `outputs/`.
   - Copy to local machine:
     ```bash
     scp -i <your-key.pem> -r ubuntu@<ec2-public-ip>:~/ITAI2373-NewsBot-Final/data/ .
     ```
10. **Optional: Serve as API**:
    - Install Flask:
      ```bash
      pip install flask
      ```
    - Create `app.py` to serve queries (example):
      ```python
      from flask import Flask, request, jsonify
      from src.conversation.query_processor import ConversationalAgent
      import pandas as pd

      app = Flask(__name__)
      agent = ConversationalAgent()
      df = pd.read_csv('data/cleaned_articles.csv')

      @app.route('/query', methods=['POST'])
      def query():
          data = request.json
          query = data.get('query', '')
          results = agent.process_query(query, df)
          return jsonify(results.to_dict())
      
      if __name__ == '__main__':
          app.run(host='0.0.0.0', port=80)
      ```
    - Run: `python app.py`.
    - Access: `http://<ec2-public-ip>/query` with JSON payload (e.g., `{"query": "climate change news"}`).

## Monitoring and Maintenance
- **Logs**: Check `outputs/logs.txt` for errors (e.g., `Sample insights`, `Trend prediction error`).
- **Wandb Dashboard**: Monitor fine-tuning metrics at https://wandb.ai/.
- **Updates**: Pull latest repository changes (`git pull`) and update dependencies (`pip install -r requirements.txt`).

## Troubleshooting
- **Enhancement Error**: If Cell 5 reports 0%, verify `insight_category` in `enhanced_articles.csv`.
- **Fine-tuning Error**: Ensure `transformers>=4.28.0` for `eval_strategy`.
- **Git Error**: Re-run cleaning script if `metadata.widgets` persists.
- **Contact**: Faiza Abdullah at [faiza.abdullah79"icloud.com].
