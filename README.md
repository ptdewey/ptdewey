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
    total_repositories = 32,
    total_stargazers = 95,
    total_commits_current_year = 377,
    total_prs = 41,
    total_issues = 11,
    top_languages = {
        lua = "38.4%",
        go = "21.6%",
        python = "11.0%",
        shell = "8.2%",
        r = "7.9%",
        cuda = "5.2%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
