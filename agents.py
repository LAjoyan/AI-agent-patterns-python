from schemas import AgentPlan, TaskStep, CriticReview

def planner_agent(topic: str) -> str:
    print(f"🔍 [Planner] Creating plan for: {topic}")
    plan = AgentPlan(
        task_name=topic,
        steps=[
            TaskStep(id=1, description="Research basics"),
            TaskStep(id=2, description="Write summary")
        ]
    )
    return plan.model_dump_json()

def critic_agent(data_json: str) -> str:
    print("⚖️ [Critic] Validating work...")
    review = CriticReview(approved=True, feedback="Looks solid!", score=0.9)
    return review.model_dump_json()

def worker_agent(plan_json: str) -> str:
    plan = AgentPlan.model_validate_json(plan_json)
    print(f"🛠️ [Worker] Executing: {plan.task_name}")
    
    work_done = []
    for step in plan.steps:
        print(f"  - Completed: {step.description}")
        work_done.append(f"Done: {step.description}")
    
    return f"Work results for {plan.task_name}: {' | '.join(work_done)}"