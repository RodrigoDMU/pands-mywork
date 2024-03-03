# Quiz Questions
# What are the variable types of the following variables in the code above
# a. numberOfQuestions
# b. averageAge
# c. debugMode
# d. name
# e. ages
# f. months
# g. months[1]
# h. book
# i. stuff
# j. stuff[2]
# k. someone
# l. someone["firstname"]
# m. me
# n. me["teaching"]
# o. me["teaching"][0]["semester"]
# ---- p is a trick question look at it carefully
# p. me["teaching"][0]["coursename"]

# Author: Rodrigo De Martino Ucedo

numberOfQuestions = 5
averageAge = 23.4
debugMode = True
name = "joe"
ages = []
months = ('Jan', 'Feb', 'Mar')
book = {}
stuff = [12, 'Fred', False, {}]
someone = dict(firstname="joe")
me = {
    "firstName": "Rodrigo",
    "teaching": [{
        "courseName": "programming",
        "semester": 1
    }, {
        "courseName": "Data Representation",
        "semester": 2
    }
    ]
}

# Answers Question
# a. int
# b. float
# c. boolean
# d. str
# e. list
# f. tuple
# g. str
# h. dict
# i. list
# j. boolean (False)
# k. dict
# l. str
# m. dict
# n. list (is is nested in the dict)
# o. int
# p. undefined (the code has a capital N in courseName)