# Book Recommendation System

This repository contains a Book Recommendation System built using Python and Flask. The system utilizes item-based collaborative filtering with similarity scores derived from user ratings to provide personalized book recommendations.

## Features

- **Personalized Recommendations**: Suggests books based on user rating similarities.
- **Item-based Collaborative Filtering**: Utilizes item-based collaborative filtering to find similar books.
- **Clustering**: Clusters books based on similarity scores to improve recommendation accuracy.
- **Flask Web Application**: A user-friendly web interface for interacting with the recommendation system.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/book-recommendation-system.git
    cd book-recommendation-system
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Prepare the data**:
    - Ensure the `books.pkl` and `ratings.csv` files are in the `data/` directory.

2. **Run the Flask application**:
    ```bash
    flask run
    ```

3. **Access the application**:
    - Open your web browser and navigate to `http://127.0.0.1:5000`.

## Project Structure

```
book-recommendation-system/
│
├── data/
│   ├── books.pkl
│   └── ratings.csv
│
├── templates/
│   ├── index.html
│   └── recommendations.html
│
├── static/
│   └── style.css
│
├── app.py
├── recommender.py
├── requirements.txt
└── README.md
```

- `data/`: Contains the dataset files.
- `templates/`: HTML templates for the web application.
- `static/`: CSS styles for the web application.
- `app.py`: Main Flask application.
- `recommender.py`: Logic for the recommendation system.
- `requirements.txt`: List of required Python packages.
- `README.md`: Project documentation.

## How it Works

1. **Data Loading**: The system loads user ratings and book information from the dataset files.
2. **Similarity Calculation**: Computes similarity scores between books using user ratings.
3. **Collaborative Filtering**: Uses item-based collaborative filtering to recommend books similar to those the user has rated highly.
4. **Clustering**: Clusters books to improve the accuracy and relevance of recommendations.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.


## Acknowledgements

- The dataset used in this project is sourced from Kaggle.
