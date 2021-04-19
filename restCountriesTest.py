from restcountries import RestCountryApiV2 as rapi

def foo(name):
    country_list = rapi.get_countries_by_name(name ,filters=["name","currencies","capital"])
    country = country_list[0]
    print(country.capital)

def main():
    foo("France")

if __name__ == "__main__":
    main()
