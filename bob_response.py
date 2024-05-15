import re
def response(hey_bob):
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