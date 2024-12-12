import io
from cProfile import label
import customtkinter as ctc
import requests
from PIL import Image, ImageTk
import textwrap

app = ctc.CTk()
app.geometry("400x400")
app.title("Potter Finder")
ctc.set_default_color_theme("dark-blue")


def books_click(book_index):
    if book_index > 7:
        error_app = ctc.CTkToplevel()
        error_app.title("Error")
        error_label = ctc.CTkLabel(
            error_app,
            text="Index out of range, \n this API don't have this many indexes.",
            font=("CTkFont", 20),
        )
        error_label.pack()
        return

    book_app = ctc.CTkToplevel()
    label_book_name = ctc.CTkLabel(book_app, font=("Garamond", 25))
    label_photo = ctc.CTkLabel(book_app, text=None, font=("Garamond", 25))
    label_release = ctc.CTkLabel(
        book_app, text=None, justify="center", font=("Garamond", 25)
    )
    label_description = ctc.CTkLabel(
        book_app, text=None, justify="center", font=("Garamond", 25)
    )
    label_pages = ctc.CTkLabel(book_app, font=("Garamond", 25))

    url = f"https://potterapi-fedeperin.vercel.app/en/books?index={book_index}"
    response = requests.get(url)
    data = response.json()

    label_book_name.configure(text=data["title"])
    label_release.configure(text=f'Release date: {data["releaseDate"]}')
    wrapped_description = "\n".join(textwrap.wrap(data["description"], width=80))
    label_description.configure(text=wrapped_description)
    label_pages.configure(text=f"Number of pages: {data['pages']}")

    image_url = data["cover"]
    image_data = requests.get(image_url)
    picture = ctc.CTkImage(Image.open(io.BytesIO(image_data.content)), size=(261, 381))
    label_photo.configure(image=picture)


    label_book_name.pack()
    label_release.pack()
    label_photo.pack()
    label_description.pack()
    label_pages.pack()


def characters_click(book_index):
    if book_index > 24 or 0 > book_index:
        error_app = ctc.CTkToplevel()
        error_app.title("Error")
        error_label = ctc.CTkLabel(
            error_app,
            text="Index out of range, \n this API doesn't have this many indexes.",
            font=("CTkFont", 20),
        )
        error_label.pack()
        return

    book_app = ctc.CTkToplevel()
    label_character_name = ctc.CTkLabel(book_app, font=("Garamond", 25))
    label_house = ctc.CTkLabel(book_app, font=("Garamond", 25))
    label_children = ctc.CTkLabel(book_app, font=("Garamond", 25))
    label_birthdate = ctc.CTkLabel(book_app, font=("Garamond", 25))
    label_photo = ctc.CTkLabel(book_app, text=None, width=350, height=500)

    url = f"https://potterapi-fedeperin.vercel.app/en/characters?index={book_index}"
    response = requests.get(url)
    data = response.json()

    if "children" in data and data["children"]:
        label_children.configure(text=f'Children: {", ".join(data["children"])}')
    else:
        label_children.configure(text="This character has no children")

    label_character_name.configure(text=f'Full name: {data["fullName"]}')
    label_house.configure(text=f"House: {data['hogwartsHouse']}")
    label_birthdate.configure(text=f"Birthdate: {data['birthdate']}")

    image_url = data["image"]
    image_data = requests.get(image_url)
    picture = ctc.CTkImage(Image.open(io.BytesIO(image_data.content)), size=(350, 500))
    label_photo.configure(image=picture)

    label_house.pack()
    label_character_name.pack()
    label_photo.pack()
    label_children.pack()
    label_birthdate.pack()


def houses_click(book_index):
    if book_index > 3:
        error_app = ctc.CTkToplevel()
        error_app.title("Error")
        error_label = ctc.CTkLabel(
            error_app,
            text="Index out of range, \n this API doesn't have this many indexes.",
            font=("CTkFont", 20),
        )
        error_label.pack()
        return

    url = f"https://potterapi-fedeperin.vercel.app/en/houses?index={book_index}"
    response = requests.get(url)
    data = response.json()

    book_app = ctc.CTkToplevel()
    label_house_name = ctc.CTkLabel(book_app, font=("Garamond", 25))
    label_emoji = ctc.CTkLabel(book_app, font=("Garamond", 25))
    label_founder = ctc.CTkLabel(book_app, font=("Garamond", 25))
    label_colors = ctc.CTkLabel(book_app, font=("Garamond", 25))
    label_animal = ctc.CTkLabel(book_app, font=("Garamond", 25))

    label_colors.configure(text=f'Colors: {", ".join(data["colors"])}')
    label_founder.configure(text=f'Founder: {data["founder"]}')
    label_house_name.configure(text=f'House name: {data["house"]}')
    label_emoji.configure(text=f'Emoji: {data["emoji"]}')
    label_animal.configure(text=f'Animal: {data["animal"]}')

    label_house_name.pack()
    label_emoji.pack()
    label_founder.pack()
    label_colors.pack()
    label_animal.pack()


def spells_click(book_index):
    if book_index > 71:
        error_app = ctc.CTkToplevel()
        error_app.title("Error")
        error_label = ctc.CTkLabel(
            error_app,
            text="Index out of range, \n this API doesn't have this many indexes.",
            font=("CTkFont", 20),
        )
        error_label.pack()
        return

    book_app = ctc.CTkToplevel()
    label_spell_name = ctc.CTkLabel(book_app, font=("Garamond", 25))
    label_use = ctc.CTkLabel(book_app, font=("Garamond", 25))
    url = f"https://potterapi-fedeperin.vercel.app/en/spells?index={book_index}"
    response = requests.get(url)
    data = response.json()
    label_spell_name.configure(text=f'Name: {data["spell"]}')
    label_use.configure(text=f'Usage: {data["use"]}')
    label_spell_name.pack()
    label_use.pack()


tabview = ctc.CTkTabview(app, width=400, height=400)

tabview.add("Books")
tabview.add("Characters")
tabview.add("Houses")
tabview.add("Spells")


def search_book():
    try:
        search_index = int(entry_books.get())
        books_click(search_index)
    except ValueError:
        error_app = ctc.CTkToplevel()
        error_app.title("Error")
        error_label = ctc.CTkLabel(
            error_app,
            text="Please enter a valid number.",
            font=("CTkFont", 20),
        )
        error_label.pack()


search_books = ctc.CTkButton(
    tabview.tab("Books"),
    text="SEARCH",
    width=380,
    height=40,
    command=search_book,
    corner_radius=0,
)
scroll_books = ctc.CTkScrollableFrame(tabview.tab("Books"), width=400)
url = f"https://potterapi-fedeperin.vercel.app/en/books"
response = requests.get(url)
data = response.json()
titles = [book["title"] for book in data]
for index, title in enumerate(titles):
    all_book = ctc.CTkButton(
        scroll_books,
        text=title,
        command=lambda i=index: books_click(i),
        width=400,
        corner_radius=0,
    )
    all_book.pack()


scroll_characters = ctc.CTkScrollableFrame(tabview.tab("Characters"), width=400)
url = "https://potterapi-fedeperin.vercel.app/en/characters"
response = requests.get(url)
data = response.json()
titles = [character["fullName"] for character in data]
for index, title in enumerate(titles):

    all_characters = ctc.CTkButton(
        scroll_characters,
        text=title,
        command=lambda i=index: characters_click(i),
        width=400,
        corner_radius=0,
    )
    all_characters.pack()


scroll_houses = ctc.CTkScrollableFrame(tabview.tab("Houses"), width=400)
url = "https://potterapi-fedeperin.vercel.app/en/houses"
response = requests.get(url)
data = response.json()
titles = [house["house"] for house in data]

for index, title in enumerate(titles):
    all_houses = ctc.CTkButton(
        scroll_houses,
        text=title,
        command=lambda i=index: houses_click(i),
        width=400,
        corner_radius=0,
    )
    all_houses.pack()


def search_character():
    try:
        search_index = int(entry_characters.get())
        characters_click(search_index)
    except ValueError:
        error_app = ctc.CTkToplevel()
        error_app.title("Error")
        error_label = ctc.CTkLabel(
            error_app,
            text="Please enter a valid number.",
            font=("CTkFont", 20),
        )
        error_label.pack()


search_characters = ctc.CTkButton(
    tabview.tab("Characters"),
    text="SEARCH",
    width=380,
    height=40,
    command=search_character,
)


def search_house():
    try:
        search_index = int(entry_houses.get())
        houses_click(search_index)
    except ValueError:
        error_app = ctc.CTkToplevel()
        error_app.title("Error")
        error_label = ctc.CTkLabel(
            error_app,
            text="Please enter a valid number.",
            font=("CTkFont", 20),
        )
        error_label.pack()


search_houses = ctc.CTkButton(
    tabview.tab("Houses"),
    text="SEARCH",
    command=search_house,
    width=380,
    corner_radius=0,
    height=40,
)


def search_spell():
    try:
        search_index = int(entry_spells.get())
        spells_click(search_index)
    except ValueError:
        error_app = ctc.CTkToplevel()
        error_app.title("Error")
        error_label = ctc.CTkLabel(
            error_app,
            text="Please enter a valid number.",
            font=("CTkFont", 20),
        )
        error_label.pack()


search_spells = ctc.CTkButton(
    tabview.tab("Spells"), text="SEARCH", width=380, height=40, command=search_spell
)

scroll_spells = ctc.CTkScrollableFrame(tabview.tab("Spells"), width=400)
url = "https://potterapi-fedeperin.vercel.app/en/spells"
response = requests.get(url)
data = response.json()
titles = [spell["spell"] for spell in data]
for index, title in enumerate(titles):
    all_spells = ctc.CTkButton(
        scroll_spells,
        text=title,
        command=lambda i=index: spells_click(i),
        width=400,
        corner_radius=0,
    )
    all_spells.pack()

entry_books = ctc.CTkEntry(
    tabview.tab("Books"),
    placeholder_text="Search for books (max index = 7)",
    width=380,
    height=60,
)

entry_characters = ctc.CTkEntry(
    tabview.tab("Characters"),
    placeholder_text="Search for characters (max index = 24)",
    width=380,
    height=60,
)

entry_houses = ctc.CTkEntry(
    tabview.tab("Houses"),
    placeholder_text="Search for houses (max index = 3)",
    width=380,
    height=60,
)

entry_spells = ctc.CTkEntry(
    tabview.tab("Spells"),
    placeholder_text="Search for spells (max index = 71)",
    width=380,
    height=60,
)

entry_books.pack(expand=True)
entry_characters.pack(expand=True)
entry_houses.pack(expand=True)
entry_spells.pack(expand=True)

search_books.pack()
search_characters.pack()
search_houses.pack()
search_spells.pack()

scroll_books.pack()
scroll_characters.pack()
scroll_houses.pack()
scroll_spells.pack()

tabview.pack()

app.mainloop()
