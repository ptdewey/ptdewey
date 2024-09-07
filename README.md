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
    total_repositories = 35,
    total_stargazers = 154,
    total_commits_current_year = 431,
    total_prs = 44,
    total_issues = 13,
    top_languages = {
        lua = "29.0%",
        go = "25.4%",
        python = "12.5%",
        shell = "9.4%",
        r = "9.0%",
        cuda = "5.9%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
