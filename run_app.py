from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
agent = Agent.load('./models/dialogue',interpreter=nlu_interpreter)

input_channel = SlackInput('xoxp-492286150006-490280401569-492288668806-588b262b1528c5fdb2ebd0bd885bec45',
							'xoxb-492286150006-490282925649-tt7OIktA8llJa3i5qifua6nc',
							'kINqWSpOpZRrvuE3pllzhJhT',
							True
							)

agent.handle_channel(HttpInputChannel(5004,'/',input_channel))

