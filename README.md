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
    total_repositories = 34,
    total_stargazers = 185,
    total_commits_current_year = 536,
    total_prs = 47,
    total_issues = 13,
    top_languages = {
        go = "27.5%",
        lua = "27.3%",
        python = "11.7%",
        shell = "8.7%",
        r = "8.4%",
        cuda = "5.5%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
