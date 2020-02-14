
from apscheduler.schedulers.background import BackgroundScheduler
from students.views import dummytaskinit

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(dummytaskinit, 'interval', minutes=1)
    scheduler.start()