import capmonster_python.turnstile

capmonster = capmonster_python.turnstile.TurnstileTask("YOUR CAPMONSTER API KEY HERE")
task_id = capmonster.create_task("WEBSITE URL", "WEBSITE CAPTCHA TOKEN")
result = capmonster.join_task_result(task_id)
print(result.get("token"))
