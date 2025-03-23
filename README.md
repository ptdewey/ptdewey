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
    total_repositories = 41,
    total_stargazers = 257,
    total_commits_current_year = 95,
    total_prs = 65,
    total_issues = 17,
    top_languages = {
        go = "29.4%",
        lua = "23.0%",
        python = "10.0%",
        r = "6.8%",
        shell = "6.8%",
        cuda = "4.7%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
