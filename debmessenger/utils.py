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

from email.header import decode_header
from email.message import Message
from email.parser import Parser
import traceback


class UnicodeMessage(Message):
    @staticmethod
    def decode_email_header(header):
        parts = []
        for part, encoding in decode_header(header):
            parts.append(part.decode(encoding or "utf-8"))

        return u''.join(parts)

    def __getitem__(self, item):
        ret = Message.__getitem__(self, item)

        return self.decode_email_header(ret)


def file_to_mail(filename):
    return Parser(UnicodeMessage).parse(open(filename))


def get_email_body(filename):
    payload = file_to_mail(filename).get_payload()
    return payload[0] if isinstance(payload, list) else payload


def mail_hook(translator, publisher):
    def hook(filename):
        try:
            topic, msg = translator(filename)
            publisher(**{u'topic': topic, u'msg': msg})
        except (Exception,) as e:
            traceback.print_exc()
    return hook
