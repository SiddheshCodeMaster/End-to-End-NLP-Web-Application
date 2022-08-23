from flask import Flask, render_template, url_for
from flask import request as req
import requests as rs
app = Flask(__name__)
@app.route("/",methods=['GET','POST'])
def Index():
    return render_template("index.html")

@app.route("/Summarize",methods=["GET","POST"])
def Summarize():
    if req.method == "POST":
        API_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"
        headers = {"Authorization": "Bearer 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"}

        data = req.form["data"]


        min_length = 20 #int(input("Enter the Minimum Length for the summary: "))
        max_length = int(req.form["max_length"])
        def query(payload):
            response = rs.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({
	        "inputs": data,
	        "parameters":{"min_length":min_length,"max_length":max_length},
        })[0]

        return render_template("index.html", result=output['summary_text'])
    else:
        return render_template("index.html")
    


if __name__=="__main__":
    app.debug = True # While testing I am keeping debug = True.
    app.run()

