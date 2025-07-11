from flask import Flask, request, render_template
from datetime import datetime
from db.connection import collection
from utils.formatter import format_event

app = Flask(__name__)

@app.route('/')
def index():
    events = list(collection.find().sort("timestamp", -1).limit(10))
    print("Fetched Events:", events)
    return render_template("index.html", events=events, format_event=format_event)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        return "✅ Webhook endpoint is live. Use POST for GitHub events.", 200

    # POST method (from GitHub)
    print("✅ /webhook POST hit!")
    data = request.json
    event_type = request.headers.get('X-GitHub-Event')
    print("👉 Event Type:", event_type)
    print("📦 Payload:", data)

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
            print("❌ Ignored Event:", event_type)
            return "", 204

        collection.insert_one(doc)
        print("✅ Event saved to MongoDB")
        return "", 200

    except Exception as e:
        print(f"❌ Error handling webhook: {e}")
        return "Internal Server Error", 500

if __name__ == "__main__":
    app.run(debug=True)
