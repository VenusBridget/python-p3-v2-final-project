# lib/cli.py

from helpers import (
    exit_program,
    # helper_1
    list_playlists,
    find_playlist_by_name,
    find_playlist_by_id,
    create_playlist,
    update_playlist,
    delete_playlist,
    list_songs,
    find_song_by_title,
    find_song_by_id,
    create_song,
    update_song,
    delete_song,
    list_playlist_songs,
    list_artist_songs,
    list_artists,
    find_artist_by_name,
    find_artist_by_id,
    create_artist,
    update_artist,
    delete_artist,
    list_collabs,
    find_collab_by_title,
    find_collab_by_id,
    create_collab,
    update_collab,
    delete_collab,
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_playlists()
        elif choice == "2":
            find_playlist_by_name()
        elif choice == "3":
            find_playlist_by_id()
        elif choice == "4":
            create_playlist()
        elif choice == "5":
            update_playlist()
        elif choice == "6":
            delete_playlist()
        elif choice == "7":
            list_songs()
        elif choice == "8":
            find_song_by_title()
        elif choice == "9":
            find_song_by_id()
        elif choice == "10":
            create_song()
        elif choice == "11":
            update_song()
        elif choice == "12":
            delete_song()
        elif choice == "13":
            list_playlist_songs()
        elif choice == "14":
            list_artist_songs()
        elif choice == "15":
            list_artists()
        elif choice == "16":
            find_artist_by_name()
        elif choice == "17":
            find_artist_by_id()
        elif choice == "18":
            create_artist()
        elif choice == "19":
            update_artist()
        elif choice == "20":
            delete_artist()
        elif choice == "21":
            list_collabs()
        elif choice == "22":
            find_collab_by_title()
        elif choice == "23":
            find_collab_by_id()
        elif choice == "24":
            create_collab()
        elif choice == "25":
            update_collab()
        elif choice == "26":
            delete_collab()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all playlists")
    print("2. Find playlist by name")
    print("3. Find playlist by id")
    print("4. Create playlist")
    print("5. Update playlist")
    print("6. Delete playlist")
    print("7. List all songs")
    print("8. Find song by title")
    print("9. Find song by id")
    print("10. Create song")
    print("11. Update song")
    print("12. Delete song")
    print("13. List all songs in a playlist")
    print("14. List all songs by an artist")
    print("15. List all artists")
    print("16. Find artist by name")
    print("17. Find artist by id")
    print("18. Create artist")
    print("19. Update artist")
    print("20. Delete artist")
    print("21. List all collabs")
    print("22. Find collab by name")
    print("23. Find collab by id")
    print("24. Create collab")
    print("25. Update collab")
    print("26. Delete collab")

if __name__ == "__main__":
    main()
