from swapi import swapi

def get_film(film_id):
    film = swapi.get_film(film_id)
    print(f"Фільм: {film.title}")

if __name__ == '__main__':
    film = input("Введіть індетифікатор фільму: ")
    get_film(film)
