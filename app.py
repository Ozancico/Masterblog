from flask import Flask, render_template, request, url_for, redirect
import json


app = Flask(__name__)
FILENAME = 'data.json'

def load_blog_data():
    """
    Reads blog data from a JSON file.
    :return: A list of blog entries, each represented as a dictionary.
    """
    try:
        with open(FILENAME, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []  # Return an empty list if the file does not exist
    except json.JSONDecodeError:
        print("Error decoding JSON from the file. Returning an empty list.")


def save_blog_data(data):
    """Writes blog data to a JSON file.
    """
    with open(FILENAME, 'w') as file:
        json.dump(data, file, indent=4)


@app.route('/')
def index():
    """
    Renders the index page with a list of blog entries.
    """
    blog_data = load_blog_data()
    return render_template('index.html', blog_entries=blog_data)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    Handles the addition of new blog entries.
    If the request method is POST, it saves the new entry and redirects to index.
    If GET, display the form to add a new entry.
    """
    if request.method == 'POST':
        posts = load_blog_data()
        new_post = {
            "id": max([post["id"] for post in posts], default=0) + 1,
            'title': request.form.get('title'),
            'author': request.form.get('author'),
            'content': request.form.get('content'),
            'likes': 0
        }
        posts.append(new_post)
        save_blog_data(posts)
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/delete/<int:post_id>')
def delete(post_id):
    """
    Deletes a blog post with the given ID.
    """
    posts = load_blog_data()
    posts = [post for post in posts if post['id'] != post_id]
    save_blog_data(posts)
    return redirect(url_for('index'))


def fetch_post_by_id(post_id):
    """
    Fetches a blog post by its ID.
    Returns None if not found.
    """
    posts = load_blog_data()
    for post in posts:
        if post['id'] == post_id:
            return post
    return None

@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """
    Handles the update of existing blog entries.
    GET: Displays the update form with current post data
    POST: Updates the post and redirects to index
    """
    post = fetch_post_by_id(post_id)
    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        posts = load_blog_data()
        for p in posts:
            if p['id'] == post_id:
                p['title'] = request.form.get('title')
                p['author'] = request.form.get('author')
                p['content'] = request.form.get('content')
                break
        save_blog_data(posts)
        return redirect(url_for('index'))

    return render_template('update.html', post=post)

@app.route('/like/<int:post_id>')
def like_post(post_id):
    """
    Increment the like count for a post.
    """
    posts = load_blog_data()
    for post in posts:
        if post['id'] == post_id:
            post['likes'] = post.get('likes', 0) + 1
            break
    save_blog_data(posts)
    return redirect(url_for('index'))




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5008, debug=True)
