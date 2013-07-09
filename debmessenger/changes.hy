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

(import [debian.deb822 [Changes Deb822Dict]])
(import [io [FileIO]])
(import [debmessenger.utils [mail-hook get-email-body]])
(import [debmessenger.message [publish]])

(defn undeb822 [item]
      (cond ((isinstance item Deb822Dict)
             (let ((new_dict {}))
               (do
                 (for (key (iter item))
                      (assoc new_dict key (undeb822 (get item key))))
                 new_dict)))
            ((isinstance item list)
             (let ((new_list []))
               (do (for (i item)
                        (.append new_list (undeb822 i)))
                 new_list)))
            (True item))) ;; Return the item if not the right type

(defn changes-to-msg [filename]
      (let ((ch (Changes (get-email-body filename))))
        (, (+ "changes." (get ch "Source")) (undeb822 ch))))

(setv hook (mail-hook changes-to-msg publish))

