import json
import urllib.request

class JokeGenrator:
    history=[]
    favorites=[]

    def __init__(self):
        self.history = []
        self.favorites = []

    def fetch_real_joke(self):
        url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,racist,sexist"
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": "Mozilla/5.0"}
            )
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())

                # Handles both single-line jokes and setup/punchline jokes
                if data["type"] == "single":
                    return data["joke"]
                else:
                    return f"{data['setup']}\n👉 {data['delivery']}"
        except Exception:
            return "Failed to fetch a joke. Check your internet connection!"
        
    def GenerateJoke(self):
        while(True):
            user_input = input("Press Enter to generate a joke or N to exit: ") 
            if user_input.lower() == "n":
                print("Exiting the joke generator.")
                break
            joke = self.fetch_real_joke()
            print(f"😂 {joke}\n")
            self.history.append(joke)
            while True:
                likes=input("Do you want to add to favorites (Y/N): ")
                if likes.lower()=="y":
                    self.favorites.append(joke)
                    print("⭐ Added to favorites successfully!")
                    break
                elif likes.lower()=="n":
                    print("Skipped adding to favorites.")
                    break
                else:
                    print("Wrong selection. Please enter Y or N.")


    def showFavorites(self):
        if len(self.favorites) == 0:
            print("No favorites yet.")
        else:
            print("⭐ Your Favorite Jokes:")
            for joke in self.favorites:
                print(joke)    
    def showHistory(self):
        if len(self.history) == 0:
            print("No jokes generated yet.")
        else:
            print("📜 Joke History:")
            for joke in self.history:
                print(joke)

def main():
    print("Welcome to Jokes Generator!")
    joke_gen = JokeGenrator()

    print("==========Menu===========")
    print("1. Generate a joke \n2. Show favorite jokes \n3. Show joke history \n4. Exit")
    while True:
        choice = int(input("Enter your choice (1-4) :"))
        if choice==1:
            print("==========================================")
            joke_gen.GenerateJoke()
            print("==========================================")

        elif choice==2:
            print("======================")
            joke_gen.showFavorites()
            print("======================")
                
        elif choice==3:
            print("=======================")
            joke_gen.showHistory()    
            print("=======================")
        elif choice==4:
            print("Exiting the program. Goodbye!")
            exit("Thanks for using the program! \n=============================" )
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")   

if __name__ == "__main__":
    main()