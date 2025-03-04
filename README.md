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
    total_repositories = 38,
    total_stargazers = 253,
    total_commits_current_year = 49,
    total_prs = 61,
    total_issues = 17,
    top_languages = {
        go = "28.1%",
        lua = "23.1%",
        python = "10.2%",
        r = "7.0%",
        shell = "7.0%",
        cuda = "4.8%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
