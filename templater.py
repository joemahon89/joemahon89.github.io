
from jinja2 import Environment, FileSystemLoader, select_autoescape
from collections import OrderedDict




def main():
    # Get the environment
    env = Environment(
            loader=FileSystemLoader('templates/'),
            autoescape=select_autoescape(['html', 'xml']))
    # Get the template
    template = env.get_template('web.html')


    header= "Joseph Mahon"

    top_choices = OrderedDict()
    top_choices["Home"] = "home.html"
    top_choices["Programming"] = "projects.html"
    top_choices["Pottery"] = "test.html"

    test2 = [
            "bla1",
            "bla2",
            "bla4",
            "bla3",
            ]
            

    html_data = template.render(
                                header=header,
                                top_choices=top_choices,
                                )

    with open("completed_template.html", "w") as file:
        file.write(html_data)




if __name__ == "__main__":
    main()