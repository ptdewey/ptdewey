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
    total_stargazers = 269,
    total_commits_current_year = 134,
    total_prs = 68,
    total_issues = 19,
    top_languages = {
        go = "28.9%",
        lua = "25.7%",
        python = "9.7%",
        shell = "6.7%",
        r = "6.6%",
        cuda = "4.6%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
