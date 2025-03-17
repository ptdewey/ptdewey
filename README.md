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
    total_repositories = 39,
    total_stargazers = 256,
    total_commits_current_year = 72,
    total_prs = 61,
    total_issues = 17,
    top_languages = {
        go = "28.7%",
        lua = "23.0%",
        python = "10.2%",
        r = "6.9%",
        shell = "6.9%",
        cuda = "4.8%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
