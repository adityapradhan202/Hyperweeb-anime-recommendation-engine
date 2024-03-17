import random
import numpy as np
from recommendation import recommendations as recom
from display_genres import glist


def main():

    try:

        print("Here's a list of few genres that you can search:\nGenres:")
        for i in range(len(glist)-5):
            print(f"{i+1} {glist[i]}")

        print("\nEnter genres seprated by commas...")
        user_input = input("Type the genres here: ")
        recoms = recom(user_input)

        # 5-recommedations
        first = recoms[random.randint(0, len(recoms))]
        second = recoms[random.randint(0, len(recoms))]
        third = recoms[random.randint(0, len(recoms))]
        fourth = recoms[random.randint(0, len(recoms))]
        fifth = recoms[random.randint(0, len(recoms))]

        print('\nRecommendations:')
        print(f"1. {first}")
        print(f"2. {second}")
        print(f"3. {third}")
        print(f"4. {fourth}")
        print(f"5. {fifth}")

    except Exception as e:
        print('Some exception occured!')

    finally:
        choice = input("Enter 'y' if you want to search for more anime recommendations\notherwise enter 'n':\n")
        if choice.lower() == 'y':
            main()
        elif choice.lower() == 'n':
            print('\nThanks for using our anime recommendation system!')
            exit(0)
    


if __name__ == "__main__":
    main()
        
