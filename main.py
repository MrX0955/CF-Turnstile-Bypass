import capmonster_python.turnstile

capmonster = capmonster_python.turnstile.TurnstileTask("API KEY") #Your Capmonster Solver api key token here.
task_id = capmonster.create_task("WEBSITE URL", "WEBSITE CAPTCHA TOKEN") #Captcha Token will be like this: 0x4AAAAAAABFlgIgsFUIYIzA
result = capmonster.join_task_result(task_id)
print(result.get("token"))
