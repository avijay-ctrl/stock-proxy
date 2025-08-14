from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# ScrapingDog API key
SCRAPINGDOG_API_KEY = "689b7f086b9260801e5c40b1"

@app.route("/stock", methods=["GET"])
def get_stock_data():
    query = request.args.get("query")
    if not query:
        return jsonify({"error": "Missing 'query' parameter"}), 400

    url = "https://api.scrapingdog.com/google_finance"
    params = {
        "api_key": SCRAPINGDOG_API_KEY,
        "query": query
    }

    try:
        resp = requests.get(url, params=params)
        resp.raise_for_status()
        return jsonify(resp.json())
    except requests.RequestException as e:
        return jsonify({"error": f"API request failed: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

if __name__ == "__main__":
    # Render provides the port via the PORT env variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
