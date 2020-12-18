from CompanyStock import CompanyStock
import wikipedia


def get_by_name(name):
    wikipedia.set_lang("en")
    ford = CompanyStock("F", "Ford Motor Company", "https://www.akcesoria-ford.pl/Content/Images/GoFurther/logo_ford_gofurther_xl.png", wikipedia.summary("Ford Motor Company", sentences = 3))
    tesla = CompanyStock("TSLA", "Tesla, Inc.", "https://download.logo.wine/logo/Tesla%2C_Inc./Tesla%2C_Inc.-Logo.wine.png", wikipedia.summary("Tesla, Inc.", sentences = 3))
    apple = CompanyStock("AAPL", "Apple Inc.", "https://logofirmy.net/wp-content/uploads/2020/04/Apple-Logo.png", wikipedia.summary("Apple (company)", sentences = 3))

    mock_index_dict = {'Ford': ford, 'Tesla': tesla, 'Apple': apple }
    return mock_index_dict.get(name)
    


