#creates a program that gives a color based off the description of an emotion
from openai import OpenAI

client = OpenAI(
    api_key = "add your own API key!!!! "
)

end_program= False
#end program will become true when the user enters the exit command
#while: While a condition is true, run the code in the loop
#until end program is true, the while loop will keep running
while not end_program:
    get_input = input("Enter a prompt: ")
    if get_input.lower() == "goodbye" or get_input.lower() == "exit":
        end_program = True #this is making it true, which stops it runnung
        print("Have a great day!")
    else:
        system_data= [ #using a dictionary to map different values, giving data to openAi to prompt response
            #the first dictionary is for the system, the second for the user
            {"role": "system", "content": "You will be provided with a description of a mood, and your task is to generate the CSS code for a color that matches it. Write your output in json with a single key called css_code."},
            {"role": "user", "content": get_input}
            #Use OpenAI to preform an API call in order to make a request to the server
        ]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=system_data
        )

        #formatted as a JSON
        #append adds it to the end of the list
        assistant_response = response.choices[0].message.content
        system_data.append({"role": "assistant", "content": assistant_response})
        print("Assistant: " + assistant_response)