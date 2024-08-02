from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

# Database connection
def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='your_user',
        password='your_password',
        db='cafe_service',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Study Space Management
@app.route('/study_space', methods=['GET', 'POST'])
def study_space():
    if request.method == 'POST':
        cafe_name = request.form['cafe_name']
        study_zone = request.form['study_zone']
        amenities = request.form['amenities']
        booking_time = request.form['booking_time']
        student_id = request.form['student_id']
        
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = "INSERT INTO study_spaces (cafe_name, study_zone, amenities, booking_time, student_id) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (cafe_name, study_zone, amenities, booking_time, student_id))
        connection.commit()
        connection.close()
        
        return redirect(url_for('study_space'))
    
    return render_template('study_space.html')

# Delivery and Takeaway Services
@app.route('/delivery', methods=['GET', 'POST'])
def delivery():
    if request.method == 'POST':
        cafe_name = request.form['cafe_name']
        item_name = request.form['item_name']
        delivery_time = request.form['delivery_time']
        student_id = request.form['student_id']
        
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = "INSERT INTO deliveries (cafe_name, item_name, delivery_time, student_id) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (cafe_name, item_name, delivery_time, student_id))
        connection.commit()
        connection.close()
        
        return redirect(url_for('delivery'))
    
    return render_template('delivery.html')

# Loyalty Program
@app.route('/loyalty', methods=['GET', 'POST'])
def loyalty():
    if request.method == 'POST':
        student_id = request.form['student_id']
        points = request.form['points']
        rewards = request.form['rewards']
        
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = "INSERT INTO loyalty_program (student_id, points, rewards) VALUES (%s, %s, %s)"
            cursor.execute(sql, (student_id, points, rewards))
        connection.commit()
        connection.close()
        
        return redirect(url_for('loyalty'))
    
    return render_template('loyalty.html')

if __name__ == '__main__':
    app.run(debug=True)
