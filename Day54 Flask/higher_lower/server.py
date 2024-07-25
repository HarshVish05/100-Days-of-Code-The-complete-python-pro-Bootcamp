from flask import Flask
import random


app = Flask('__name__')

number = random.randint(0,9)

@app.route('/')
def home_page():
    return '''<h1>Guess the number between 0 to 9</h1>
            <img src= "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExOTMzbDR1ZWsxZWx4NXk2OGE3MzNsbGpjZHEwbHl6Zm0wb2NrOXNtdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/21T5tmCRksyw6rCoEF/giphy.gif"  >
            '''

@app.route('/<int:guessnum>')
def higher_or_lower(guessnum):

    if number > guessnum:
        return '''<p>Too Low. Guess Again</p>
                <img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGxubGZpZG01MG1yeWU5d29lcjFvaWs1NG1ndGZkNmN0YW1tZW9ybyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TgmiJ4AZ3HSiIqpOj6/giphy.gif" > 
                '''
    elif number < guessnum:
        return '''<p>Too High. Guess Again</p>
                <img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZzNzeHdqOWFienpqNWl4a2ZoNGNpcjJ6aHZ0aTdyMHh3ZnFhOGFzaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/79eQOjPPrisR9B2zy6/giphy.gif" > 
                '''
    else:
        return '''<p>Hurray!!!!</p>
                <img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExc2J2YnNzd3JxanM4aTM5M21wYmV1dXk2MzlndjMzYzJvc293ZHR1YSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/11sBLVxNs7v6WA/giphy.gif" > 
                '''
    
    


if __name__ == "__main__":
    
    app.run(debug= True)