# Copyright 2013 Simon Chopin <chopin.simon@gmail.com>
#
# This file is part of the debmessenger software and is placed under
# the following license:
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from debian.deb822 import Changes, Deb822Dict
from io import FileIO
from debmessenger.utils import mail_hook, get_email_body
from debmessenger.message import publish

def undeb822(item):
    if isinstance(item, Deb822Dict):
        new_dict = {}
        for key in iter(item):
            new_dict[key] = undeb822(item[key])
        return new_dict
    if isinstance(item, list):
        new_list = []
        for i in item:
            new_list.append(undeb822(i))
        return new_list
    return item

def changes_to_msg(filename):
    ch = Changes(get_email_body(filename))
    return ((u'package.upload'), undeb822(ch))

hook = mail_hook(changes_to_msg, publish)
