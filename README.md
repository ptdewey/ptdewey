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
    total_repositories = 28,
    total_stargazers = 57,
    total_commits_current_year = 243,
    total_prs = 31,
    total_issues = 10,
    top_languages = {
        lua = "21.4%",
        go = "17.0%",
        python = "15.8%",
        r = "11.4%",
        shell = "11.1%",
        cuda = "7.4%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
