from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/play')          # The "@" decorator associates this route with the function immediately following
def play():
    return render_template('index.html', phrase='hello', times=3, color1='#9FC5F5')  


@app.route('/play/<num>')          # The "@" decorator associates this route with the function immediately following
def playNum(num):
    num = int(num)
        #For Loop goes here to print out the number of names it's given in the url
    # print(name)
    return render_template('index.html', times=num, color1='#9FC5F5') 

@app.route('/play/<num>/<color>')          # The "@" decorator associates this route with the function immediately following
def playNumColor(num, color):
    num = int(num)

        #For Loop goes here to print out the number of names it's given in the url
    # print(name)
    return render_template('index.html', times=num, color1=color)  



    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
