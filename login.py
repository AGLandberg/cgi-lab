#!/usr/bin/env python3
import cgi
import os
import secret
from templates import login_page
from templates import secret_page

def parse_cookies(cookie_string):
    result = {}
    if not cookie_string:
        return result
    cookies = cookie_string.split(";")
    for cookie in cookies:
        split_cookie = cookie.split("=")
        result[split_cookie[0]] = split_cookie[1]

    return result

cookies = parse_cookies(os.environ["HTTP_COOKIE"])

form = cgi.FieldStorage()

username = form.getfirst("username")
password = form.getfirst("password")

header = "Content-Type: text/html\r\n"

body = ""
correct_login = False

if (username == secret.username and password == secret.password):
    correct_login = True
    header += "Set-Cookie: correct_login=true\r\n"

if correct_login or ('logged' in cookies and cookies['logged'] == "true"):
    body += secret_page(username, password)
    header += "Set-Cookie: logged=true\r\n"
else:
    body += login_page()

print(header)
print()
print(body)