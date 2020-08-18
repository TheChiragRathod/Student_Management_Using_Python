import re
EmailPattern=re.compile(r'[a-zA-z]+[.0-9+-]+[a-zA-z0-9]*@[a-zA-z]+[0-9-]*\.[a-zA-z]+[0-9-.]*')
EnrollPattern=re.compile(r'\d{2}[a-zA-z]{5}\d{5}')


def DataValidationEnroll(Enroll):
    match=EnrollPattern.findall(Enroll)
    if(len(match)==0):
        return False
    else:
        return True

def DataValidationEmail(Email):
    match=EmailPattern.findall(Email)
    if(len(match)==0):
        return False
    else:
        return True