from flask import Flask, request
import requests
import os

app = Flask(__name__)
#This project is still in the idea phase read more here: https://trello.com/c/0sfsu3tD/24-new-roblox-python-api-wrapper
@app.route('/requestProduct/', methods=['POST'])
def requestProduct():
	pass