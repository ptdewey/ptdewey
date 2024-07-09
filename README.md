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
    total_stargazers = 64,
    total_commits_current_year = 288,
    total_prs = 34,
    total_issues = 10,
    top_languages = {
        lua = "44.9%",
        go = "13.2%",
        python = "11.9%",
        r = "8.5%",
        shell = "8.5%",
        cuda = "5.6%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
