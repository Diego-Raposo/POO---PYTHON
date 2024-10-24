"""
WARNING:

Please make sure you install the bot dependencies with `pip install --upgrade -r requirements.txt`
in order to get all the dependencies on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the dependencies.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at
https://documentation.botcity.dev/tutorials/python-automations/web/
"""


# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

from webdriver_manager.chrome import ChromeDriverManager

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

class formBase:
     def __init__(self, nome, email, data_nascimento):
          self.nome = nome 
          
          self.email = email 
    
          self.data_nascimento = data_nascimento

class formContato(formBase):
     def __init__(self, nome, email, data_nascimento, telefone, endereco):
          super().__init__(nome, email, data_nascimento)
          self.telefone = telefone 
          self.endereco = endereco 

class formLogin(formContato):
     def __init__(self, nome,  email,  data_nascimento, telefone, endereco, usuario,senha):
          super().__init__(nome, email, data_nascimento, telefone, endereco)
          self.usuario = usuario
          self.senha = senha

formulario = formBase("Diego da Silva Raposo",  'Diego.eimec@gmail.com', '19/12/1999')
def preencher_forms(bot):
        while len(bot.find_elements('//*[@id="nome"]',By.XPATH))<1:
            bot.wait(1000)
            print("carregando")
        bot.find_element('//*[@id="nome"]', By.XPATH).send_keys(formulario.nome)
        bot.wait(1000)
        bot.find_element('//*[@id="email"]', By.XPATH).send_keys(formulario.email)
        bot.wait(1000)
        bot.find_element('//*[@id="data_nascimento"]', By.XPATH).send_keys(formulario.data_nascimento)
        bot.wait(1000)
        bot.find_element('/html/body/div/form/input[4]', By.XPATH).click()
    


formulario2 = formContato("Diego da Silva Raposo", 'Diego.eimec@gmail.com', '19/12/1999', '986209329','Rua Manjericão, n° 174')
def preencher_forms_contato(bot):
        while len(bot.find_elements('//*[@id="nome"]',By.XPATH))<1:
            bot.wait(1000)
            print("carregando")
        bot.find_element('//*[@id="nome"]', By.XPATH).send_keys(formulario.nome)
        bot.wait(1000)
        bot.find_element('//*[@id="email"]', By.XPATH).send_keys(formulario.email)
        bot.wait(1000)
        bot.find_element('//*[@id="data_nascimento"]', By.XPATH).send_keys(formulario.data_nascimento)
        bot.wait(1000)
        bot.find_element('//*[@id="telefone"]', By.XPATH).send_keys(formulario2.telefone)
        bot.wait(1000)
        bot.find_element('//*[@id="endereco"]', By.XPATH).send_keys(formulario2.endereco)
        bot.wait(1000)
        bot.find_element('/html/body/div/form/input[6]', By.XPATH).click()

formulario3 = formLogin("Diego da Silva Raposo", 'Diego.eimec@gmail.com','19/12/1999', '986209329','Rua Manjericão, n° 174', 'Raposo', '94371160')
def preencher_forms_login(bot):
        while len(bot.find_elements('//*[@id="nome"]',By.XPATH))<1:
            bot.wait(1000)
            print("carregando")
        bot.find_element('//*[@id="nome"]', By.XPATH).send_keys(formulario3.nome)
        bot.wait(1000)
        bot.find_element('//*[@id="email"]', By.XPATH).send_keys(formulario3.email)
        bot.wait(1000)
        bot.find_element('//*[@id="data_nascimento"]', By.XPATH).send_keys(formulario3.data_nascimento)
        bot.wait(1000)
        bot.find_element('//*[@id="telefone"]', By.XPATH).send_keys(formulario3.telefone)
        bot.wait(1000)
        bot.find_element('//*[@id="endereco"]', By.XPATH).send_keys(formulario3.endereco)
        bot.wait(1000)
        bot.find_element('//*[@id="new_usuario"]', By.XPATH).send_keys(formulario3.usuario)
        bot.wait(1000)
        bot.find_element('//*[@id="new_senha"]', By.XPATH).send_keys(formulario3.senha)
        bot.wait(1000)
        bot.find_element('/html/body/div/form/input[8]', By.XPATH).click()


def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    # Configure whether or not to run on headless mode
    bot.headless = False

    # Uncomment to change the default Browser to Firefox
    bot.browser = Browser.CHROME


    # Uncomment to set the WebDriver path
    bot.driver_path = ChromeDriverManager().install()

   
    # Opens the BotCity website.
    bot.browse("http://127.0.0.1:5500/formbase.html")
    preencher_forms(bot)
    bot.wait(2000)
    bot.browse("http://127.0.0.1:5500/formContato.html")
    preencher_forms_contato(bot)
    bot.wait(2000)
    bot.browse("http://127.0.0.1:5500/formLogin.html")
    preencher_forms_login(bot)
    bot.wait(2000)
    

    # Implement here your logic...
    ...

    # Wait 3 seconds before closing
    bot.wait(3000)

    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    bot.stop_browser()

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
