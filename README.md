# Webhook Receiver - GitHub Event Tracker

This project is built to receive GitHub webhook events (Push, Pull Request, Merge), store them in MongoDB, and display them on a minimal UI every 15 seconds.

## 🧩 Tech Stack

- Flask
- MongoDB Atlas
- Render (Deployment)
- GitHub Webhooks

## 📡 Live Site

👉 [View Live Webhook UI](https://webhook-repo-ocsr.onrender.com/)

## 📦 Repositories

1. GitHub Action Repo (to trigger webhooks):  
   🔗 https://github.com/manyabhardwaj/action-repo

2. Webhook Receiver Repo (Flask backend + Mongo):  
   🔗 https://github.com/manyabhardwaj/webhook-repo

## 🛠 How It Works

- GitHub webhooks trigger on Push, PR, Merge
- Webhook hits `/webhook` route in Flask app
- Data saved to MongoDB
- Frontend fetches and displays it every 15 seconds

## ✅ Example Output

> Travis pushed to main on 1st April 2021 - 9:30 PM UTC  
> Travis submitted a pull request from staging to master on 1st April 2021 - 9:00 AM UTC

---

## 👩‍💻 Developed By

Manya Bhardwaj
