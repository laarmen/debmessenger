#!/usr/bin/env python

import sys

import hy.importer
from pyinotify import WatchManager, IN_MOVED_TO, Notifier, ProcessEvent

from debmessenger import changes, bugs

hooks = {
        sys.argv[1]: changes.hook,
        sys.argv[2]: bugs.hook,
        }

class EventHandler(ProcessEvent):
    def process_IN_MOVED_TO(self, event):
        hooks[event.path](event.pathname)

wm = WatchManager()
wm.add_watch(sys.argv[1], IN_MOVED_TO)

notifier = Notifier(wm, EventHandler())
notifier.loop()

