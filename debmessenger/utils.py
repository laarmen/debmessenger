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

from email.parser import Parser
import traceback

def file_to_mail(filename):
    return Parser().parse(open(filename))

def get_email_body(filename):

    def _hy_anon_fn_2():
        payload = file_to_mail(filename).get_payload()
        return (payload[0] if isinstance(payload, list) else payload)
    return _hy_anon_fn_2()

def mail_hook(translator, publisher):

    def _hy_anon_fn_5(filename):
        try:

            def _hy_anon_fn_4():
                (topic, msg) = translator(filename)
                (topic, msg)
                return publisher(**{u'topic': topic, u'msg': msg})
            _hy_anon_var_1 = _hy_anon_fn_4()
        except (Exception,) as e:
            _hy_anon_var_1 = traceback.print_exc()
        return _hy_anon_var_1
    return _hy_anon_fn_5