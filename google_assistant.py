def say(response):
    return {
		"conversationToken": "",
		"expectUserResponse": True,
		"expectedInputs": [
			{
				"inputPrompt": {
					"richInitialPrompt": {
						"items": [
							{
								"simpleResponse": {
									"textToSpeech": response,
									"displayText": response
								}
							}
						],
						"suggestions": []
					}
				},
				"possibleIntents": [
					{
						"intent": "actions.intent.TEXT"
					}
				]
			}
		]
	}
