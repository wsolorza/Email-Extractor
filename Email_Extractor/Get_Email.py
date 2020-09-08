import re


class Get_Email(object):
    # Constructor
    def __init__(self):

        # Mails [Private]
        self.__Emails = []

    # Search Email
    def Search_Email(self, _Beautiful_Soup):
        # Regex Email
        EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|
                          \\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|
                          \[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|
                          [a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

        try:
            for _Email in _Beautiful_Soup.find_all('a'):

                # Check Regex
                if(bool(re.match(EMAIL_REGEX, _Email.text))):

                    if(_Email.text not in self.__Emails):
                        print(_Email.text)

                    # Add Email to List
                    self.__Emails.append(_Email.text)
        except Exception:
            pass
