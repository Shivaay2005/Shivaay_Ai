 # import openai
# import os

# # Set your OpenAI API key here
# openai.api_key = "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"

# # Shivaay chatbot function
# def shivaay_chatbot():
#     print("Shivaay: Hi! I'm Shivaay, your study assistant for computer science. Ask me anything!")
#     print("Type 'exit' anytime to end the conversation.")
    
#     while True:
#         # Get user input
#         user_input = input("\nYou: ").strip()
        
#         # Exit condition
#         if user_input.lower() in ['exit', 'bye']:
#             print("Shivaay: Goodbye! Keep learning and coding! 😊")
#             break
        
#         try:
#             # Call the OpenAI API to generate a response
#             response = openai.ChatCompletion.create(
#                 model="gpt-3.5-turbo",  # You can also use "gpt-4" if available in your API
#                 messages=[
#                     {"role": "system", "content": "You are Shivaay, a highly knowledgeable computer science study assistant."},
#                     {"role": "user", "content": user_input}
#                 ]
#             )
            
#             # Extract and print the AI's response
#             answer = response['choices'][0]['message']['content']
#             print(f"Shivaay: {answer}")
        
#         except Exception as e:
#             print(f"Shivaay: Sorry, I encountered an error: {e}")

# # Run the chatbot
# if __name__ == "__main__":
#     shivaay_chatbot()




# import openai
# import os

# # Set your OpenAI API key here
# openai.api_key = "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"

# # Shivaay chatbot function
# def shivaay_chatbot():
#     print("Shivaay: Hi! I'm Shivaay, your study assistant for computer science. Ask me anything!")
#     print("Type 'exit' anytime to end the conversation.")
    
#     while True:
#         # Get user input
#         user_input = input("\nYou: ").strip().lower()
        
#         # Exit condition
#         if user_input in ['exit', 'bye']:
#             print("Shivaay: Goodbye! Keep learning and coding! 😊")
#             break
        
#         # Check for specific introduction-related questions
#         if "who trained you" in user_input or "who made you" in user_input or "who are you" in user_input:
#             print("Shivaay: I was created by Mr. Shivaay to help with computer science. I'm here to assist you!")
#             continue
        
#         # Check if user asks about Shivaay
#         if "tell me about Shivaay" in user_input or "who is Shivaay" in user_input or "what about Shivaay" in user_input:
#             print(shivaay_info())
#             continue
        
#         # Check if user asks about Vishal
#         if "who is Vishal" in user_input or "tell me about Vishal" or "Vishal kon hai" in user_input:
#             print(vishal_info())
#             continue
        
#         # Check if user asks about Prateek
#         if "who is Prateek" in user_input or "tell me about Prateek" or "Prateek kon hai "in user_input:
#             print(prateek_info())
#             continue
        
#         # Check if user asks about Rohit
#         if "who is Rohit" in user_input or "tell me about Rohit" in user_input:
#             print(rohit_info())
#             continue
        
#         # Check if user asks about Nitish
#         if "who is Nitish" in user_input or "tell me about Nitish" in user_input:
#             print(nitish_info())
#             continue
        
#         try:
#             # Call the OpenAI API to generate a response
#             response = openai.ChatCompletion.create(
#                 model="gpt-3.5-turbo",  # You can also use "gpt-4" if available in your API
#                 messages=[
#                     {"role": "system", "content": "You are Shivaay, a friendly and easy-to-understand computer science study assistant."},
#                     {"role": "user", "content": user_input}
#                 ]
#             )
            
#             # Extract and print the AI's response
#             answer = response['choices'][0]['message']['content']
            
#             # Simplify the answer to make it easy to understand
#             simplified_answer = simplify_answer(answer)
#             print(f"Shivaay: {simplified_answer}")
        
#         except Exception as e:
#             print(f"Shivaay: Sorry, I encountered an error: {e}")

# # Function to simplify the answers
# def simplify_answer(answer):
#     # This function can be improved to use specific rules or even external libraries
#     # to simplify the text. For now, let's just ensure the response is short and clear.
#     simplified = answer.replace("can", "could").replace("may", "might").replace("is", "means").replace("therefore", "so")
#     # Example of removing complex terms
#     simplified = simplified.replace("implement", "use").replace("functionality", "feature")
#     return simplified

# # Function to provide details about Shivaay (developer)
# def shivaay_info():
#     info = """
#     Shivaay (Mr. Priyanshu) is a highly skilled developer and a passionate computer science enthusiast. 
#     He specializes in web development, programming, and artificial intelligence. He has experience 
#     working with various programming languages such as Python, JavaScript, C, and C++.

#     Shivaay loves to help students and learners by creating useful tools and assistants for their studies. 
#     He is also working on various advanced projects to make computer science more accessible and enjoyable.
    
#     If you need help with anything related to computer science or programming, Shivaay is always ready to assist!
#     """
#     return info

# # Function to provide details about Vishal (friend)
# def vishal_info():
#     info = """
#     Vishal is a highly skilled individual with a passion for sports, motivation, and self-improvement. 
#     He excels in volleyball and is known for his determination and focus. Vishal is also an ambivert, 
#     enjoying both social interactions and quiet moments for reflection.

#     If you need motivation or help with anything related to sports or personal growth, Vishal is always there to inspire you!
#     """
#     return info

# # Function to provide details about Prateek (friend)
# def prateek_info():
#     info = """
#     Prateek is a brilliant student with a keen interest in technology and problem-solving. He is known 
#     for his logical thinking and loves tackling challenging coding problems. Prateek has a strong grasp of 
#     algorithms and data structures, making him a valuable team player in any tech-related project.

#     Whether you need coding advice or help with understanding complex algorithms, Prateek is there to assist you!
#     """
#     return info

# # Function to provide details about Rohit (friend)
# def rohit_info():
#     info = """
#     Rohit is an enthusiastic learner who is passionate about science and mathematics. He has an aptitude 
#     for understanding complex concepts in physics and is always eager to dive deep into technical subjects. 
#     Rohit is also a great team collaborator, known for his patience and ability to explain difficult concepts in simple terms.

#     If you're struggling with scientific theories or mathematical problems, Rohit is always ready to lend a hand!
#     """
#     return info

# # Function to provide details about Nitish (friend)
# def nitish_info():
#     info = """
#     Nitish is a skilled individual who is passionate about machine learning and artificial intelligence. 
#     He is constantly exploring new technologies and improving his skills in coding. Nitish is dedicated to 
#     making an impact in the tech field, and he is always excited to work on innovative projects.

#     If you're interested in machine learning or AI, Nitish is the perfect person to talk to!
#     """
#     return info

# # Run the chatbot
# if __name__ == "__main__":
#     shivaay_chatbot()



import openai
import os

# Set your OpenAI API key here
openai.api_key = "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"

# Shivaay chatbot function
def shivaay_chatbot():
    print("Shivaay: Hi! I'm Shivaay, your study assistant for computer science. Ask me anything!")
    print("Type 'exit' anytime to end the conversation.")
    
    while True:
        # Get user input
        user_input = input("\nYou: ").strip().lower()
        
        # Exit condition
        if user_input in ['exit', 'bye']:
            print("Shivaay: Goodbye! Keep learning and coding! 😊")
            break
        
        # Check for specific introduction-related questions
        if "who trained you" in user_input or "who made you" in user_input or "who are you" in user_input:
            print("Shivaay: I was created by Mr. Shivaay to help with computer science. I'm here to assist you!")
            continue
        
        # Check if user asks about Shivaay
        if "tell me about Shivaay" in user_input or "who is Shivaay" in user_input or "what about Shivaay" in user_input:
            print(shivaay_info())
            continue

        try:
            # Call the OpenAI API to generate a response
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # You can also use "gpt-4" if available in your API
                messages=[
                    {"role": "system", "content": "You are Shivaay, a friendly and easy-to-understand computer science study assistant."},
                    {"role": "user", "content": user_input}
                ]
            )
            
            # Extract and print the AI's response
            answer = response['choices'][0]['message']['content']
            
            # Simplify the answer to make it easy to understand
            simplified_answer = simplify_answer(answer)
            print(f"Shivaay: {simplified_answer}")
        
        except Exception as e:
            print(f"Shivaay: Sorry, I encountered an error: {e}")

# Function to simplify the answers
def simplify_answer(answer):
    # This function can be improved to use specific rules or even external libraries
    # to simplify the text. For now, let's just ensure the response is short and clear.
    simplified = answer.replace("can", "could").replace("may", "might").replace("is", "means").replace("therefore", "so")
    # Example of removing complex terms
    simplified = simplified.replace("implement", "use").replace("functionality", "feature")
    return simplified

# Function to provide details about Shivaay (developer)
def shivaay_info():
    info = """
    Shivaay (Mr. Priyanshu) is a highly skilled developer and a passionate computer science enthusiast. 
    He specializes in web development, programming, and artificial intelligence. He has experience 
    working with various programming languages such as Python, JavaScript, C, and C++.

    Shivaay loves to help students and learners by creating useful tools and assistants for their studies. 
    He is also working on various advanced projects to make computer science more accessible and enjoyable.
    
    If you need help with anything related to computer science or programming, Shivaay is always ready to assist!
    """
    return info

# Run the chatbot
if __name__ == "__main__":
    shivaay_chatbot()
