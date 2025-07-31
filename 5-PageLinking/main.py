from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, abort
import os
from datetime import datetime
import json
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Simple user database (in production, use a real database)
users = {
    "admin": {"password": "admin123", "name": "Admin User", "role": "admin"},
    "user1": {"password": "password1", "name": "John Doe", "role": "user"},
    "user2": {"password": "password2", "name": "Jane Smith", "role": "user"}
}

# Sample blog posts
blog_posts = [
    {"id": 1, "title": "Getting Started with Flask", "author": "Admin", "date": "2023-05-15", 
     "content": "Flask is a lightweight WSGI web application framework...", "image": "flask.jpg"},
    {"id": 2, "title": "Mastering CSS Animations", "author": "Jane Smith", "date": "2023-06-02", 
     "content": "CSS animations bring your website to life with smooth transitions...", "image": "css.jpg"},
    {"id": 3, "title": "Building Responsive Websites", "author": "John Doe", "date": "2023-06-20", 
     "content": "Responsive design ensures your website looks great on all devices...", "image": "responsive.jpg"}
]

# Sample products
products = [
    {"id": 1, "name": "Web Design Package", "price": 499, "description": "Complete website design solution", "category": "Design"},
    {"id": 2, "name": "SEO Optimization", "price": 299, "description": "Improve your search engine rankings", "category": "Marketing"},
    {"id": 3, "name": "Custom Web Application", "price": 1499, "description": "Tailor-made web application for your business", "category": "Development"}
]

# Route for home page
@app.route('/')
def home():
    return render_template('home.html', posts=blog_posts[:3], user=session.get('user'))

# Route for about page
@app.route('/about')
def about():
    team_members = [
        {"name": "Alex Johnson", "position": "CEO & Founder", "bio": "10+ years of web development experience"},
        {"name": "Sarah Williams", "position": "Lead Designer", "bio": "Specializes in UI/UX and brand identity"},
        {"name": "Michael Chen", "position": "Senior Developer", "bio": "Full-stack developer with DevOps expertise"}
    ]
    return render_template('about.html', team=team_members)

# Route for contact page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # In a real app, you would save this to a database
        flash(f'Thank you {name}! Your message has been sent successfully.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contactus.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username in users and users[username]['password'] == password:
            session['user'] = {
                'username': username,
                'name': users[username]['name'],
                'role': users[username]['role']
            }
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out successfully', 'info')
    return redirect(url_for('home'))

# Profile route
@app.route('/profile')
def profile():
    if 'user' not in session:
        flash('Please login to view your profile', 'warning')
        return redirect(url_for('login'))
    
    user_data = users.get(session['user']['username'], {})
    return render_template('profile.html', user=session['user'], user_data=user_data)

# Blog route
@app.route('/blog')
def blog():
    return render_template('blog.html', posts=blog_posts)

# Single blog post route
@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    post = next((p for p in blog_posts if p['id'] == post_id), None)
    if not post:
        abort(404)
    return render_template('blog_post.html', post=post)

# Products route
@app.route('/products')
def products_page():
    return render_template('products.html', products=products)

# AJAX search endpoint
@app.route('/search')
def search():
    query = request.args.get('q', '').lower()
    results = []
    
    if query:
        # Search in blog posts
        for post in blog_posts:
            if query in post['title'].lower() or query in post['content'].lower():
                results.append({
                    'type': 'Blog Post',
                    'title': post['title'],
                    'url': url_for('blog_post', post_id=post['id'])
                })
        
        # Search in products
        for product in products:
            if query in product['name'].lower() or query in product['description'].lower():
                results.append({
                    'type': 'Product',
                    'title': product['name'],
                    'url': url_for('products_page')
                })
    
    return jsonify(results)

# 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)