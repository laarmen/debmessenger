#!/usr/bin/env python

import sys

from pyinotify import WatchManager, IN_CREATE, Notifier, ProcessEvent

from debmessenger import package, bug

hooks = {
        sys.argv[1]: package.hook,
        sys.argv[2]: bug.hook,
        }

class EventHandler(ProcessEvent):
    def process_IN_CREATE(self, event):
        hooks[event.path](event.pathname)

wm = WatchManager()
for dir in sys.argv[1:]:
    wm.add_watch(dir, IN_CREATE)

notifier = Notifier(wm, EventHandler())
notifier.loop()

