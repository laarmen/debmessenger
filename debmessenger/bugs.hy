;; Copyright 2013 Simon Chopin <chopin.simon@gmail.com>
;;
;; This file is part of the debmessenger software and is placed under
;; the following license:
;;
;; Permission is hereby granted, free of charge, to any person obtaining
;; a copy of this software and associated documentation files (the
;; "Software"), to deal in the Software without restriction, including
;; without limitation the rights to use, copy, modify, merge, publish,
;; distribute, sublicense, and/or sell copies of the Software, and to
;; permit persons to whom the Software is furnished to do so, subject to
;; the following conditions:
;;
;; The above copyright notice and this permission notice shall be included
;; in all copies or substantial portions of the Software.
;;
;; THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
;; EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
;; MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
;; IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
;; CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
;; TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
;; SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

(import [ debmessenger.utils [ file-to-mail ] ])
(import [ debmessenger.message [ publish ] ])

(defn bug-to-msg [mail]
      (let ((type-nb (.split (get mail X-Debian-PR-Message) " "))
            (tags (.split (get mail "X-Debian-PR-Keywords")))
            (payload (.get_payload mail)))
        {"source" (get mail "X-Debian-PR-Source")
         "package" (get mail "X-Debian-PR-Package")
         "tags" tags
         "type" (get type-nb 0)
         "nb" (get type-nb 1)
         "title" (get mail "Subject")
         "content" (if (isinstance payload list)
                     (.get_payload (get payload 0))
                     payload)
         "patches" (if (and (in "patch" tags) (isinstance payload list))
                     (list-comp
                       (.get_payload p)
                       (p payload)
                       (= "text/x-diff" (.get_content_type p)))
                     [])}))

(setv hook (mail-hook (lambda [filename]
                        (bug-to-msg (file-to-mail filename)))
                      publish))

