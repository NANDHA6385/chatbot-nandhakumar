def chatbot_response(user_input):
    responses={"hello":"hi there!",
               "how are you":"i'm doing great, thanks!",
               "bye":"goodbye!"}
    user_input-user_input.lower()
    return responses.get(user_input,"I don't understand that.")
while True:
    user_input= input("you:")
    if user_input.lower()=="bye":
        print("chatbot:goodbye!")
        break
    print("chatbot:",
          chatbot_response(user_input))