from app import create_app

def test_save_answer():
    with create_app().test_client() as client:
        client.set_cookie('localhost', 'user_token', '12345678')
        res = client.post('answers', json={
            'answers': [{
                'answer': 'answer one',
                'question_id': '1'
            }],
            'page': 1
        })

        assert res.status_code == 201