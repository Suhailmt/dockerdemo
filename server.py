from flask import Flask, render_template, redirect
import os
import socket

# What will we show pictures of? Default is cat
picture_of = os.getenv('PICTURE_OF', 'cat')

# Create Flask app
app = Flask('app')

# URL route for site root 
@app.route('/')
def route_root():
  return render_template('index.html', picture_of=picture_of, hostname=socket.gethostname())

# URL route for random pictures
@app.route('/image')
def route_image():
  return redirect("https://loremflickr.com/640/480/" + picture_of, code=302)
  
# Start Flask HTTP server
print('\n### Demo app started, will display pictures of: ' + picture_of + '\n')
app.run(host='0.0.0.0', port=8000)
