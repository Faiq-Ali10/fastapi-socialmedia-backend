
def test_up_vote(authorized_user, test_posts):
    res = authorized_user.post("/vote/", json={"post_id":1, "direction":1})
    assert res.status_code == 201
    
def test_down_vote(authorized_user, test_posts):
    res = authorized_user.post("/vote/", json={"post_id":2, "direction":-1})
    assert res.status_code == 201
    
def test_up_vote_twice(authorized_user, create_up_vote):
    res = authorized_user.post("/vote/", json={"post_id":1, "direction":1})
    assert res.status_code == 409
    
def test_down_vote_twice(authorized_user, create_down_vote):
    res = authorized_user.post("/vote/", json={"post_id":1, "direction":-1})
    assert res.status_code == 409
    
def test_up_to_down_vote(authorized_user, create_up_vote):
    res = authorized_user.post("/vote/", json={"post_id":1, "direction":-1})
    assert res.status_code == 201
    
def test_down_to_up_vote(authorized_user, create_down_vote):
    res = authorized_user.post("/vote/", json={"post_id":1, "direction":1})
    assert res.status_code == 201
    
def test_remove_up_vote(authorized_user, create_up_vote):
    res = authorized_user.post("/vote/", json={"post_id":1, "direction":0})
    assert res.status_code == 201
    
def test_remove_down_vote(authorized_user, create_down_vote):
    res = authorized_user.post("/vote/", json={"post_id":1, "direction":0})
    assert res.status_code == 201
    
def test_remove_not_vote(authorized_user, test_posts):
    res = authorized_user.post("/vote/", json={"post_id":1, "direction":0})
    assert res.status_code == 409
    