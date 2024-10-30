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
    total_stargazers = 225,
    total_commits_current_year = 633,
    total_prs = 49,
    total_issues = 13,
    top_languages = {
        go = "28.3%",
        lua = "27.6%",
        python = "11.5%",
        shell = "8.6%",
        r = "7.9%",
        cuda = "5.4%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
