import json
import threading
import time
import datetime
import asyncio
from pathlib import Path


import sys
from pathlib import Path

# Add the project root to Python path
sys.path.append(str(Path(__file__).parent.parent.parent))  # goes up to system_optic/

# Now use absolute import
from whatsapp_aut_test.automation.whatsapp_worker import WhatsAppAutomation
# from automation.whatsapp_worker import WhatsAppAutomation

JOBS_FILE = Path("jobs.json")

class JobScheduler:
    def __init__(self, ui_callback=None):
        """
        ui_callback: optional function to notify UI about status updates
        """
        self.ui_callback = ui_callback
        self.jobs = []
        self.running = False

    def load_jobs(self):
        if JOBS_FILE.exists():
            with open(JOBS_FILE, "r") as f:
                self.jobs = json.load(f)
        else:
            self.jobs = []

    def save_jobs(self):
        with open(JOBS_FILE, "w") as f:
            json.dump(self.jobs, f, indent=4)

    def add_job(self, job):
        self.jobs.append(job)
        self.save_jobs()

    def delete_job(self, index):
        if 0 <= index < len(self.jobs):
            self.jobs.pop(index)
            self.save_jobs()

    def start(self):
        self.running = True
        threading.Thread(target=self._run, daemon=True).start()

    def stop(self):
        self.running = False

    def _run(self):
        while self.running:
            now = datetime.datetime.now()
            for job in self.jobs:
                if not job.get("done", False):
                    job_time = datetime.datetime.strptime(job["datetime"], "%Y-%m-%d %H:%M")
                    if now >= job_time:
                        asyncio.run(self._trigger_job(job))
                        job["done"] = True
                        self.save_jobs()
            time.sleep(30)  # check every 30s

    async def _trigger_job(self, job):
        chat_name = job.get("chat_name")
        phone = job.get("phone")
        message = job["message"]
        persistent = job.get("persistent", False)

        if self.ui_callback:
            self.ui_callback(f"⏰ Triggering job for {chat_name or phone}...")

        wa = WhatsAppAutomation(headless=False)
        success = await wa.send_message(
            phone=phone if phone else None,
            name=chat_name if chat_name else None,
            message=message
        )

        if self.ui_callback:
            if success:
                self.ui_callback(f"✅ Message sent to {chat_name or phone}")
            else:
                self.ui_callback(f"❌ Failed to send to {chat_name or phone}")
