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
    total_repositories = 31,
    total_stargazers = 95,
    total_commits_current_year = 373,
    total_prs = 40,
    total_issues = 10,
    top_languages = {
        lua = "36.0%",
        go = "22.4%",
        python = "11.4%",
        shell = "8.6%",
        r = "8.2%",
        cuda = "5.4%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
