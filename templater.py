
from jinja2 import Environment, FileSystemLoader, select_autoescape
from collections import OrderedDict

from content_blocks import (home_content_blocks,
                            programming_content_blocks,
                            ceramics_content_blocks,
                            fossils_content_blocks)

def get_header():
    header = "Joseph Mahon"
    return header

def get_pages():
    pages = OrderedDict()
    pages["Home"] = {"url":"home.html"}
    pages["Programming/Gamedev"] =  {"url":"programming.html"}
    pages["Ceramics"] =  {"url":"ceramics.html"}
    pages["Fossils"] =  {"url":"fossils.html"}
    return pages

def get_content(page_title, page_dict):
    if page_title == "Home":
        page_content_blocks = home_content_blocks
    elif page_title == "Programming/Gamedev":
        page_content_blocks = programming_content_blocks
    elif page_title == "Ceramics":
        page_content_blocks = ceramics_content_blocks
    elif page_title == "Fossils":
        page_content_blocks = fossils_content_blocks
    page_dict["content_blocks"] = page_content_blocks
    return page_dict


def save_page():
    pass


def main():
    # Set up the environment
    env = Environment(
            loader=FileSystemLoader('templates/'),
            autoescape=select_autoescape(['html', 'xml']))
    # Get the template
    template = env.get_template('web.html')

    # Get the page headers
    header = get_header()
    # Get the different base page dicts (with just urls and titles so far)
    pages = get_pages()
    # Get the content for each page
    for page_title, page_dict in pages.items():
        # Get the content of the page
        pages[page_title] = get_content(page_title, page_dict)
        # Generate the HTML
        html_data = template.render(
                                header=header,
                                top_links=pages,
                                title=page_title,
                                content_blocks=pages[page_title]["content_blocks"]
                                )

        with open(page_dict["url"], "w") as file:
            file.write(html_data)








if __name__ == "__main__":
    main()