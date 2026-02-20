import anvil.server
import requests
# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
@anvil.server.callable
def fetch(u):
  x=requests.get('https://v1.nocodeapi.com/bfcomics/github/gYLKaAnlBYFADiBX/repos?username='+u)
  y=x.json()
  return y

@anvil.server.route('/git')
def git():
  return anvil.server.FormResponse('Gitfetch')