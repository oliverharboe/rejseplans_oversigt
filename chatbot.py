import json
f = open('data.json')
data = json.load(f)
print("hej jeg er en chatbot")
while(True) :
    message = input().lower()
    if message in data['q_n_a'][0]:
        print(data['q_n_a'][0][message])
    elif message == "stop" :
        break
    else :
        print("Jeg forstår ikke hvad du mener")
        f.close()

