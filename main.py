from agents import planner_agent, worker_agent, critic_agent
import json


def main():
    print("\n🚀 --- Starting Multi-Agent Workflow ---")

    topic = input("📝 Enter a topic for the agents to work on: ")

    approved = False
    attempts = 0
    max_attempts = 3
    current_topic = topic

    while not approved and attempts < max_attempts:
        attempts += 1
        print(f"\n🔄 --- Attempt {attempts} ---")

        plan_json = planner_agent(current_topic)

        work_result = worker_agent(plan_json)

        review_json = critic_agent(work_result)
        review = json.loads(review_json)

        approved = review["approved"]

        if not approved:
            print(f"❌ Rejected by Critic: {review['feedback']}")
            current_topic = f"{current_topic} (REVISED: provide more detail)"
        else:
            print(f"✅ Approved by Critic! Score: {review['score']}")

    if not approved:
        print("\n⚠️ Workflow stopped: Max attempts reached without approval.")
    else:
        print("\n🎯 Workflow Complete: Result is high quality.")


if __name__ == "__main__":
    main()
