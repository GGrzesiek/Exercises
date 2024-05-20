import re
def response(hey_bob):
    """This function takes a string as input and returns a response based on the input string.
    
    Bob only ever answers one of five things:

    "Sure." This is his response if you ask him a question, such as "How are you?" The convention used for questions is that it ends with a question mark.
    "Whoa, chill out!" This is his answer if you YELL AT HIM. The convention used for yelling is ALL CAPITAL LETTERS.
    "Calm down, I know what I'm doing!" This is what he says if you yell a question at him.
    "Fine. Be that way!" This is how he responds to silence. The convention used for silence is nothing, or various combinations of whitespace characters.
    "Whatever." This is what he answers to anything else.
    """
    response = ["Sure.",
                "Calm down, I know what I'm doing!",
                "Whoa, chill out!",
                "Fine. Be that way!",
                "Whatever."]
    if((hey_bob.isspace())|(len(hey_bob) == 0 )):
         return response[3]
    elif(re.search(r"\?\s*$", hey_bob)):
        if(hey_bob.isupper()):
            return response[1]
        else:
            return response[0]
    elif(hey_bob.isupper()):
        return response[2]
    else:
        return response[4]