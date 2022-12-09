from app import create_app

def test_get_home():
    with create_app().test_client() as client:
        res = client.get('/')
        assert res.status_code == 200
