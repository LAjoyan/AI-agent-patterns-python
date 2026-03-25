from schemas import AgentPlan, TaskStep, CriticReview

def planner_agent(topic: str) -> str:
    print(f"🔍 [Planner] Creating plan for: {topic}")
    plan = AgentPlan(
        task_name=topic,
        # Now the steps include the actual topic name!
        steps=[
            TaskStep(id=1, description=f"Research basics of {topic}"),
            TaskStep(id=2, description=f"Write a technical summary about {topic}")
        ]
    )
    return plan.model_dump_json()

def critic_agent(work_result: str) -> str:
    print("⚖️ [Critic] Validating work...")

    print("DEBUG work_result:", work_result)

    # Extract topic
    topic = work_result.split("Work results for ")[1].split(":")[0]
    print("DEBUG topic:", topic)

    # ✅ NEW LOGIC (this is the important part)
    is_good_effort = len(topic) > 20

    review = CriticReview(
        approved=is_good_effort,
        feedback="Great detail!" if is_good_effort else "Too brief, provide more detail.",
        score=0.95 if is_good_effort else 0.2
    )
    return review.model_dump_json()

def worker_agent(plan_json: str) -> str:
    plan = AgentPlan.model_validate_json(plan_json)
    print(f"🛠️ [Worker] Executing: {plan.task_name}")
    
    work_done = []
    for step in plan.steps:
        print(f"  - Completed: {step.description}")
        work_done.append(f"Done: {step.description}")
    
    return f"Work results for {plan.task_name}: {' | '.join(work_done)}"