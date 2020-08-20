import random
import mysql.connector
from faker import Faker
import datetime
import radar

# from faker_e164.providers import E164Provide
fake_data = Faker()
# fake_data.add_provider(E164Provider)
mydb = mysql.connector.connect(
    user="root",
    password="",
    database="con_recommendation",
    host="localhost")

mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM auth_user')
myresult = mycursor.fetchall()
# print(myresult)
for _ in range(0, 500):
    mydata = """INSERT INTO auth_user (first_name, last_name, username, email, password) VALUES(%s,%s, %s, %s, %s)"""
    data = (fake_data.name(), fake_data.name(),
            fake_data.email(), fake_data.email(), fake_data.password())
    datainsert = mycursor.execute(mydata, data)
    print(datainsert)
    user_id = mycursor.lastrowid
    print(mycursor.lastrowid)
    Budgets = random.sample(list(['Luxury', 'Budget']), 1)

    cuisine = random.sample(list(['American', 'Chinese', 'European', 'French', 'Greek',
                                  'Indian', 'Japanese', 'Lebanese', 'Mediterranean', 'Thai', 'Turkish']), 3)
    event = random.sample(list(['Music Festivals & Concerts', 'High Fashion', 'Movie Premiers & Film Festivals', 'Theater & Live Shows',
                                'Business Events', 'Shopping Festivals', 'Movies, TV shows & Subscriptions', '​Art & Literature']), 2)
    hobbies = random.sample(list(['Adventure Sports', 'Fitness', 'Music & Dancing',
                                  'Photography', 'Cycling', 'Drawing & Painting', 'Golf']), 3)
    lifestyle = random.sample(list(['Fashion', 'Nightlife', 'Wellness & Spa', 'Business & Corporate', 'Bespoke Experiences',
                                    'Gastronomy', 'Car Rental', 'Lifestyle Services', 'Luxury Purchase', 'Charters', 'Airport Services']), 2)
    sport = random.sample(list(['Cricket', 'Football', 'Tennis',
                                'Grand Prix', 'Moto-GP', 'Multi-sport', 'Rugby', 'Derby']), 3)
    travel = random.sample(list(['Nature & Outdoors', 'Weekend Getaways', 'Safari', 'Historical & Heritage',
                                 'Countryside', 'Family', 'Desert Safari', 'Beaches', 'Cityscape', 'Romantic Getaways']), 3)
    location = random.sample(list(
        ['Jaipur', 'Lucknow', 'Agra', 'Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Surat', 'Pune']), 1)

    c = ','.join(cuisine)
    e = ','.join(event)
    h = ','.join(hobbies)
    l = ','.join(lifestyle)
    s = ','.join(sport)
    t = ','.join(travel)
    loca = ','.join(location)
    bud = ','.join(Budgets)
    print(c)
    print(e)
    print(h)
    print(l)
    print(s)
    print(t)
    date = radar.random_datetime(
        start=datetime.datetime(year=1990, month=5, day=24),
        stop=datetime.datetime(year=2013, month=5, day=24)
    )
    profile = """INSERT INTO account_profile (mobile,DOB,Location,Budget,user_id) VALUES(%s,%s, %s, %s, %s)"""
    dataprof = (fake_data.phone_number(), date, loca, bud, user_id)
    profinsert = mycursor.execute(profile, dataprof)
    prefrence = """INSERT INTO account_preference (Cuisine,Lifestyle,Sportevent,Travel,Entertainment_events,Hobbies,user_id) VALUES(%s,%s, %s, %s, %s,%s,%s)"""
    datapref = (c, l, s, t, e, h, user_id)
    prefinsert = mycursor.execute(prefrence, datapref)


# mycursor.execute('SELECT id FROM auth_user ORDER BY id ASC')
# userid = mycursor.fetchall()
# print(userid)
mydb.commit()
mydb.close()
# fruits = set(['apple', 'orange', 'watermelon', 'grape'])
# k = random.sample(list(['aplle', 'ball', 'cat', 'dog', 'egg', 'fish']), 2)
# print(k)
# my_string = ','.join(k)
# print(my_string)
# faker = Faker('en_IN')
# name = faker.name()
# address = faker.address()
# phone = faker.phone_number()
# city = faker.city()
# state = faker.state()
# print(name)
# print(state)
# print(city)
# print('{}, INDIA'.format(faker.city()))

# # Generate random datetime (parsing dates from str values)
# # radar.random_datetime(start='2000-05-24', stop='2013-05-24T23:59:59')

# # Generate random datetime from datetime.datetime values

# print(date)
