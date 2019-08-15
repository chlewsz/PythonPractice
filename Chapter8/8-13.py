def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, val in user_info.items():
        profile[key] = val
    return profile

user_profile = build_profile('zhang', 'san', sex='man', age=30)
print(user_profile)