
from jinja2 import Environment, FileSystemLoader, select_autoescape





def main():
    # Get the environment
    env = Environment(
            loader=FileSystemLoader('templates/'),
            autoescape=select_autoescape(['html', 'xml']))
    # Get the template
    template = env.get_template('web.html')

    test="testdata"
    test2 = [
            "bla1",
            "bla2",
            "bla4",
            "bla3",
            ]
            

    html_data = template.render(
                                test=test,
                                test2=test2,
                                )

    with open("completed_template.html", "w") as file:
        file.write(html_data)




if __name__ == "__main__":
    main()