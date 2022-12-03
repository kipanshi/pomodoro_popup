#!/usr/bin/env python3

import time
from datetime import datetime

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

POMODORO_LENGTH = 25 * 60  # seconds


class Base(object):
    def __init__(self):
        # Main window
        self.window = Gtk.Window()
        #self.window.set_position(Gtk.WIN_POS_CENTER)
        self.window.set_size_request(300, 150)
        self.window.set_title("Pomodoro rest break")

        # Label
        self.label_1 = Gtk.Label(label="<")
        

        # Button next pomodoro
        self.button_next = Gtk.Button.new_with_label('Start next pomodoro')
        self.button_next.set_size_request(150, 40)
        self.button_next.connect('clicked', self.wait)

        # Put buttons
        fixed = Gtk.Fixed()
        fixed.put(self.button_next, 75, 55)
        fixed.put(self.label_1, 25, 25)

        self.window.add(fixed)
        self.window.show_all()
        self.window.connect('destroy', self.destroy)

    def wait(self, widget, **kwargs):
        time_lapse = kwargs.get('time_lapse', POMODORO_LENGTH)

        #self.window.hide()
        datetimenow = str(datetime.now())
        self.label_1.set_text(datetimenow)

        time_start = time.time()
        time_end = (time_start + time_lapse)

        while time_end > time.time():
            time.sleep(1)
            while Gtk.events_pending():
                Gtk.main_iteration()

        self.window.show()

    def destroy(self, widget):
        """Close main window."""
        Gtk.main_quit()

    def main(self):
        Gtk.main()


if __name__ == '__main__':
    try:
        Base().main()
    except KeyboardInterrupt:
        exit(1)
