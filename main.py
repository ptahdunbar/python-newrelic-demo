import os
from dotenv import load_dotenv
load_dotenv()

import newrelic.agent
newrelic.agent.initialize()

from api import generate, check_strength

# Wraps our task in a newrelic background task
def execute_task(application, task_name, times):
    with newrelic.agent.BackgroundTask(application, name=task_name):
        generate(times)
        check_strength()

def main():
    # run the task
    application = newrelic.agent.register_application(timeout=10)
    execute_task(application, "generate", 100)
    newrelic.agent.shutdown_agent(timeout=10)

if __name__ == "__main__":
    main()