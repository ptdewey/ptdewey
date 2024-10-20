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
    total_stargazers = 219,
    total_commits_current_year = 606,
    total_prs = 47,
    total_issues = 13,
    top_languages = {
        go = "27.8%",
        lua = "27.7%",
        python = "11.7%",
        shell = "8.6%",
        r = "8.0%",
        cuda = "5.5%"
    }
}

return ptdewey
```
<!--CONTENT_END-->
