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
    total_repositories = 35,
    total_stargazers = 224,
    total_commits_current_year = 621,
    total_prs = 48,
    total_issues = 13,
    top_languages = {
        go = "28.3%",
        lua = "27.7%",
        python = "11.5%",
        shell = "8.5%",
        r = "7.9%",
        cuda = "5.4%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
