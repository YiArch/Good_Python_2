from string import digits, ascii_lowercase
from random import choice, randint

alph = ascii_lowercase + digits + '_.'


class EmailValidator:

    def __new__(cls, *args, **kwargs):
        return None

    @staticmethod
    def __is_email_str(email):
        return type(email) is str

    @classmethod
    def check_email(cls, email):
        if cls.__is_email_str(email):
            lst = list(email.split('@'))
            if len(lst) == 2 and 1 < len(lst[0]) < 101 and 1 < len(lst[1]) < 51:
                left = all([map(lambda ch: ch in alph, lst[0]), '..' not in lst[0]])
                right = all([map(lambda ch: ch in alph, lst[1]), '..' not in lst[1], '.' in lst[1]])
                return all([left, right])
        return False

    @classmethod
    def get_random_email(cls):
        while True:
            em_len = randint(1,100)
            new_mail = ''.join([choice(alph) for _ in range(em_len)])
            if all([map(lambda ch: ch in alph, new_mail), '..' not in new_mail]):
                return new_mail + '@gmail.com'