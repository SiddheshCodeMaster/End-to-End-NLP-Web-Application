from flask import Flask, render_template, url_for
from flask import request as req

app = Flask(__name__)
@app.route("/", methods=['GET','POST'])

def Index():
    return render_template('index.html')

@app.route("/Summarize", methods=['GET','POST'])
def Summarize():
    if req.methods == "POST":
        API_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"
        headers = {"Authorization": f"Bearer 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"}

        data = req.form["data"]

        min_length = 20 #int(input("Enter the Minimum Length for the summary: "))
        max_length = 70 #int(input("Enter the Maximum Length for the summary: "))
        def query(payload):
            response = req.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({
	        "inputs": data,
	        "parameters":{"min_length":min_length,"max_length":max_length},
        })[0]
    
        return render_template('index.html',result=output['summary_text'])
    else:
        return render_template('index.html')


if __name__=="__main__":
    app.debug=True # Keep it always True when your are debugging and making hcnages with your project
    app.run()