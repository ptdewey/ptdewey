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
    total_repositories = 37,
    total_stargazers = 235,
    total_commits_current_year = 812,
    total_prs = 60,
    total_issues = 16,
    top_languages = {
        go = "27.1%",
        lua = "26.0%",
        python = "10.4%",
        shell = "7.9%",
        r = "7.1%",
        cuda = "4.9%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
