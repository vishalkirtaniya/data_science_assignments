import json

# use cleaned_data from assignment 1
data = json.load(open('massive_data.json'))

# Part A — Developers You May Know
def people_you_may_know(user_id, data):
    user_data = {}
    for user in data['users']:
        user_data[user['id']] = user['friends']

    if user_id not in user_data:
        print("User not found")
        return []

    direct_friends = user_data[user_id]

    if direct_friends == []:
        print('No Suggestions - user has no connections yet')

    mutual_suggestions = {}
    for user in direct_friends:
        for mutual in user_data[user]:
            if mutual != user_id and mutual not in direct_friends:
                mutual_suggestions[mutual] = mutual_suggestions.get(mutual, 0) + 1

    sorted_suggestions = sorted(mutual_suggestions.items(), key=lambda x: x[1], reverse=True)

    return [user for user, _ in sorted_suggestions]

print(f"friends: {people_you_may_know(2, data)}")
print("-----------------------------------------------")

# Part B — Communities You Might Like
def pages_you_might_like(user_id, data):
    liked_pages = {}
    for user in data['users']:
        liked_pages[user['id']] = user['liked_pages']

    if user_id not in liked_pages:
        return []
    
    direct_liked_pages = liked_pages[user_id]

    pages_suggestion = {}
    all_pages = set()
    for pages in liked_pages.values():
        all_pages.update(pages)  # collect every page ID across all users

    if set(direct_liked_pages) >= all_pages:  # is my set a superset of all pages?
        print("You're already following everything!")
        return []

    for direct_page in direct_liked_pages:
        for _, liked_list in liked_pages.items():
            for mutual_page in liked_list:
                if mutual_page != direct_page:
                    pages_suggestion[mutual_page] = pages_suggestion.get(mutual_page, 0) + 1

    sorted_suggestions = sorted(pages_suggestion.items(), key=lambda x: x[1], reverse=True)

    return [page_id for page_id, _ in sorted_suggestions]

print(f"pages: {pages_you_might_like(1, data)}")
print("-----------------------------------------------")

# Part B.5 — People with common likes

def users_with_same_likes(user_id, data):
    liked_data = {}
    for user in data['users']:
        liked_data[user['id']] = user['liked_pages']
        
    if user_id not in liked_data:
        return []
    
    direct_liked_pages = liked_data[user_id]

    like_users = {}
    for direct_like in direct_liked_pages:
        for user, liked_pages in liked_data.items():
            if direct_like in liked_pages and user != user_id:
                like_users[user] = like_users.get(user, 0) + 1

    sorted_users = sorted(like_users.items(), key=lambda x: x[1], reverse=True)

    return [user for user, _ in sorted_users]

print(f"users: {users_with_same_likes(1, data)}")