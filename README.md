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
    total_repositories = 36,
    total_stargazers = 236,
    total_commits_current_year = 796,
    total_prs = 59,
    total_issues = 16,
    top_languages = {
        go = "26.7%",
        lua = "25.6%",
        python = "10.5%",
        shell = "8.0%",
        r = "7.2%",
        cuda = "5.0%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
