import media
import fresh_tomatoes

#Create instance for Toy Story
toy_story = media.Movie("Toy Story", "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc", "22 November 1995", "John Lasseter")
#Create instance for Avatar
avatar = media.Movie("Avatar", "A Paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is home", "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY", "18 December 2009", "James Cameron")
#Create instance for The Dark Knight
the_dark_knight = media.Movie("The Dark Knight", "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice.", "http://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg", "https://www.youtube.com/watch?v=EXeTwQWrcwY", "18 July 2008", "Christopher Nolan" )
#Create instance for Inception
inception = media.Movie("Inception", "A thief who steals corporate secrets through use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.", "http://upload.wikimedia.org/wikipedia/en/thumb/7/7f/Inception_ver3.jpg/220px-Inception_ver3.jpg", "https://www.youtube.com/watch?v=8hP9D6kZseM", "16 July 2010", "Christopher Nolan")
#Create instance for Fight Club
fight_club = media.Movie("Fight Club", "An insomniac office worker looking for a way to change his life crosses paths with a devil-may-care soap maker and they form an underground fight club that evolves into something much, much more...", "http://upload.wikimedia.org/wikipedia/en/thumb/f/fc/Fight_Club_poster.jpg/220px-Fight_Club_poster.jpg", "https://www.youtube.com/watch?v=SUXWAEX2jlg", "15 October 1999", "David Fincher")
#Create instance for Forrest Gump
forrest_gump = media.Movie("Forrest Gump", "Forrest Gump, while not intelligent, has accidentally been present at many historic moments, but his true love, Jenny Curran, eludes him.", "http://upload.wikimedia.org/wikipedia/en/thumb/6/67/Forrest_Gump_poster.jpg/220px-Forrest_Gump_poster.jpg", "https://www.youtube.com/watch?v=uPIEn0M8su0", "6 July 1994", "Robert Zemeckis" )

#create list of movies and pass to open movies function
movies = [toy_story, avatar, inception, the_dark_knight, fight_club, forrest_gump]
fresh_tomatoes.open_movies_page(movies)

