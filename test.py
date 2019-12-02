from instapyModules.instapyy import InstaPy
from selenium import webdriver


session = InstaPy(username=insta_username,
                  password=insta_password)

session.set_dont_include(["salon", "sklep"])

session.login()
# session.like_by_tags(["podroze"], amount=15, skip_top_posts=True)
session.follow_by_tags(['wspinaczka'], amount=5)

