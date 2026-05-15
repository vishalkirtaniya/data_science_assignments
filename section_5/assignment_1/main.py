import json
import copy

# Part A:
def load_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

original = load_data('devCircle.json')
for user in original['users']:
    print(user)

original_copy = copy.deepcopy(original)
print('-------------------------')
# Part B:

def cleaning(data):
    # removes users with empty names
    filtered_users = []
    for user in data['users']:
        if user['name'].strip():
            filtered_users.append(user)

    # remove duplicate entried for users friend list:
    for user in data['users']:
        user['friends'] = list(set(user['friends']))
    
    #remove inactive users (empty friends and liked_pages)
    filtered = []
    for user in filtered_users:
        if user['friends'] and user['liked_pages']:
            filtered.append(user)

    data['users'] = filtered

    index = {}
    for page in data['pages']:
        index[page['id']] = page

    data['pages'] = list(index.values())

    return data

cleaned = cleaning(original)

def save_cleaned_data(cleaned):
    with open('cleaned.json', 'w') as file:
        json.dump(cleaned, file, indent=2)

save_cleaned_data(cleaned)

for user in cleaned['users']:
    print(user)

for page in cleaned['pages']:
    print(page)

print("------------------------------------------------------------------------")

# Part C:

def cleaning_report(original, cleaned):
    users_removed = len(original['users']) - len(cleaned['users'])

    print(f"Users Removed: {users_removed}")

    duplicate_friend_entries_fixed = 0
    for user in original['users']:
        original_friends = len(user['friends'])
        cleaned_friends = len(list(set(user['friends'])))
        duplicate_friend_entries_fixed += original_friends - cleaned_friends
    
    print(f"Duplicate friend entries fixed: {duplicate_friend_entries_fixed}")

    pages_deduplicated = len(original['pages']) - len(cleaned['pages'])
    print(f"Pages deduplicated: {pages_deduplicated}")

cleaning_report(original_copy, cleaned)