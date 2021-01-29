
from jinja2 import Environment, FileSystemLoader, select_autoescape
from collections import OrderedDict

from content_blocks import (home_content_blocks,
                            programming_content_blocks,
                            ceramics_content_blocks,
                            fossils_content_blocks,
                            ImageBlock)

def get_header():
    header = "Joseph Mahon"
    return header

def get_pages():
    pages = OrderedDict()
    pages["Home"] = {"url":"index.html", "hidden":"false"}
    pages["Programming/Gamedev"] =  {"url":"programming.html", "hidden":"false"}
    pages["Ceramics"] =  {"url":"ceramics.html", "hidden":"false"}
    pages["Fossils"] =  {"url":"fossils.html", "hidden":"false"}
    pages["Privacy Policy"] =  {"url":"privacy_policy.html", "hidden":"true"}
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
    elif page_title == "Privacy Policy":
        page_content_blocks = privacy_policy_content_blocks
    page_dict["content_blocks"] = page_content_blocks
    return page_dict


def convert_content(page_dict):
    """Sometimes will need to change the content of a content block,
    for example if its some images and need to place them neatly"""
    cleaned_content_blocks = []
    for index, content_block in enumerate(page_dict["content_blocks"]):
        # Images are added as lists
        if type(content_block) == ImageBlock:
            image_block_html = create_image_block_html(content_block)
            cleaned_content_blocks.append(image_block_html)
        # Text can remain as text, just wrapped in <p> tags
        else:
            cleaned_content_blocks.append("<p>" + content_block + "</p>")
    page_dict["content_blocks"] = cleaned_content_blocks
    return page_dict

    
def create_image_block_html(image_content_block):
    image_content_block_html = []
    width_per_image = 100 / len(image_content_block.image_paths)
    image_content_block_html.append('<div class="row">')
    for image_path in image_content_block.image_paths:
        image_content_block_html.append(
                f'<div class="column" style="width:{width_per_image}%">' +
                f'<img src="{image_path}" alt="{image_path}" style="width:100%">' +
                f'</div>'
                )
    image_content_block_html.append('</div>')
    image_content_block_html_string = "".join(image_content_block_html)
    return image_content_block_html_string

'''
     <div class="row">
      <div class="column">
        <img src="images/landerlarry01.png" alt="ll_titlescreen" style="width:100%">
      </div>
      <div class="column">
        <img src="images/landerlarry02.jpg" alt="ll_image1" style="width:100%">
      </div>
      <div class="column">
        <img src="images/landerlarry03.jpg" alt="ll_image2" style="width:100%">
      </div>
    </div> 

    ''',





def save_page():
    pass


def main():
    # Set up the environment
    env = Environment(
            loader=FileSystemLoader('templates/'),
            autoescape=select_autoescape(['html', 'xml']))
    # Get the template
    template = env.get_template('web.html')
    output_dir = "joemahon89.github.io/"

    # Get the page headers
    header = get_header()
    # Get the different base page dicts (with just urls and titles so far)
    pages = get_pages()
    # Get the content for each page
    for page_title, page_dict in pages.items():
        # Get the content of the page
        pages[page_title] = get_content(page_title, page_dict)
        # Convert some of the content (get proper HTML for image gallery etc)
        pages[page_title] = convert_content(page_dict)
        print(pages[page_title]["content_blocks"])
        # Generate the HTML
        html_data = template.render(
                                header=header,
                                top_links=pages,
                                title=page_title,
                                content_blocks=pages[page_title]["content_blocks"]
                                )

        with open(output_dir+page_dict["url"], "w") as file:
            file.write(html_data)








if __name__ == "__main__":
    main()