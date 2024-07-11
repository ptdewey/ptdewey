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
    total_repositories = 26,
    total_stargazers = 67,
    total_commits_current_year = 293,
    total_prs = 34,
    total_issues = 10,
    top_languages = {
        lua = "43.6%",
        go = "12.9%",
        python = "11.5%",
        shell = "11.2%",
        r = "8.3%",
        cuda = "5.4%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
