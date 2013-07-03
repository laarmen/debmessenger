(import [ email.parser [ Parser ] ])

(defn get-email-body [filename]
      (.get_payload (.parse (Parser)
                            (open filename))))

(defn mail-hook [translator publisher]
      (lambda (filename)
        (let ((msg-tuple (translator (get-email-body filename))))
          (kwapply (publisher)
                   { "topic" (get msg-tuple 0)
                     "msg" (get msg-tuple 1)
                   }))))
