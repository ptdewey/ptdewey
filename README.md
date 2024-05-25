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
    total_repositories = 27,
    total_stargazers = 54,
    total_commits_current_year = 219,
    total_prs = 31,
    total_issues = 9,
    top_languages = {
        lua = "21.6%",
        go = "17.0%",
        python = "16.2%",
        r = "11.6%",
        shell = "11.0%",
        cuda = "7.6%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
