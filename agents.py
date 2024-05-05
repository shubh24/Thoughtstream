from crewai import Agent
# from crewai_tools.tools import WebsiteSearchTool, SerperDevTool, FileReadTool
from tools import Tools

class Agents():
	def executive_assistant(self):
		return Agent(
			role='Executive Assistant to your Manager',
			goal='Help your manager with all their tasks, understand their intent, and invoke the relevant agents to complete the task',
			tools=[],
			backstory='Expert in understanding your manager, their needs, their habits, their relationships, and how to get the job done.',
			verbose=True
		)

	def comms_agent(self):
			return Agent(
				role='Senior Communications Manager',
				goal='Given a task, engage with the relevant stakeholders via communication tools like Slack and Telegram, using the right tone and language.',
				tools=[Tools.write_slack_message_tool],
				backstory='Skilled in asking the right questions, following up, and getting the required answer from the stakeholders',
				verbose=True
			)

	def ops_agent(self):
			return Agent(
				role='Operations Manager',
				goal='Given an operational task, able to use all the tools at your disposal to get the job done, whether that be setting up a meeting or getting a lunch delivered.',
				tools=[],
				backstory='A meticulous Operations Manager with an eye for detail, ensuring every task is completed using the appropriate tooling.',
				verbose=True
			)
