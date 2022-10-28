from flask import Flask, json
stage1 = [ {"slackUsername": "Susan Adesoji", "backend": True, "age": 24, "bio": "I am a software engineer" }]

api = Flask(__name__)

@api.route('/', methods=['GET'])
def get_stage1():
  return json.dumps(stage1, sort_keys=False)

if __name__ == '__main__':
    api.run() 
