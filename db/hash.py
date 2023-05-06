'''                             Why we use Hash??
Passwords are one of the most sensitive data that we deal with in the database.
Therefore, we cannot store this type of data like the rest of the data we get from users.
Using the PASSLIB library, we hash the password we get from the user and store it in the database.
'''

from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes='bcrypt', deprecated='auto')


class Hash:

    @staticmethod
    def bcrypt(password):
        return pwd_cxt.hash(password)

    @staticmethod
    def verify(hashed_password, plain_password):
        pwd_cxt.verify(plain_password, hashed_password)