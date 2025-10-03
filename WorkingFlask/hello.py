from flask import Flask
import random

countries = ["Morocco","USA","UK","Kanada"]
random_number = random.randint(0,3)

app = Flask(__name__)

@app.route('/')
def Geuss():
    return '<h1><center>Guess the country,try Morocco, USA, UK or Kanada.</center></h1> <center><img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMTM4eGdyazN3OTRvaHJqcHdocmwwem93ejZuYzU5NmVhOTAyNXV2aSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/llJ72v9vCcVgbUXSss/giphy.webp" width=200></center>'

@app.route("/<country>")
def Info(country):
    if country == countries[random_number] :
        return f"<center>u re right buddy the right answer is : <strong>{country}</strong></center>"
    else:
        return f"<center>Give it another try u re wrong</center>"



if __name__ == "__main__":
    app.run(debug=True) #this is just a simple project to see how flask module works 