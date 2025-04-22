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
    total_repositories = 45,
    total_stargazers = 280,
    total_commits_current_year = 158,
    total_prs = 74,
    total_issues = 22,
    top_languages = {
        go = "29.6%",
        lua = "25.5%",
        python = "9.6%",
        shell = "6.6%",
        r = "6.5%",
        cuda = "4.5%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
