import requests 
from colorama import Fore, Style, init

init(autoreset=True)

def print_ascii_art():
    """
    АСКИ
    """
    ascii_art = """
 ________  ______                                             __ 
/        |/      \\                                           /  |
$$$$$$$$//$$$$$$  |        _______   ______   _______    ____$$ |
   $$ |  $$ | _$$/        /       | /      \\ /       \\  /    $$ |
   $$ |  $$ |/    |      /$$$$$$$/ /$$$$$$  |$$$$$$$  |/$$$$$$$ |
   $$ |  $$ |$$$$ |      $$      \\ $$    $$ |$$ |  $$ |$$ |  $$ |
   $$ |  $$ \\__$$ |       $$$$$$  |$$$$$$$$/ $$ |  $$ |$$ \\__$$ |
   $$ |  $$    $$/       /     $$/ $$       |$$ |  $$ |$$    $$ |
   $$/    $$$$$$/        $$$$$$$/   $$$$$$$/ $$/   $$/  $$$$$$$/ 

                        
                                                                 
                                                     
"""
    print(Fore.CYAN + Style.BRIGHT + ascii_art)
# Я НАСРАЛ В ТУРБИНУ САМОЛЕТА
def send_message(bot_token, chat_id, message):
    """
    Отправляет сообщения в тг бота

    :param bot_token: АПИ бота
    :param chat_id:   Айди чата
    :param message: Текст
    """
    base_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }

    response = requests.post(base_url, json=payload)
    if response.status_code == 200:
        print(Fore.GREEN + "Сообщение успешно отправлено!")
    else:
        print(Fore.RED + f"Ошибка при отправке сообщения: {response.status_code}")
        print(Fore.RED + f"Описание ошибки: {response.json().get('description', 'Неизвестная ошибка')}")

if __name__ == "__main__":
    print_ascii_art()

    print(Fore.YELLOW + "Добро пожаловать в TGSEND")
    print(Fore.YELLOW + "Введите данные")
    
    bot_token = input(Fore.BLUE + "Введи HTTP API бота:" + Fore.WHITE).strip()
    
    while True:
        try:
            chat_id = input(Fore.BLUE + "Введи ChatID человека или же exit: " + Fore.WHITE).strip()
            if chat_id.lower() == "exit":
                print(Fore.BLUE + "Выход из программы.")
                break

            message = input(Fore.BLUE + "Введи текст: " + Fore.WHITE).strip()
            send_message(bot_token, chat_id, message)
        except Exception as e:
            print(Fore.RED + f"Произошла ошибка: {e}")
