(import [debian.deb822 [Changes]])
(import [io [FileIO]])
(import [debmessenger.utils [mail-hook]])
(import [debmessenger.message [publish]])

(defn changes-to-msg [body]
      (let ((ch (Changes (body))))
        [(+ "changes." (.get_as_string ch "Source"))
         ch]))

(setv hook (mail-hook changes-to-msg publish))
