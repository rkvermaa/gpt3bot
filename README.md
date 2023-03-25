
# AI Application using GPT-3

This application is a chatbot which is build using chatgpt- API. this is the explanation document to run this application 


## Folder structure
 * [tree-md](./tree-md)
 * [gpt3bot](./gpt3bot)
   * [main.py](./gpt3bot/main.py)
   * [readme.io](./gpt3bot/readme.io)
    * [templates](./templates)
        * [home.html](./templates/home.html)


main.py is the file which is to be run for opening the application

## API Reference

Chatgpt uses provide following type of model 



| model | Type         |
| :-------- | :------- |
| `text-davichi-003` | `string` |
| `text-davichi-002` | `string` |
| `text-davichi-001` | `string` |
| `text-curie-001` | `string` |
| `text-babbage-001` | `string` |
| `text-ada-001` | `string` |

in main file under generate_response(_) function, model parameter is define in engine



```python
def generate_response(prompt):
    completions = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=256,
            n=1,
            stop=None,
            temperature=0.5,
        )
        message = completions.choices[0].text
        return message.strip()
}
```


## Steps to run application

1. install all the required library 

    ```python
    pip install openai
    pip install request
    pip install flask


2. make sure to have API handy , genrate it from the https://platform.openai.com/overview website

![click on encircled ](https://github.com/rkverma87/gpt3bot/blob/main/images/img1.PNG)

make sure to save the key , as you will not be able to see it again
![click on encircled](https://github.com/rkverma87/gpt3bot/blob/main/images/img2.PNG)

3. Paster the newly genrated API in the code where API is defined

4. run the main.py file in IDE, you will get follwing message. 

![copy the local host URL and paste it on browser](https://github.com/rkverma87/gpt3bot/blob/main/images/image3.PNG)

now the bot is running on local host

Note: bot may not be responding due to expiring of API or if usage of API is used, these error has been handled in the code 

Entire app is deployed on the following URL, click on the following URL and check the result.

http://gpt3app.pythonanywhere.com/

Thank you !
