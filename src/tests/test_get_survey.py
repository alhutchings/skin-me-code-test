from app import create_app

def test_get_survey():
    with create_app().test_client() as client:
        res = client.get('/survey?page=1')
        assert res.status_code == 200