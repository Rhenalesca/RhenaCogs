import random
from discord.ext import commands

# THIS IS A GUESS NUMBER GAME.
# Players get 5 guesses.
# They must guess a random number between 1 to 100.

@commands.command(pass_context=True)
    async def guessnumber(self, ctx):
        """Try guessing the number and win money!"""
        attempts = 5
        guess = 0
        reward = 0
        user = ctx.message.author
        await self.bot.say("I have picked a number from 1 to 100. Guess what it is. Guessing the number will give you a $5000 reward! You only get 5 tries, though.")
        secret_number = random.randint(1, 100)
        for attempts in range(attempts):
            guess = await self.bot.wait_for_message(author=ctx.message.author)
            if (guess.content).isdigit():
                if int(guess.content) < secret_number:
                    await self.bot.say('Higher...')
                elif int(guess.content) > secret_number:
                    await self.bot.say('Lower...')
                else:
                    await self.bot.say('You guessed it!, {}. The number was '.format(user.mention)+str(secret_number))
                    await self.bot.say('$5000 has been deposited into your account.')
                    reward = 5000
                    self.bank.deposit_credits(ctx.message.author, reward)
                    break

            else:
                await self.bot.say('You idiot. Put a number.')

        if int(guess.content) != secret_number:
            await self.bot.say('Sorry {}, you reached the maximum number of tries!').format(user.mention)
            await self.bot.say('The secret number was {}'.format(secret_number))

def setup(bot):
    bot.add_cog(GuessTheNumber(bot))
