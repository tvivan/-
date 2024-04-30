from openai import OpenAI
from prompt import prompt_table
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def user_message(inquiry):
    user_message = (
        f"""      
You are calculation bot. Your job is analyze provided tables in <> and answer on inquire in <<>>.
You must provide calculations to show dynamic in data you provided.
Also you must calculate expected result for 2023 and 2024 based on information you provided.
Try to simulate Arima,Arch,Garch or something else models to show analytics.
Dont show process, just show the result and very short explanation
You must give commentary to every singe table you provided
If you can't calculate, just assume possible variation.
Repsonce must looks simillire to that form:
1.Table №
2. Grow and down in data
3. Predictions on 2023 and 2024
strictly to the form. All three points must be to each table
ALWAYS ANSWER IN RUSSIAN
<
{table}
>
<<Inquiry:{prompt_table()}>>
        """
    )
    return user_message


def classify_inquiry(inquiry):

    prompt = user_message(inquiry)
    completion = client.chat.completions.create(
        model="TheBloke/Mistral-7B-Instruct-v0.2-GGUF",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=1.0,
    )


    response = str(completion.choices[0].message.content.strip())
    return response

    response = str(completion.choices[0].message.content.strip())
    return response

if __name__ == "__main__":
    question = "Найди зависимости между таблицами и предскажи резульаты на 2023 и 2024 года"
    print(classify_inquiry(question))


