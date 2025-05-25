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
    total_repositories = 46,
    total_stargazers = 289,
    total_commits_current_year = 193,
    total_prs = 74,
    total_issues = 25,
    top_languages = {
        go = "29.9%",
        lua = "25.7%",
        python = "9.4%",
        shell = "6.4%",
        r = "6.4%",
        cuda = "4.4%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
