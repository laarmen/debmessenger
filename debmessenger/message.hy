(import [ fedmsg.core [FedMsgContext] ] )
(import [ fedmsg.config [load_config] ])
(import [ threading [ RLock ] ])

(setv __fedmsg_name "debmessenger")
(setv __context (let ((config (load_config)))
                  (do
                    (assoc config "name" __fedmsg_name)
                    (kwapply (FedMsgContext) config))))
(setv __context_lock (RLock))

(defn publish [&rest args &kwargs kwargs]
      (with [__context_lock]
            (apply __context.publish args kwargs)))
