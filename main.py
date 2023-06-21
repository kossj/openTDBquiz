from enum import Enum
import requests


class Trivia_Difficulty(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"
    
class Trivia_Type(Enum):
    MULTIPLE_CHOICE = "multiple"
    TRUE_FALSE = "boolean"
    
def get_questions(number_questions: int = 10, difficulty: Trivia_Difficulty = None, type: Trivia_Type = None):
    trivia_url = "https://opentdb.com/api.php"
    none_print_format = lambda param, arg: f"&{param}={arg}" if arg else ""
    r = requests.get(f"{trivia_url}/?amount={number_questions}{none_print_format('difficulty', difficulty)}{none_print_format('type', type)}")
    print(r)
        
def main():
    get_questions(5, Trivia_Difficulty.EASY)
    get_questions(type=Trivia_Type.TRUE_FALSE)

if __name__ == '__main__':
    main()
