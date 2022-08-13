from flask import Flask
from ratelimit import limits, RateLimitException
import requests

CLIENT_ID = "NGfWIEZIqoa5Or3hMSlZyRQ6c2urFuNbYznjw_a6RxE"
UNSPLASH_URL = "https://api.unsplash.com/photos/random?query=dolphin&client_id=" + CLIENT_ID

app = Flask(__name__)

@app.errorhandler(RateLimitException)
def handle_rate_limit(e):
    return 'You have exceeded the rate limit of one call per second for this endpoint. Please wait and try again.', 429

@app.route('/picture', methods=['GET'])
@limits(calls=1, period=1)
def get_random_dolphin_image():
  def dolphin_image_stream():
    request = requests.get(UNSPLASH_URL)
    request_data = request.json()
    image_url = request_data["links"]["download"]

    return requests.get(image_url, stream=True)

  return app.response_class(dolphin_image_stream(), mimetype='image/jpeg')


