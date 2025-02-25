from crewai_tools import ScrapeWebsiteTool

# To enable scrapping any website it finds during it's execution
tool = ScrapeWebsiteTool()

# Initialize the tool with the website URL, 
# so the agent can only scrap the content of the specified website
tool = ScrapeWebsiteTool(website_url='https://universe.leagueoflegends.com/en_US/story/champion/skarner/')

# Extract the text from the site
text = tool.run()
print(text)