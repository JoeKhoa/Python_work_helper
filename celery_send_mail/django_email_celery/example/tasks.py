### tasks.py (in any of your app)


from __future__ import absolute_import
from celery import shared_task

from celery.decorators import task
from celery.utils.log import get_task_logger
from time import sleep
from .inform_using_mail import send_mail_to

# @shared_task
# def test(param):
#     return 'The test task executed with argument "%s" ' % param


# sleeplogger = get_task_logger(__name__)@task(name='my_first_task')

@shared_task
def my_first_task(duration):
    print('running my_first_task CELERY!')
    subject= 'Celery send mail test'
    message= 'My task done successfully'
    receiver= 'bluenight0105@gmail.com'
    is_task_completed= False
    error=receiver_m
    try:
        sleep(duration)
        is_task_completed= True
    except Exception as err:
        error= str(err)
        logger.error(error)
    if is_task_completed:
        send_mail_to(subject,message,receivers)
    else:
        send_mail_to(subject,error,receivers)
    return('first_task_done')
