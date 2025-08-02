# TODO: place your cursor at the end of line 6 and press Enter to generate a suggestion.
# Tip: press tab to accept the suggestion.

fake_users = [
    { "name": "User 1", "id": "user1", "city": "San Francisco", "state": "CA" },
]
def get_user_by_id(user_id):
    for user in fake_users:
        if user["id"] == user_id:
            return user
    return None
def test_get_user_by_id():
    assert get_user_by_id("user1") == { "name": "User 1", "id": "user1", "city": "San Francisco", "state": "CA" }
    assert get_user_by_id("user2") == None
    assert get_user_by_id("user3") == None
    assert get_user_by_id("user4") == None
    assert get_user_by_id("user5") == None
    assert get_user_by_id("user6") == None
    return
# File path: /c%3A/Users/Rodrigo/AppData/Roaming/Code/User/globalStorage/amazonwebservices.amazon-q-vscode/Generate_unit_tests.py
# Content:
    assert get_user_by_id("user1") == { "name": "User 1", "id": "user1", "city": "San Francisco", "state": "CA" }
    assert get_user_by_id("user2") == None
    assert get_user_by_id("user3") == None
    assert get_user_by_id("user4") == None
    assert get_user_by_id("user5") == None  
    




    