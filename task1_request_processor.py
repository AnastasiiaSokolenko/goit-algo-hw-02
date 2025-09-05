import queue
import random
import time

# Створення черги заявок
request_queue = queue.Queue()
request_id = 1  # Унікальний номер заявки

def generate_request():
    """Генерує нову заявку та додає її до черги."""
    global request_id
    request = f"Заявка №{request_id}"
    request_queue.put(request)
    print(f"[+] Додано: {request}")
    request_id += 1

def process_request():
    """Обробляє заявку з черги, якщо черга не пуста."""
    if not request_queue.empty():
        request = request_queue.get()
        print(f"[-] Обробляється: {request}")
        # Імітація обробки
        time.sleep(random.uniform(0.5, 1.5))
        print(f"[✓] Завершено: {request}")
    else:
        print("[!] Черга пуста. Немає заявок для обробки.")

def main():
    print("Симуляція сервісного центру. Натисніть Ctrl+C для завершення.")
    try:
        while True:
            # Генерація нових заявок з певною ймовірністю
            if random.random() < 0.7:  # 70% ймовірність додати заявку
                generate_request()

            # Обробка заявки
            process_request()

            # Затримка між циклами
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[!] Програма завершена користувачем.")

if __name__ == "__main__":
    main()