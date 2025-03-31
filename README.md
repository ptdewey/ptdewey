<!--CONTENT_START-->
```lua
-- user-profile.lua
local ptdewey = {}

-- user info
ptdewey.info = {
    name = "patrick dewey",
    education = {
        masters = "computer science at virginia tech",
        bachelors = "computational modeling and data analytics at virginia tech"
    }
}

-- user stats
ptdewey.stats = {
    total_repositories = 43,
    total_stargazers = 267,
    total_commits_current_year = 120,
    total_prs = 68,
    total_issues = 19,
    top_languages = {
        go = "29.9%",
        lua = "23.1%",
        python = "10.1%",
        r = "6.9%",
        shell = "6.9%",
        cuda = "4.8%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
