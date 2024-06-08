import pymongo as m
from urllib.parse import quote_plus
from datetime import datetime

def main():
    myclient = m.MongoClient("mongodb+srv://gillam:MTHeUahmIeRcu2F8@alexcluster.t5fqhgn.mongodb.net/?retryWrites=true&w=majority&appName=alexcluster")
    mydb = myclient["alex_recipes"]
    mycol = mydb["favorite recipes"]

    myquery = { "food_type": "Pizza", "description": "Brick oven-style pizza", "url": "https://www.kingarthurbaking.com/recipes/brick-oven-style-pizza-recipe", \
                "date_added": datetime.now() }

    mydoc = mycol.insert_one(myquery)
    print(mydoc)

if __name__ == "__main__":
    main()