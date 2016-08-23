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
#html boilerplate for bottom of page
page_footer = """
</body>
</html>
"""
class Index(webapp2.RequestHandler):

    def get(self):
    #create form
        signup_form="""
        <form action="/signup" method="post">
        <label for="username">Username: </label>
        <input name="username" type="text">
        <br>
        <label for="password">Password: </label>
        <input name="password" type="password">
        <br>
        <label for="verify">Verify Password: </label>
        <input name="verify" type="password">
        <br>
        <label for="email">Email Address: </label>
        <input name="email" type="text">
        <br>
        <input type="submit" value="Submit">
        </form>
        """
        main_content = page_header + signup_form + page_footer
        self.response.write(main_content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
