# 🎬 Movie Recommender System (Content-Based)

### 🔗 Live Demo  
👉 [Click here to try the app](https://movie-recommender-system-content-based-app-hfrbxfbdd3cbfx2szjn.streamlit.app/)

---

## 📌 Overview
This project is a **Content-Based Movie Recommendation System** built with **Python** and **Streamlit**.  
It suggests movies similar to the one selected by the user, based on **movie metadata** like overview, cast, crew, genres, and keywords.  

Such systems are widely used by platforms like **Netflix, Prime Video, and Hotstar** to enhance user experience.

---

## ❓ Problem Statement
With thousands of movies available, users often struggle to decide *"What should I watch next?"*.  
The challenge is to design a system that automatically recommends **relevant movies** based on user’s preference.  

---

## 💡 Solution
We implemented a **Content-Based Filtering** approach:
1. **Data Collection** – TMDB 5000 Movies Dataset.  
2. **Feature Engineering** – Extracted important features (overview, genres, keywords, cast, crew).  
3. **Text Processing** – Combined features into "tags", applied stemming, and vectorized using **CountVectorizer**.  
4. **Similarity Calculation** – Used **Cosine Similarity** to measure closeness between movies.  
5. **Recommendation Function** – For any given movie, system retrieves the top 5 most similar movies.  
6. **Deployment** – Interactive **Streamlit App** with TMDB API integration for fetching posters.  

---

## 🚀 Features
- 🎥 Search any movie and get top 5 recommendations.  
- 🖼️ Movie posters displayed via TMDB API.  
- ⚡ Fast and lightweight – works on 5000+ movies dataset.  
- 🖥️ Clean and interactive UI built with Streamlit.  

---

## 📊 Workflow
flowchart LR
A[TMDB Dataset] --> B[Preprocessing & Feature Engineering]
B --> C[Tags Creation]
C --> D[Vectorization (CountVectorizer)]
D --> E[Cosine Similarity Matrix]
E --> F[Recommendation Function]
F --> G[Streamlit Web App]


---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** – Web App Framework
* **Pandas, NumPy** – Data Handling
* **Scikit-learn** – Machine Learning (Vectorization & Similarity)
* **Requests** – Fetching movie posters via TMDB API

---

## 📂 Project Structure

```
├── app.py              # Main Streamlit app
├── movie_dict.pkl      # Preprocessed movie dataset
├── similarity.pkl      # Similarity matrix
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

---

## ⚡ How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/movie-recommender.git
   cd movie-recommender
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   streamlit run app.py
   ```

---

## 🌐 Deployment

This app can be deployed on multiple platforms:

* [Streamlit Community Cloud](https://streamlit.io/cloud)
* [Hugging Face Spaces](https://huggingface.co/spaces)
* Heroku / AWS / GCP

---

## 📊 Dataset

* **Name:** TMDB 5000 Movies Dataset
* **Source:** [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
* **Size:** \~5000 movies with metadata

---

## 👨‍💻 Author

Made with ❤️ by **Arif Ansari**

---

## ✨ Future Enhancements

* Add **Collaborative Filtering** (based on user ratings).
* Hybrid approach combining **Content + Collaborative** methods.
* Improve search functionality with fuzzy matching.
* Deploy with **Docker** and CI/CD pipeline.


