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
    total_stargazers = 132,
    total_commits_current_year = 415,
    total_prs = 42,
    total_issues = 12,
    top_languages = {
        lua = "29.5%",
        go = "24.7%",
        python = "12.5%",
        shell = "9.5%",
        r = "9.0%",
        cuda = "5.9%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
