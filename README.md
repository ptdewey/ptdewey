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
    total_stargazers = 169,
    total_commits_current_year = 498,
    total_prs = 47,
    total_issues = 13,
    top_languages = {
        lua = "28.9%",
        go = "25.9%",
        python = "12.4%",
        shell = "9.2%",
        r = "8.9%",
        cuda = "5.8%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
