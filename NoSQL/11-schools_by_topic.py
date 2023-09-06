#!/usr/bin/env python3
"task 11: Where can I learn Python?"


def schools_by_topic(mongo_collection, topic):
    "function that returns the list of school having a specific topic:"
    cursor = mongo_collection.find({"topics": topic})
    school= []
    for i in school:
        school.append(i)
    return school
