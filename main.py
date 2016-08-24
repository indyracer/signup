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

#declare error
error = ""
username=""
email=""
#html boilder plate for top of page

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Sign Up</title>
</head>
<body>
    <h1>Signup</h1>
"""

#create form
signup_form="""
    <form action="/signup" method="post">
        <table>
            <tr>
                <td>
                    <label for="username">Username: </label>
                </td>
                <td>
                    <input name="username" type="text" value="%(username)s"/>
                </td>
                <td><div style="color: red">%(error)s</div></td>
            </tr>
            <tr>
                <td>
                    <label for="password">Password: </label>
                </td>
                <td>
                    <input name="password" type="password" />
                    <span class="error"></span>
            </tr>
            <tr>
                <td>
                    <label for="verify">Verify Password: </label>
                </td>
                <td>
                    <input name="verify" type="password" />
                    <span class="error"></span>
                </td>
            </tr>
            <tr>
                <td>
                    <label for="email">Email Address: </label>
                </td>
                <td>
                    <input name="email" type="text" value="%(email)s" />
                    <span class="error"></span>
                </td>
            </tr>
        </table>
        <input type="submit" value="Submit">
    </form>
    """ % {"error": error, "username":username, "email":email}




#html boilerplate for bottom of page
page_footer = """
</body>
</html>
"""
class Index(webapp2.RequestHandler):
    #print header and form
    def get(self):
        main_content = page_header + signup_form + error + page_footer
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
        email = cgi.escape(email,quote=True)


        #error no user name
        if username == "":
            global error
            error = "That's not a valid username"
            self.response.write(page_header + signup_form + page_footer)
            #getting blank form



app = webapp2.WSGIApplication([
    ('/', Index),
    ('/signup', Signup)
], debug=True)
