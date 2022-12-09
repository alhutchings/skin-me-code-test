from app import create_app

def test_create_question():
    with create_app().test_client() as client:
        res = client.post('questions', json={
            'name': 'Will this test work?',
            'field_type': 'free_text',
            'page': '3',
            'order': 1,
            'field_options': ''
        })
        
        assert res.status_code == 200
