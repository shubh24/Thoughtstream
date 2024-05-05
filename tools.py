import json
import os

import requests
from langchain.tools import tool
from interpreter import interpreter

class Tools():

  @tool("Invoke OpenInterpreter to open Slack and message in DMs")
  def write_slack_message_tool(message, user):
    """Useful to invoke openinterpreter and write a Slack message"""
    interpreter.llm.model = "gpt-3.5-turbo"
    interpreter.llm.api_key = os.getenv('OPENAI_API_KEY')
    interpreter.auto_run = True

    interpreter.chat("Open Slack by using Spotlight commands on my macbook, search for the user by hitting Cmd+K. The user's name is: Rahul, search by that name and when you find the user, hit enter. Then, write them the following message: {message}")
