list = []
print("ANIME LIST MAKER")
while True:
    anime = input("Enter the title of an anime (type 'exit' to finish): ")
    if anime.lower() == 'exit':
        print("Exiting the program...")
        break
    
    list.append(anime)
entry = len(list)
print("The following are the animes you love to watch:")
for i in range(entry):
    print(f"- {list[i]}")
print("Great choice!")