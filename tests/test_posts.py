
def test_get_all(authorized_user, test_posts):
    res = authorized_user.get("/post/")
    assert res.status_code == 200
    
def test_create_post(authorized_user):
    res = authorized_user.post("/post/", json={"title":"test", "content":"test"})
    assert res.status_code == 201
    
def test_create_post_publish(authorized_user):
    res = authorized_user.post("/post/", json={"title":"test", "content":"test", "is_published":False})
    assert res.status_code == 201
    
def test_get_one_post(authorized_user, test_posts):
    res = authorized_user.get("/post/1")
    assert res.status_code == 200
    
def test_delete_post(authorized_user, test_posts):
    res = authorized_user.delete("/post/1")
    assert res.status_code == 200
    
def test_update_post(authorized_user, test_posts):
    res = authorized_user.put("/post/1", json={"title":"update_test", "content":"update_test"})
    assert res.status_code == 200