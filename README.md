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
    total_repositories = 36,
    total_stargazers = 171,
    total_commits_current_year = 509,
    total_prs = 47,
    total_issues = 13,
    top_languages = {
        lua = "28.1%",
        go = "25.3%",
        python = "12.1%",
        shell = "9.0%",
        r = "8.7%",
        cuda = "5.7%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
