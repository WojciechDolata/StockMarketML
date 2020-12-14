from CompanyStock import CompanyStock
import wikipedia


def get_by_name(name):
    wikipedia.set_lang("en")
    ford = CompanyStock("F", "Ford Motor Company", "https://www.akcesoria-ford.pl/Content/Images/GoFurther/logo_ford_gofurther_xl.png", wikipedia.summary("Ford Motor Company", sentences = 3))
    tesla = CompanyStock("TSLA", "Tesla, Inc.", "https://download.logo.wine/logo/Tesla%2C_Inc./Tesla%2C_Inc.-Logo.wine.png", wikipedia.summary("Tesla, Inc.", sentences = 3))
    # apple = CompanyStock("AAPL", "Apple Inc.", "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Apple_logo_black.svg/1200px-Apple_logo_black.svg.png", wikipedia.summary("Apple Inc.", sentences = 5))

    mock_index_dict = {'Ford': ford, 'Tesla': tesla, 'Apple': None }
    return mock_index_dict.get(name)
    


