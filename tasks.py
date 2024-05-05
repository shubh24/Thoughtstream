from textwrap import dedent
from crewai import Task

class Tasks():
		def understand_user_intent_task(self, agent, task_at_hand):
				return Task(
						description=dedent(f"""\
								Analyze the provided task: {task_at_hand} and based on the intent, figure out the user intent and come up with a plan of action"""),
						expected_output=dedent("""\
								A comprehensive plan detailing the tasks to be done by the other agents at your disposal."""),
						agent=agent
				)

		def identify_people_to_reachout_task(self, agent, people_to_involve):
				return Task(
						description=dedent(f"""\
								Based on the executive assistant's needs and the people involved: {people_to_involve}, list out the people that we need to engage with."""),
						expected_output=dedent("""\
								A list of people that we need to reachout to."""),
						agent=agent
				)

		def communicate_with_stakeholder_task(self, agent, tone):
				return Task(
						description=dedent(f"""\
								Draft a message for the stakeholders in the following tone: {tone}
								"""),
						expected_output=dedent("""\
								A detailed, engaging message to be shared with the stakeholder."""),
						agent=agent
				)

		def execute_ops_task(self, agent, task_at_hand):
				return Task(
						description=dedent(f"""\
								Given the task: {task_at_hand}, now figure out the plan-of-action for any operational job that needs to be done"""),
						expected_output=dedent("""\
								Final output of all tasks that were done by the Ops Agent"""),
						agent=agent,
				)

