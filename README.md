<!--CONTENT_START-->
```lua
-- initialize user profile
local ptdewey = {}

-- user info
ptdewey.info = {
    name = "patrick dewey",
    education = {
        masters = "computer science at virginia tech",
        bachelors = "computational modeling and data analytics at virginia tech"
    },
    experience = {
        "software engineering",
        "data science",
        "computational science"
    }
}

-- user stats
ptdewey.stats = {
    total_repositories = 25,
    total_stargazers = 58,
    total_commits_current_year = 254,
    total_prs = 33,
    total_issues = 10,
    top_languages = {
        lua = "21.7%",
        go = "17.1%",
        python = "15.9%",
        r = "11.4%",
        shell = "11.3%",
        cuda = "7.5%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
