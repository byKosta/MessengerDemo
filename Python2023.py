#Messenger
import time
messages_list=[]
message_user=""
message_text=""
message_time=""
stop_word="Exit"
def add_message(name,text,time):
  new_message={
      'name' : name,
      'text' : text,
      'time' : message_time
  }
  messages_list.append(new_message)
while message_user != stop_word:
  message_user=input("\nInput your name [or Exit for exiting]: ")
  message_text=input("Input your message: ")
  message_time=time.ctime()
  add_message(message_user,message_text,message_time)
print("\nChat history:")
def print_messages():
  for message in messages_list:
    name=message["name"]
    text=message["text"]
    time=message["time"]
    print(f"\nUser: {name} \nMessage: {text} \nTime: {time}")

print_messages()

