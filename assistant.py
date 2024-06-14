#OPENAI API
#Use library from first day and API key from OPEN AI to acess
#ChatGPT through Python

from openai import OpenAI
#libraries are sets of commands created by other programmers

client=OpenAI(
    api_key="add your own API key!!!"
)

#opening our json file to read the data
open_file= open("dataset.json", "rb") #rb only gives persmission to be read and not edited

#allows us to send file over to OpenAI
data_file = client.files.create(
    file=open_file,
    purpose='assistants'
)

ai_assistant = client.beta.assistants.create(
    name="Trip Planner",
    instructions="You are an application with special expertise in recommending the most popular tourist spots in a "
                 "given area based on the information you are provided with. Depending on the preferred"
                 " area,  cost, and hobbies, you are required to name the best city, tourist attractions, and "
                 "cost for the person.",

    model="gpt-3.5-turbo",
    tools=[{"type":"file_search"}]
)

prompt=input("Enter a prompt")
thread= client.beta.threads.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
            "attachments": [
                {"file_id": data_file.id, "tools": [{"type": "file_search"}]}
            ]
        }
    ]
)

print("\n#########################################")
print("Thread id: "+ thread.id)
print("Assistant id: " + ai_assistant.id)
print("#########################################\n")

run= client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id=ai_assistant.id
)

if run.status == 'completed':
    messages=client.beta.threads.messages.list(
        thread_id=thread.id
    )
    print("User: " + messages.data[1].content[0].text.value)
    print("Assistant:" + messages.data[0].content[0].text.value)

    print("\n###############################")
    print("Run id: " + run.id)
else:
    print(run.status)