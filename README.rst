==============
Pomodoro popup
==============

The "pomodoro" technique is very handy in programming, it helps
not to dive into "tunneling" and makes your work more pleasure and refreshing.

The technique I use can be described in several steps:

1) Choose a task and set timer for 25 minutes.
2) Start timer and work on the task (we call it "start pomodoro")
3) Write a note about your progress done. Stop pomodoro.
4) Rest for 3-5 minutes by walking, doing some music, etc.
5) After being refreshed and done some gym, repeat step **1**.

`pomodoro_popup.py` -- is a simple Python GTK app, that every 25 minutes raises a popup window reminding you to stop pomodoro and rest.

*Requirements*: pygtk >= 2.0, gtk

Just run it by:

    python pomodoro_popup.py

or

    ./pomodoro_popup.py
