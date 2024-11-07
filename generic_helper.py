
import re

def get_str_from_food_dict(food_dict: dict):
    result = ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])
    return result


def extract_session_id(session_str: str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string

    return ""

def get_str_from_food_dict(food_dict: dict):
    result = ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])
    return result


if __name__ == "__main__":
    #print(extract_session_id("projects/ritu-chatbot-for-food-del-immc/agent/sessions/7b17691c-3347-127b-6119-662df5c69881/contexts/ongoing-order"))
    print(get_str_from_food_dict({"samosa":2,"pizza":3}))