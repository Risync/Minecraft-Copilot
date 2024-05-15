import asyncio
from sydney import SydneyClient
from system.lib import minescript as mc
import sys

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def sydney_ai(question):
    # Define Sydney, giving sydney a precise style to ensure a proper response, alias as sydney for better readability
    async with SydneyClient(style='precise') as sydney:
        # the question parameter gets send after the usual prompt
        prompt = (
            # Your Static prompt goes here
            "1: Do not try to reference links using brackets like this [^1], Numerical referencing is not available. it will not work as the player is receiving your response in minecraft, this will not be clickable link so make sure to always exclude it from your response."
            "2: VERY IMPORTANT never cite a source, or post links to websites, this will cause errors for our use case."
            "3: VERY IMPORTANT DO NOT use emoji's in your response."
            "A players Question Will follow after this sentence:"
            + question
        )
        # Await the response
        response = await sydney.ask(
            prompt,
            citations=False
        )    
        mc.echo("Response:", response)


# use sys.argv[1:] so that it does not send the file name in the question
question = ' '.join(sys.argv[1:])
mc.echo("Question:", question)

asyncio.run(sydney_ai(question))
