# It is simmilar to lists excepts that it accepts item as key-value pair
# user = ['Mahesh','35','DevOps Engineer','US']

user = {"username": "Mahesh", "age": "35", "job": "DevOps Engineer", "country": "US"}
print("The Username is", user["username"], ", he is", user["age"], "years old", "he works as", user["job"], "and lives in", user["country"])

###############Loop Through Dictionary##########################

langs = {
    "en": "English",
    "es": "Spanish",
    "ar": "Arabic",
    "it": "Italian"
}

for key, value in langs.items():
    print(key, ":", value)


