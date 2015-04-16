import pybossa.sched as sched
from pybossa.forms.forms import TaskSchedulerForm
from flask.ext.plugins import Plugin
from functools import wraps

__plugin__ = "TemplateScheduler"
__version__ = "0.0.1"

SCHEDULER_NAME = 'template'
SCHEDULER_DISPLAY_NAME = "Template"


def get_task(project_id, user_id=None, user_ip=None, n_answers=30, offset=0):
    """Add here the logic for your scheduler."""
    pass


def with_custom_scheduler(f):
    @wraps(f)
    def wrapper(project_id, sched, user_id=None, user_ip=None, offset=0):
        if sched == SCHEDULER_NAME:
            return get_task(project_id, user_id, user_ip, offset=offset)
        return f(project_id, sched, user_id=user_id, user_ip=user_ip, offset=offset)
    return wrapper


def variants_with_custom_scheduler(f):
    @wraps(f)
    def wrapper():
        return f() + [(SCHEDULER_NAME, SCHEDULER_DISPLAY_NAME)]
    return wrapper


class TemplateScheduler(Plugin):

    def setup(self):
        sched.new_task = with_custom_scheduler(sched.new_task)
        sched.sched_variants = variants_with_custom_scheduler(sched.sched_variants)
        TaskSchedulerForm.update_sched_options(sched.sched_variants())
