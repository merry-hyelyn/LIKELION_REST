import json

diary = {
    'id' : 3,
    'title' : 'hungry',
    'body' : 'chiken, pizza, meat',
}

print(diary)
print(type(diary))

diary_s = json.dumps(diary)

print(diary_s)
print(type(diary_s))

diary_back = json.loads(diary_s)
print(diary_back)
print(type(diary_back))