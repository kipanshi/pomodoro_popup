#!/usr/bin/env python

import time

import pygtk
pygtk.require('2.0')
import gtk

POMODORO_LENGTH = 25 * 60  # seconds


class Base(object):
    def __init__(self):
        # Main window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.set_size_request(300, 150)
        self.window.set_title("Pomodoro rest break")

        # Button next pomodoro
        self.button_next = gtk.Button('Start next pomodoro')
        self.button_next.set_size_request(150, 40)
        self.button_next.connect('clicked', self.wait)

        # Put buttons
        fixed = gtk.Fixed()
        fixed.put(self.button_next, 75, 55)

        self.window.add(fixed)
        self.window.show_all()
        self.window.connect('destroy', self.destroy)

    def wait(self, widget, **kwargs):
        time_lapse = kwargs.get('time_lapse', POMODORO_LENGTH)

        self.window.hide()

        time_start = time.time()
        time_end = (time_start + time_lapse)

        while time_end > time.time():
            while gtk.events_pending():
                gtk.main_iteration()

        self.window.show()

    def destroy(self, widget):
        """Close main window."""
        gtk.main_quit()

    def main(self):
        gtk.main()


if __name__ == '__main__':
    try:
        Base().main()
    except KeyboardInterrupt:
        exit(1)
