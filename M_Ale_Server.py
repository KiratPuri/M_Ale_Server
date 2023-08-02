from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/img')
def img():
    return redirect("https://images.dog.ceo//breeds//labrador//n02099712_2473.jpg")

# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     if request.method == "POST":
#         try:
#             data = request.form.to_dict()
#             write_to_csv(data)
#             return redirect("./Thank_you_page.html")
#         except:
#             return "Did not save to database!"
#     else:
#         return "Somthing went wronge"
#     return "Hure! Thanks for submiting."