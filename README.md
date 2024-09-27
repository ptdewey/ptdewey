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
    total_repositories = 34,
    total_stargazers = 192,
    total_commits_current_year = 553,
    total_prs = 45,
    total_issues = 13,
    top_languages = {
        go = "27.8%",
        lua = "27.3%",
        python = "11.7%",
        r = "8.0%",
        shell = "7.9%",
        cuda = "5.5%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
