from agents import planner_agent, worker_agent, critic_agent


def main():
    print("\n🚀 --- Starting Multi-Agent Workflow ---")

    topic = input("📝 Enter a topic for the agents to work on: ")

    if not topic:
        print("❌ No topic provided. Exiting.")
        return

    plan_json = planner_agent(topic)

    work_result = worker_agent(plan_json)

    review_json = critic_agent(work_result)

    print("\n✅ --- Workflow Complete ---")
    print(f"Final Critic Review: {review_json}")


if __name__ == "__main__":
    main()
