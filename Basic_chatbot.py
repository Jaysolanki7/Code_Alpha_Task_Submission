from openai import OpenAI
import json
client = OpenAI(api_key="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")
class ChatbotMemory:
    def __init__(self, filename="conversation_history.json"):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        """Load conversation history from a JSON file."""
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_data(self):
        """Save conversation history to a JSON file."""
        with open(self.filename, "w") as file:
            json.dump(self.data, file, indent=4)

    def find_answer(self, user_input):
        
        """Check if the question already exists in saved conversations."""
        for i in range(len(self.data) - 1, -1, -1):  # Loop through messages in reverse order
            if self.data[i]["role"] == "user" and self.data[i]["content"].lower() == user_input:
                # Ensure there is a next message and it's from the assistant
                if i + 1 < len(self.data) and self.data[i + 1]["role"] == "assistant":
                    return self.data[i + 1]["content"]  # Return the chatbot's response

        return None 
            
    def add_conversation(self, user_input, bot_response):
        """Save a new user-bot conversation entry."""
        self.data.append({"role": "user", "content": user_input})
        self.data.append({"role": "assistant", "content": bot_response})
        self.save_data()
while True:
    memory = ChatbotMemory()
    user_input = input("User : ")
    if user_input.lower() in ["exit", "stop", "quit"]:
        break
        #return
    saved_response = memory.find_answer(user_input)
    if saved_response:
            print(f"Chatbot (from memory): {saved_response}")
            continue  # Skip calling OpenAI API
    elif user_input == 'none':
            continue
        # Retrieve recent conversation history to maintain context
    conversation_history = memory.data[:]  
        
    completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation_history + [{"role": "user", "content": user_input}]
        )
    ai_response = str(completion.choices[0].message.content)
        
    print(f"Chatbot : {ai_response}")
    saved_response = memory.find_answer(user_input)
    if saved_response == ai_response:
        continue
    memory.add_conversation(user_input, ai_response)