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
    total_stargazers = 57,
    total_commits_current_year = 268,
    total_prs = 33,
    total_issues = 10,
    top_languages = {
        lua = "21.8%",
        go = "17.6%",
        python = "15.7%",
        r = "11.3%",
        shell = "11.2%",
        cuda = "7.4%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
