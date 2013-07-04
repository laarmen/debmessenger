#!/usr/bin/env python

import sys

import hy.importer
from pyinotify import WatchManager, IN_MOVED_TO, Notifier, ProcessEvent

from debmessenger import changes

class EventHandler(ProcessEvent):
    def process_IN_MOVED_TO(self, event):
        changes.hook(event.pathname)

wm = WatchManager()
wm.add_watch(sys.argv[1], IN_MOVED_TO)

notifier = Notifier(wm, EventHandler())
notifier.loop()

