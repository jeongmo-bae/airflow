def get_job_run_info(owner: str, **context):
    print("========== START ==========")
    print("owner: ", owner)
    print("===========================")
    print("hostname: ", context.get("hostname"))
    print("dag_run: ", context.get("dag_run"))
    print("task_instance: ", context.get("task_instance"))
    print("run_id: ", context.get("run_id"))
    print("========== END ==========")

