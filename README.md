

\# ReviewSense AI

\## Restaurant Review Sentiment Analysis Using NLP



\### 1. Project Overview

ReviewSense AI is a machine learning project that analyzes restaurant reviews and classifies their sentiment into three categories: Positive, Negative, and Neutral.



\### 2. Objectives

\- Analyze restaurant review text.

\- Apply Natural Language Processing (NLP) techniques.

\- Classify reviews using a machine learning model.

\- Display the predicted sentiment through a web interface.



\### 3. Technologies Used

\- Python

\- Streamlit

\- Pandas

\- Scikit-learn

\- TF-IDF Vectorization

\- Support Vector Machine (SVM)



\### 4. Dataset

The project uses the Yelp restaurant review dataset:

`yelp\_sentiment\_master\_dataset.csv`



The dataset contains review text and sentiment labels.



\### 5. Model

The system uses a TF-IDF vectorizer and a Linear Support Vector Machine (SVM) classifier. Balanced class weights are used during training to help address class imbalance.



\### 6. Project Files

\- `app.py` — Streamlit website.

\- `train\_model.py` — model training and evaluation.

\- `reviewsense\_svm\_3class.pkl` — trained model pipeline.

\- `yelp\_sentiment\_master\_dataset.csv` — training dataset.

\- `requirements.txt` — Python dependencies.

\- `README.md` — project documentation.



\### 7. Installation

Install the required packages using:



```bash

pip install -r requirements.txt

```



\### 8. Run the Project

To train the model:



```bash

python train\_model.py

```



To start the website:



```bash

python -m streamlit run app.py

```



Open the local URL displayed in the terminal.



\### 9. Model Evaluation

The current model achieved approximately 82% accuracy on a held-out test set. The Neutral class has lower performance than the Positive and Negative classes, so predictions may not always be correct.



\### 10. Limitations

\- Prediction quality depends on the dataset and its labels.

\- Neutral reviews can be difficult to classify.

\- The model may make incorrect predictions for unfamiliar reviews.



\### 11. Conclusion

ReviewSense AI demonstrates how NLP and machine learning can be used to analyze restaurant review sentiment through an interactive web application.



