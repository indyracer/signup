#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

import cgi

import re


#html boilder plate for top of page

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Sign Up</title>
</head>
<body>

"""

#create form

def render_signup_form(substitions):
    return """
    <form action="/signup" method="post">
    <h1>Signup</h1>
        <table>
            <tr>
                <td>
                    <label for="username">Username: </label>
                </td>
                <td>
                    <input name="username" type="text" value="%(username)s"/>
                </td>
                <td><div style="color: red">%(error_username)s</div></td>
            </tr>
            <tr>
                <td>
                    <label for="password">Password: </label>
                </td>
                <td>
                    <input name="password" type="password" value="%(password)s" />
                <td>
                <td>
                    <div style="color: red">%(error_password)s</div>
            </tr>
            <tr>
                <td>
                    <label for="verify">Verify Password: </label>
                </td>
                <td>
                    <input name="verify" type="password" value="%(verify)s"/>
                </td>
                <td>
                    <div style="color: red">%(error_verify)s</s>
                </td>
            </tr>
            <tr>
                <td>
                    <label for="email">Email Address: </label>
                </td>
                <td>
                    <input name="email" type="text" value="%(email)s" />
                </td>
                <td>
                    <div style="color: red">%(error_email)s</span>
                </td>
            </tr>
        </table>
        <input type="submit" value="Submit">
    </form>
    """ % substitions




#html boilerplate for bottom of page
page_footer = """
</body>
</html>
"""
class Index(webapp2.RequestHandler):
    #print header and form
    def get(self):
        main_content = page_header + render_signup_form({"username": "", "password": "", "verify": "", "email": "", "error_username":"", "error_password": "", "error_verify": "", "error_email": ""}) + page_footer
        self.response.write(main_content)

class Signup(webapp2.RequestHandler):
    #take in data
    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")

        #escape out html
        username = cgi.escape(username, quote=True)
        password = cgi.escape(password, quote=True)
        verify = cgi.escape(verify, quote=True)
        email = cgi.escape(email, quote=True)

        #assign error messages
        error_username = ""
        error_password= ""
        error_verify = ""
        error_email = ""
        error_present = False

        #regex data
        USER_RE = re.compile(r"^[a-zA-Z0-9_]{3,20}$")
        def valid_username(username):
            return username and USER_RE.match(username)

        PASS_RE = re.compile(r"^.{3,20}$")
        def valid_password(password):
            return password and PASS_RE.match(password)

        EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
        def valid_email(email):
            return not email or EMAIL_RE.match(email)


        #error no user name
        if not valid_username(username):
            error_username = "That's not a valid username"
            error_present = True

        if not valid_password(password):
            error_password = "No password submitted, please enter a password"
            error_present = True

        if password != verify:
            error_verify = "Passwords don't match"
            error_present = True

        if not valid_email(email):
            error_email = "That's not a valid email"
            error_present = True

        if error_present:
            self.response.write(render_signup_form({"username": username, "password": "" , "verify": "", "email": email, "error_username": error_username, "error_password": error_password, "error_verify": error_verify, "error_email": error_email}))
        else:
            self.redirect('/welcome?username='+ username)

class Welcome(webapp2.RequestHandler):
    def get(self):
        username = self.request.get("username")

        self.response.write('<h1>Welcome ' + username + '!</h1>')



app = webapp2.WSGIApplication([
    ('/', Index),
    ('/signup', Signup),
    ('/welcome', Welcome)
], debug=True)
