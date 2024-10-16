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
    total_stargazers = 211,
    total_commits_current_year = 591,
    total_prs = 47,
    total_issues = 13,
    top_languages = {
        go = "27.6%",
        lua = "27.4%",
        python = "11.6%",
        shell = "8.4%",
        r = "7.9%",
        cuda = "5.5%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
