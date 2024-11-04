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
    total_stargazers = 226,
    total_commits_current_year = 644,
    total_prs = 52,
    total_issues = 14,
    top_languages = {
        go = "28.3%",
        lua = "27.6%",
        python = "11.5%",
        shell = "8.7%",
        r = "7.9%",
        cuda = "5.4%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
