from datetime import datetime

def format_event(event):
    ts = event["timestamp"].strftime('%d %b %Y - %I:%M %p UTC')
    
    if event["type"] == "push":
        return f'{event["author"]} pushed to {event["to_branch"]} on {ts}'
    
    elif event["type"] == "pull_request":
        return f'{event["author"]} submitted a pull request from {event["from_branch"]} to {event["to_branch"]} on {ts}'
    
    elif event["type"] == "merge":
        return f'{event["author"]} merged branch {event["from_branch"]} to {event["to_branch"]} on {ts}'
    
    return "Unknown event"
