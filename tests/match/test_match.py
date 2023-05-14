from flaskr.models.match_model import CompetitionInformation


def test_request_example(client):
    response = client.get("/")
    assert "<title>米吉魔方赛事网</title>" in response.text


def test_match_list(client):
    response = client.get('list')
    assert response.status_code == 200
