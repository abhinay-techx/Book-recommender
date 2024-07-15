from flask import Flask, render_template, request
import pickle
import numpy as np

# Load pickled data
popular_data = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(popular_data['Book-Title'].values),
                           author=list(popular_data['Book-Author'].values),
                           image=list(popular_data['Image-URL-M'].values),
                           votes=list(popular_data['num_rating'].values),
                           rating=list(popular_data['avg_rating'].values))

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=['POST'])
def recommend_books():
    user_input = request.form.get('user_input')
    
    if user_input is None or user_input.strip() == '':
        error_message = "Please enter a valid book name."
        return render_template('recommend.html', error_message=error_message)
    
    if user_input not in pt.index:
        error_message = f"No recommendations found for the book '{user_input}'. Please check the spelling or try another book."
        return render_template('recommend.html', error_message=error_message)

    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)

    print(data)

    return render_template('recommend.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
