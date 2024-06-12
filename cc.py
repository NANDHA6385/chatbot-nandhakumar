def chatbot_response(user_input):
    responses={"hello":"hi there",
               "hi":"hello!",
               "how are you?":"i'm doing great,thanks!",
               "what's your name?":"i'm a chatbot created by openAI.",
               "bye":"goodbye!",
               "thank you":"you're welcome!,"}
    user_input=user_input.lower()
    return responses.get(user_input,"i don't undestand that.can you repharse?")
if __name__=="__main__":
    print("chatbot: hello! i am a simple chatbot.type 'bye' to exit.")
    while True:
        user_input=input("you:")
        if user_input.lower()=="bye":
            print("chatbot:goodbye!")
            break
        response=chatbot_response(user_input)
        print("chatbot:",response)