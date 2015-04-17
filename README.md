# PyBossa scheduler template
A template for building and adding your own scheduler to PyBossa

Schedulers are at the heart of PyBossa's logic, and they're the ones that handle
how tasks are delivered to the users when contributing to a project.
This is a simple template that will allow you to build a custom scheduler and add
it to your PyBossa server instance, without having to modify the PyBossa code at
all.

Being built as a plugin (thanks to the [Flask-plugins](https://github.com/sh4nks/flask-plugins)
Flask extension), you can also add it or remove it without affecting the rest of
the PyBossa system.

## How to build your own scheduler

You only need to write the code for the 'get_task' function defined in 
template_scheduler/__init__.py file. You also have access to all the pybossa
packages and modules from there.

Also, you may feel the need of writing some tests for your scheduler, as it is
a critical part of PyBossa software. You can find a place to put your tests in
test/test_template_schedueler.py file, where you will also have access to the test
modules and utilities defined in the PyBossa testing suite itself.

Also, don't forget to pick up a cool name for your scheduler and use it instead
of the 'template' that you'll find in the following places:

- template_scheduler package
- template_scheduler/\__init\__.py. There you'll also see two constants, SCHEDULER_NAME
and SCHEDULER_DISPLAY_NAME which are, respectively, the internal denomination for
your scheduler, and the name you will see on the web GUI in PyBossa when choosing
the scheduler for any project. Also check and rename the TemplateScheduler class
there.
- template_scheduler/info.json. Change the identifier field to match the name of
your scheduler. Also change the name field to be the name of the class renamed above.

If you need a hint, you can see a working example of a customised scheduler [here](https://github.com/PyBossa/random-scheduler).

## Installing your scheduler

Once you have it running, you can install it to your PyBossa server just by moving
the template_scheduler (though you will have renamed it) folder with all its
content (plus any additional files you may have created for your scheduler) to
the plugins folder in PyBossa. That's all, next time you boot the PyBossa server
you will have the new scheduler available.
