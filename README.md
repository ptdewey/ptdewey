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
    total_stargazers = 232,
    total_commits_current_year = 749,
    total_prs = 56,
    total_issues = 16,
    top_languages = {
        go = "27.0%",
        lua = "25.8%",
        python = "10.7%",
        shell = "8.0%",
        r = "7.3%",
        cuda = "5.0%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
