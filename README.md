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
    total_commits_current_year = 272,
    total_prs = 33,
    total_issues = 10,
    top_languages = {
        lua = "41.2%",
        go = "13.2%",
        python = "11.8%",
        r = "8.5%",
        shell = "8.4%",
        cuda = "5.6%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
