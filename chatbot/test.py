import os

from dotenv import load_dotenv, find_dotenv
load_dotenv()
# e = find_dotenv()

#set the env values just outside of virtual environment
custom_env_path = lambda a : '/'.join(os.get_exec_path()[0].split('\\')[:-2])+'/'+a
# basepath = os.path()
# envars = basepath.cwd() / 'config.env'
load_dotenv(custom_env_path('chatter.env'))
print (os.getenv("OPENAI_API_KEY"))
#e = os.get_exec_path()[0]
#print ('/'.join(os.get_exec_path()[0].split('\\')[:-1])+'.env')
#print (custom_env_path('chatter.env'))




#print (e)


