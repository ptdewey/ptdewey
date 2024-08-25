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
    total_stargazers = 95,
    total_commits_current_year = 404,
    total_prs = 41,
    total_issues = 12,
    top_languages = {
        lua = "39.0%",
        go = "21.4%",
        python = "10.8%",
        shell = "8.2%",
        r = "7.8%",
        cuda = "5.1%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
