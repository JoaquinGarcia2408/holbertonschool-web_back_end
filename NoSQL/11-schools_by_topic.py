#!/usr/bin/env python3
"task 11: Where can I learn Python?"


def schools_by_topic(mongo_collection, topic):
    cursor = mongo_collection.find({"topics": topic})
    school= []
    for i in school:
        school.append(i)
    return school
