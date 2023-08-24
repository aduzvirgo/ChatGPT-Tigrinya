# codded by t.me/elphad0r
"""
Every Credits dependig on this repo goes to 
Neural Programmers Offical Authors 
t.me/neuralp
t.me/neuralg
t.me/neuraltutor
demo bot t.me/chatgpt4vbot
   ..... t.me/askgptprobot

"""
from pyrogram import *
from config import *

neural = Client ('neural tutor',
                api_id=28153993, 
                api_hash=976fd7cc4958ad84181a53b41919564b, 
                bot_token=6483187732:AAH6S7RhAurKg9NvetX9uf6Q6wjQAvVYoOE,
                plugins=dict(root='plugins')
                )
                               
neural.run()                