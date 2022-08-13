import pytest
import os

from app import app, UNSPLASH_URL

@pytest.fixture
def client():
    return app.test_client()

def test_get_random_dolphin_image(client, requests_mock):
    test_data_path = os.path.join(os.path.dirname(__file__), 'data/sample_unsplash_response.json')
    mock_unsplash_response = open(test_data_path).read()

    target_image_url = "https://unsplash.com/photos/rTJPbmm-160/download?ixid=MnwzNTQ2MTN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2NjAyNjg3Nzc"

    requests_mock.get(UNSPLASH_URL, text=mock_unsplash_response)
    requests_mock.get(target_image_url, text="dummy text")

    resp = client.get('/picture')

    assert resp.status_code == 200
    assert resp.text == "dummy text"
    assert resp.mimetype == 'image/jpeg'
