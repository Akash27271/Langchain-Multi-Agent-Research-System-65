from src.tools.tools import web_search, scrape_url

# output = web_search("Latest news on AI")

# print(output)

results = scrape_url("https://www.reddit.com/r/artificial/")
print(results)