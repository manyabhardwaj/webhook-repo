from flask import Flask, request, render_template
from datetime import datetime
from db.connection import collection
from utils.formatter import format_event

app = Flask(__name__)

@app.route('/')
def index():
    events = list(collection.find().sort("timestamp", -1).limit(10))
    return render_template("index.html", events=events, format_event=format_event)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    event_type = request.headers.get('X-GitHub-Event')
    ts = datetime.utcnow()

    try:
        if event_type == "push":
            doc = {
                "author": data["pusher"]["name"],
                "to_branch": data["ref"].split("/")[-1],
                "timestamp": ts,
                "type": "push"
            }
        elif event_type == "pull_request":
            pr = data["pull_request"]
            doc = {
                "author": pr["user"]["login"],
                "from_branch": pr["head"]["ref"],
                "to_branch": pr["base"]["ref"],
                "timestamp": ts,
                "type": "merge" if pr.get("merged") else "pull_request"
            }
        else:
            return "", 204  # Ignore other events

        collection.insert_one(doc)
        return "", 200

    except Exception as e:
        print(f"Error handling webhook: {e}")
        return "Internal Server Error", 500

if __name__ == "__main__":
    app.run(debug=True)
