questions = {"name":"Hi, what is your name?", "school":"Have you finished school?", "hobby":"What do you like to do?", "enemy":"Who is your enemy?"}



responseModel = {
	"questionResponse":["That's wonderful.", ".", "Very interesting, you are quite the character."],
	"help":["[[name]] I will help you"],
	"test":["[[name]] it looks like it is working. Don't you hate being around [[enemy]] [[ok]]"],
	#greeting
	"hello|hi":["Hi [[name]]", "I'm glad you've come to talk to me!"],
	#interests
	"eating|eat|hungry|food|ate|feed|fed":["[[name]], I'm starving", "[[name]], please give me some food", "Pork chops are my favorite"],
	#introductions
	"your.+name|who.+you":["[[name]]!! You forgot my name?! It's Biscuit!", "I'm Biscuit silly!", "You can call me Biscuit."]	,
	#compliments
	"cute|cool|awesome|amazing":["I think you are pretty great [[name]]!", "You're pretty cool yourself, [[name]].", "You are my best friend."],
	#insults
	"suck|stupid|dumb|boring":["You better watch it [[name]] or someone might bite you.", "Grrrrrrr Bark Bark!", "What's so great about you [[name]]?"],
	#negative
	"no|don't|won't|not|can't|cannot|hate|dislike":["Maybe you would feel better if you fed me.", "That's too bad, but what you can do is give me something to eat."],
	#positive
	"yes|like|good|love|sure|nice|ok|okay|great":["That's great, it's almost as great as how I feel when I get food.", "I'm happy for you, how about a treat to celebrate?"]
}
							
							
defaultResponses = ["Why are you speaking so much? Just get to feeding me.","That's very interesting; almost as much as dinner.", "I like turtles!"]
