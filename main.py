from dotenv import load_dotenv
load_dotenv()

from crewai import Crew

from tasks import Tasks
from agents import Agents

tasks = Tasks()
agents = Agents()

task_at_hand = input("What do you need help with today?\n")
people_to_involve = input("Are there any specific people you would want to include in this task?\n")
tone = input("What kind of setting is this: professional, casual, romantic, neutral\n")

# Create Agents
executive_assistant = agents.executive_assistant()
comms_agent = agents.comms_agent()
# ops_agent = agents.ops_agent()

# Define Tasks for each agent
understand_user_intent_task = tasks.understand_user_intent_task(executive_assistant, task_at_hand)
identify_people_to_reachout_task = tasks.identify_people_to_reachout_task(comms_agent, people_to_involve)
communicate_with_stakeholder_task = tasks.communicate_with_stakeholder_task(comms_agent, tone, people_to_involve)
# execute_ops_task = tasks.execute_ops_task(ops_agent, task_at_hand)

# Instantiate the crew with a sequential process
crew = Crew(
    agents=[executive_assistant, comms_agent],
    tasks=[
        understand_user_intent_task,
        identify_people_to_reachout_task,
        communicate_with_stakeholder_task,
        # execute_ops_task
    ],

)

# Kick off the process
result = crew.kickoff()

print("Result:")
print(result)