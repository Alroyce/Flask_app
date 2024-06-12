from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define routes and views
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle registration logic here
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    # Logic to fetch user's bookings and display on dashboard
    return render_template('dashboard.html')

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        # Handle cargo booking logic here
        return redirect(url_for('dashboard'))
    return render_template('booking.html')

if __name__ == '__main__':
    app.run(debug=True)
