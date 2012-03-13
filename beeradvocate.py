from util import hook, http


def get_beer(beer):
    """ search beeradvocate.com """

    search_url = "http://beeradvocate.com/search"
    base_url = "http://beeradvocate.com"

    results = http.get_html(search_url, q=http.quote_plus(inp))
    
    try:
        result = results.xpath("//td[@id='mainContent']/div[2]/ul/li[1]")[0]
    except IndexError:
        return "No Results"
    
    page_url = base_url + result.xpath('a')[0].get('href')
    scores = http.get_html(page_url).cssselect('.BAscore_big')
    return "%s :: Community Score: %s :: Bros Score: %s :: %s" % (result.text_content(), 
                                                                  scores[0].text_content(), 
                                                                  scores[1].text_content(), page_url)

@hook.command
def beeradvocate(inp):
    return get_beer(inp)

if __name__ == "__main__":
    print get_beer("budweiser")