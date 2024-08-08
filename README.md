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
    total_stargazers = 81,
    total_commits_current_year = 353,
    total_prs = 38,
    total_issues = 10,
    top_languages = {
        lua = "35.4%",
        go = "22.7%",
        python = "11.5%",
        shell = "8.7%",
        r = "8.3%",
        cuda = "5.4%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
