from collections import deque

def is_palindrome(text: str) -> bool:
    """
    Перевіряє, чи є рядок паліндромом.
    Ігнорує пробіли та регістр.
    
    Parameters:
        text (str): Вхідний рядок.
    
    Returns:
        bool: True, якщо паліндром, інакше False.
    """
    # Попередня обробка рядка: видалити пробіли та привести до нижнього регістру
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())

    # Додати всі символи до двосторонньої черги
    chars = deque(cleaned_text)

    # Порівнювати символи з обох кінців
    while len(chars) > 1:
        left = chars.popleft()
        right = chars.pop()
        if left != right:
            return False

    return True

if __name__ == "__main__":
    user_text = input("Enter a string to check if it's a palindrome: ")
    if is_palindrome(user_text):
      print("It's a palindrome!")
    else:
      print("It's not a palindrome.")