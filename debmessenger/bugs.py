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

from debmessenger.utils import file_to_mail, mail_hook
from debmessenger.message import publish

def bug_to_msg(mail):
    type_nb = mail[u'X-Debian-PR-Message'].split(u' ')
    tags = mail.get(u'X-Debian-PR-Keywords', u'').split()
    payload = mail.get_payload()
    if isinstance(payload, list) and 'patch' in tags:
        patches = [p.get_payload() for p in payload if p.get_content_type == u'text/x-diff']
    else:
        patches = []
    return [u'bugs.{}'.format(type_nb[0]), {
        u'from': mail[u'From'],
        u'source': mail[u'X-Debian-PR-Source'],
        u'package': mail[u'X-Debian-PR-Package'],
        u'tags': tags,
        u'type': type_nb[0],
        u'nb': type_nb[1],
        u'title':
        mail[u'Subject'],
        u'content': (payload[0].get_payload() if isinstance(payload, list) else payload),
        u'patches': patches
    }]

hook = mail_hook((lambda filename: bug_to_msg(file_to_mail(filename))), publish)
