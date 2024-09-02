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
    total_repositories = 33,
    total_stargazers = 148,
    total_commits_current_year = 425,
    total_prs = 44,
    total_issues = 12,
    top_languages = {
        lua = "30.2%",
        go = "24.5%",
        python = "12.4%",
        shell = "9.4%",
        r = "8.9%",
        cuda = "5.8%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
