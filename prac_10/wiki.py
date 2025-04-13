import wikipedia


def main():
    """Prompts the user for a Wikipedia page title, then prints details of that page."""

    page_title = input("Enter page title: ").strip()
    while page_title != "":
        try:
            page = wikipedia.page(page_title, auto_suggest=False)

            print(page.title)
            print(wikipedia.summary(page_title))
            print(page.url)

        except wikipedia.exceptions.PageError:
            print(f"Page id {page_title} does not match any pages. Try another id!")

        except wikipedia.exceptions.DisambiguationError:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(wikipedia.search(page_title))

        page_title = input("Enter page title: ").strip()
    print("Thank you.")


if __name__ == '__main__':
    main()
