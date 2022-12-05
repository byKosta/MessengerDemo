# МЕССЕНДЖЕР

# Список всех сообщений
messages_list = []

# Функция для добавления новых сообщений (имя отправителя, текст сообщений) в список
def add_message(name, text):
    new_message = {
        "name": name,
        "text": text,
        "time": "23:34", # ДЗ: Подставить текущее время Часы:Минуты
    }
    messages_list.append(new_message)

add_message("Майк", "Йо, это первое сообщение")
add_message("Витя", "А чо так можно было чтоли?")


# Функция для чтения сообщений
def print_messages_list():
    # for in
    # Для каждого сообщения в списке сообщений, сделать следующее:
    for message in messages_list:
        # Здесь идет код, который может сделать какие-либо действия с сообщением message
        name = message["name"]
        text = message["text"]
        time = message["time"]
        print(f"[{name}]: {text} // {time} ")
        
        print(messages_list)
        


