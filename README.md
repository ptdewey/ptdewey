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
    total_stargazers = 190,
    total_commits_current_year = 546,
    total_prs = 45,
    total_issues = 13,
    top_languages = {
        go = "27.6%",
        lua = "27.2%",
        python = "11.6%",
        shell = "8.5%",
        r = "7.9%",
        cuda = "5.5%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
